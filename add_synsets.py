import conllu
import os
import yaml
import logging


logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


def match_condition(condition, synset_entry: dict, token: conllu.Token):
    value = synset_entry[condition]
    is_list = isinstance(value, list)
    if not is_list:
        if value == 'any':
            return True
        else:
            try:
                if token[condition] == value:
                    return True
                else:
                    return False
            except KeyError:
                try:
                    if token['feats'][condition] == value:
                        return True
                    else:
                        return False
                except KeyError:
                    try:
                        if token['misc'][condition] == value:
                            return True
                        else:
                            return False
                    except KeyError:
                        return False
    else:
        try:
            if token[condition] in value:
                return True
            else:
                return False
        except KeyError:
            try:
                if token['feats'][condition] in value:
                    return True
                else:
                    return False
            except KeyError:
                try:
                    if token['misc'][condition] in value:
                        return True
                    else:
                        return False
                except KeyError:
                    return False


def match_synset(synset_entry: dict, token: conllu.Token) -> bool:
    for condition in synset_entry:
        if not match_condition(condition, synset_entry, token):
            return False
    return True


if __name__ == '__main__':
    mypath = 'rv_conllu'
    hymns = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

    with open('synsets.yaml') as file:
        synsets_dict = yaml.load(file, Loader=yaml.FullLoader)
    
    logging.info('Iterating over treebank files...')

    for hymn in hymns:
        with open(os.path.join(mypath, hymn)) as file:
            tb = conllu.parse(file.read())

        for sent in tb:
            for token in sent:
                if not token['misc']:
                    token['misc'] = {}
                for synset in synsets_dict:
                    if match_synset(synsets_dict[synset], token):
                        if 'Synset' not in token['misc']:
                            token['misc']['Synset'] = synset
                        else:
                            token['misc']['Synset'] += ',' + synset

        with open(f'rv_synsets/{hymn}', 'w') as output:
            for sent in tb:
                output.write(sent.serialize())

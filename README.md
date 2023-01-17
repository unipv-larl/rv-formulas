<div align="center">
 
# Combining WordNets with Treebanks to study idiomatic language

[![Conference](https://img.shields.io/badge/conference-GWC--2023-blue.svg)](https://www.hitz.eus/gwc2023/)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

</div>

This is the repository for the paper [_Combining WordNets with Treebanks to study idiomatic language: A pilot study on Rigvedic formulas through the lenses of the Sanskrit WordNet and the Vedic Treebank_](), presented at the [Global Wordnet Conference 2023](https://www.hitz.eus/gwc2023/) by Luca Brigada Villa, Erica Biagetti, Riccardo Ginevra and Chiara Zanchi.

## Content of this repository

- [rv_conllu](rv_conllu): a directory containing a conllu file for each RgVeda hymn, automatically parsed by Oliver Hellwig's parser
- [synsets.yaml](synsets.yaml): a YAML file used to add automatically the synsets to the conllu files
- [add_synsets.py](add_synsets.py): the script used to add the synsets to the treebank
- [rv_synsets](rv_synsets): the directory where the conllu files with the synsets will be stored

## Download

You can download a copy of all the files in this repository by cloning it with the [git](https://git-scm.com/) command:

```sh
git clone https://github.com/unipv-larl/rv-formulas.git
```

or [download a zip archive](https://github.com/unipv-larl/rv-formulas/archive/master.zip)

## Requirements

**Programming language**: python3

**Modules and packages**: [conllu](https://pypi.org/project/conllu/), yaml, sys, logging, os

**Tool for querying the treebank**: [UDeasy](https://unipv-larl.github.io/udeasy/)

## Usage

### Annotating the synsets

After downloading this repo, open a terminal window and move into the repository.

```sh
cd path/to/rv-formulas
```

Then, run the python script executing this command:

```sh
python3 add_synsets.py
```

This will produce a conllu file for each file in the rv_conllu directory. These files will be annotated with the synsets listed in the YAML file and they will be stored in the rv_synsets folder.

Then to concatenate the files into one conllu file, run this command:

```sh
cat rv_synsets/*.conllu > rv.conllu
```

#### List of synsets added to the treebank

| meaning | synset | lemmas |
| ------- | ------ | ------ |
| ask | v#00608227 | yāc, pracch |
| say | v#00652168 | vad, ah |
| call | v#00501506 | hvā, vac, brū |
| deity | n#06861622 | deva, indra, agni, varuṇa, aśvin, vāyu, marut, mitra, savitṛ, sūrya, uṣas | 

### Extracting the potential formulas

To extract the patterns from the treebank, we used [UDeasy](https://unipv-larl.github.io/udeasy/), a tool for querying conllu files easily.

Open the tool and select the file corresponding to the treebank. In the nodes panel, enter these values:

| node | optional |
| ---- | -------- |
| verb | no |
| obj | no |
| subj | yes |
| advcl | yes |

Then, in the panel that appears after the confirmation, enter these values:

#### Features

| node | feature | value |
| ---- | ------- | ----- |
| verb | upos | VERB |
| obj | deprel | obj |
| subj | deprel | nsubj |
| advcl | deprel | [advcl, advcl:fin] |

#### Relations

| first node | relation | second node |
| ---- | ------- | ----- |
| verb | is parent of | obj |
| verb | is parent of | subj |
| verb | is parent of | advcl |

## Cite this work

```sh
@InProceedings{brigadavilla-et-al:2023:GWC23,
    author = {Brigada Villa, Luca and Biagetti, Erica and Ginevra Riccardo and Zanchi, Chiara},
    title = {Combining WordNets with Treebanks to study idiomatic language: A pilot study on Rigvedic formulas through the lenses of the Sanskrit WordNet and the Vedic Treebank},
    booktitle = {Proceedings of the Twelfth Global Wordnet Conference},
    month = {january},
    year = {2023},
    address = {Donostia-San Sebastián, Spain},
    publisher = {Global Wordnet Association},
    pages = {xxx-xxx}
    abstract = {yyy},
    url = {zzz}
}
```

## License

The data are distributed under a [CC-BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/).

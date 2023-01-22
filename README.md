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

| code in misc field | description | synset | lemmas |
| ------------------ | ----------- | ------ | ------ |
| ask | address a question to and expect an answer from | v#00608227 | yāc, pracch |
| say | use language | v#00652168 | vad, ah |
| call | utter in a loud voice or announce | v#00501506 | hvā, vac, brū |
| deity | any supernatural being worshipped as controlling some part of the world or some aspect of life or who is the personification of a force | n#06861622 | deva, indra, agni, varuṇa, aśvin, vāyu, marut, mitra, savitṛ, sūrya, uṣas | 

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

## References

- Mihailo Antović and Cristóbal Pagán Cánovas (eds.). 2016. *Oral Poetics and Cognitive Science*. Berlin/Boston, de Gruyter.

- Erica Biagetti, Chiara Zanchi and William M. Short. 2021. Toward the creation of WordNets for ancient Indo-European languages. In Proceeding of the 11th Global WordNet Conference. University of South Africa (UNISA): Global Wordnet Association, pages 258–266. https://aclanthology.org/2021.gwc-1.30

- Erica Biagetti. Forthc. Integrare Sanskrit WordNet e Vedic TreeBank: uno studio pilota sulla formularità del Rigveda tra semantica e sintassi. In Isabella Bossolino and Chiara Zanchi, Prospettive sull’antico. Decennalia dei Cantieri d’Autunno. Pavia, Pavia University Press.

- Chiara Bozzone. 2014. Homeric Constructions. PhD thesis, University of California, Los Angeles.

- Luca Brigada Villa. 2022. UDeasy: a Tool for Querying Treebanks in CoNLL-U Format. In Proceedings of the Workshop on Challenges in the Management of Large Corpora (CMLC-10), pages 16–19.

- William Croft and D. Alan Cruse. 2004. Cognitive Linguistics. Cambridge, Cambridge University Press.

- Christiane Fellbaum (ed.). 1998. WordNet: An electronic lexical database. MIT Press, Cambridge, MA.

- Charles J. Fillmore and Paul Kay. 1993. Construction grammar coursebook. Berkeley, University of California.

- Adele E. Goldberg. 1995. Constructions: a Construction Grammar Approach to Argument Structure. Chicago, Chicago University Press.

- John B. Hainsworth. 1968. The Flexibility of the Homeric Formula. Oxford, Clarendon.

- Oliver Hellwig. 2017. Coarse semantic classification of rare nouns using cross-lingual data and recurrent neural networks. In IWCS 2017-12th International Conference on Computational Semantics-Long papers, Montpellier, France.

- Oliver Hellwig, Salvatore Scarlata, Elia Ackermann, and Paul Widmer. 2020. The Treebank of Vedic Sanskrit. In Proceedings of The 12th Language Resources and Evaluation Conference (LREC 2020), pages 5137–5146.

- Stephanie W. Jamison 1998. Rigvedic viśvátaḥ sīm, or, Why syntax needs poetics. In Jay Jasanoff, H. Craig Melchert and Lisi Oliver, Mir curad: Studies in honor of Calvert Watkins, Innsbruck, Innsbrucker Beiträge zur Sprachwissenschaft, pages 291–299.

- Stephanie W. Jamison and Joel P. Brereton. 2014. The Rigveda. The Earliest Religious Poetry of India. Oxford, Oxford University Press.

- Paul Kiparsky. 1976. Oral Poetry: Some Linguistic and Typological Considerations. In Benjamin A. Stolz and Richard Stoll Shannon (eds.), Oral Literature and the Formula. Ann Arbor, Center for Coordination of Ancient and Modern Studies, pages 73-106.

- Albert B. Lord. 1960. The Singer of Tales. Cambridge, MA, Harvard University Press.

- Michael N. Nagler. 1967. Towards a Generative View of the Homeric Formula. Transactions of the American Philological Association 98:269–311.

- Gregory Nagy. 1974. Comparative Studies in Greek and Indic Meter. Cambridge, MA, Harvard University Press. 

- Joakim Nivre, Marie-Catherine de Marneffe, Filip Ginter et al. 2016. Universal Dependencies V1: A Multilingual Treebank Collection. In Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC'16), Portorož, Slovenia. European Language Resources Association (ELRA), pages 1659–1666.

- Cristóbal Pagán Cánovas and Mihailo Antović. 2016. Formulaic creativity: Oral poetics and cognitive grammar. Language & Communication 47:66–74.

- Parry, Milman. 1971 [1928]. The Traditional Epithet in Homer. In Adam Parry (ed.), The Making of Homeric Verse: The Collected Papers of Milman Parry. Oxford, Oxford University Press, pages 1–190.

- Joseph Russo. 1963. A Closer Look at Homeric Formulas. Transactions of the American Philological Association 94:235–247. 

- Joseph Russo. 1966. The Structural Formula in the Homeric Verse. Yale Classical Studies 20: 217-240.

- Calvert Watkins. 1976. Answer to P. Kiparsky’s Paper: Oral Poetry: Some Linguistic and Typological Considerations. In Benjamin A. Stolz and Richard S. Shannon (eds.), Oral Literature and the Formula. Ann Arbor, Center for Coordination of Ancient and Modern Studies, pages 107–111.

- Calvert Watkins. 1995. How to Kill a Dragon: Aspects of Indo-European Poetics. New York and Oxford, Oxford University Press.

- Chiara Zanchi, Silvia Luraghi and Erica Biagetti. 2021. Linking the Ancient Greek WordNet to the Homeric Dependency Lexicon. In Computational Linguistics and Intellectual Technologies. Papers from the Annual International Conference “Dialogue”, Vol. 20:729-737.

- Chiara Zanchi, Luca Brigada Villa, and Andrea Farina. 2022. Toward combining Ancient Greek WordNet and AGDT2 for linguistic research: A pilot study on formulas of Iliad. Paper presented at the 3rd International Colloquium on Ancient Greek Linguistics, Universidad Autónoma de Madrid, Spain, 16-18 June 2022.

## Cite this work

```sh
@InProceedings{brigadavilla-et-al:2023:GWC23,
    author = {Brigada Villa, Luca and Biagetti, Erica and Ginevra Riccardo and Zanchi, Chiara},
    title = {Combining WordNets with Treebanks to study idiomatic language: A pilot study on Rigvedic formulas through the lenses of the Sanskrit WordNet and the Vedic Treebank},
    booktitle = {Proceedings of the 12th Global Wordnet Conference},
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

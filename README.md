# Describe corpus
This is a dataset where each file is associated to a term (in english language). Each file in turn contains text snippets (one by row) for the associated term, which is the name of the file. The mentioned snippets were extracted by using the information extraction system called Describe. Mentioned system specializes in extracting snippets (from unrestricted internet sources) meeting syntactic patterns which are common in definitions of terms. 

We have a total amount of 5911 snippets. This number is limited by the number of snippets Describe returns for a given search input, i.e. only those terms (47 in total) which retrieved number of snippets is greater than or equal to 70 were considered. Plain text snippets are at the `~/txt` directory and CSVs are at the `~/csv` directory.

# Vector representations

Each text snippet was embedded into a document vector representation computed with the Doc2Vec distributional semantics method. Different dimensions for these vectors were computed: 10, 20, 30, 40, 50, 100 and 300. Vectors are in plain text format at `~/vectors_Hxxx` directories.

For all dimensions, the Doc2vec model was trained with the Wikipedia dump (year 2012). The training was performed in such a way the vocabulary of the model considers 2e6 articles for a first training. Afterwards the model was re-trained with 1.6e6 additional articles with no new vocabulary (3.6e6 articles in total).

## Work in progress 

It is pending adding semantic similarity labeling among snippets. This similarity is planned to be measured with respect to different semantic domains for each snippet (similarly to the SemEval datasets). Such a labeling is thought to be provided by using our semantic similarity annotation tool: https://github.com/iarroyof/define-semantic-annotation (any contribution is welcome.)

## Remark

Not all text snippets contain definitions. Some of them are uniquely snippets containing definitional patterns (in the sense of the simplest regexs like, e.g., `x` is a `y`, `x` is defined as `y`, etc.), which do not introduces concepts (semantically speaking) in aproximately 30% of the cases.

# Citation

Please do not forget citing this repository in the case you use all/part materials collected here:

```
@misc{arroyo2016,
    author = {Arroyo-Fern\'andez, Ignacio},
    keywords = {text snippets containing definitions of terms},
    note = {Grupo de ingenir\'ia ling\"u\'istica -- Universidad Nacional Aut\'onoma de M\'exico},
    title = {The Describe Corpus: A Recopilation of Text Snippets Containing Definitions of Terms from The Web},
    url = {http://github.com/iarroyof/describe_corpus}
    year = {2016}
}
```
## Acknowledgements

This work wouldn't be possible without collaboration of some ex-members from the "Grupo de Ingeniería Lingüística -- UNAM".

# Describe corpus
This is a dataset where each file is associated to a term (in english). Each file in turn contains text snippets (one by row) for the associated term. The mentioned snippets were extracted by using the information extraction system called Describe. Mentioned system specializes in extracting sentences (from unrestricted internet sources) meeting syntactic patterns which are common in definitions of terms. Thus the general sentence form we can see in the snippets of the corpus is that of definitional sentences (i.e. definitons of terms). We have 5911 snippets in total. This number is limited by the number of snippets Describe returns for a given search input, i.e. only those terms (47 in total) which retrieved number of snippets is greater or equal to 70 were considered. Plain text snippets are in `~/txt` and CSVs in `~/csv`.

# Vector representations

Each text snippet was embedded into document vector representations computed with Doc2Vec distributional semantics model. Different dimensions for these vectors were computed: 10, 20, 30, 40, 50, 100 and 300. Vectors are in plain text format at `~/vectors_Hxxx`.

For all dimensions, the Doc2vec model was trained with the Wikipedia corpus whose contents range up to 2012. The training was performed in such a way the vocabulary of the model considers 2e6 articles for a first training. Afterwards the model was re-trained with 1.6e6 additional articles with no new vocabulary (3.6e6 articles in total).

## Work in progress 

It is pending adding semantic similarity labeling among snippets. This similarity is planned to be measured with respect to different semantic domains for each snippet (not uniquely a pairwise similarity, as in the case of existent SemEval datasets). Such a labeling is thought to be provided by using our semantic similarity annotation tool: https://github.com/iarroyof/define-semantic-annotation (any contribution is welcome.)

## Remark

Not all text snippets contain definitions. Some of them are uniquely snippets containing definitional patterns (in the sense of the simplest regexs), which do not introduces concepts (semantically speaking) in aproximately 30% of the cases.

# Citation

Please do not forget citing this repository in the case you use all/part materials collected here:

```
@misc{arroyo2016,
    author = {Arroyo-Fern\'andez, Ignacio},
    keywords = {text snippets containing definitions of terms},
    note = {Universidad Nacional Aut\'onoma de M\'exico},
    title = {{The Describe Corpus: A Recopilation of Text Snippets Containing Definitions of Terms from The Web}},
    url = {http://github.com/iarroyof/describe_corpus}
    year = {2016}
}
```

# Describe corpus
This is a dataset where each file is associated to a term (in english language). Each file in turn contains text snippets (one by row) for the associated term, which is the name of the file. The mentioned snippets were extracted by using the information extraction system called Describe. Mentioned system specializes in extracting snippets (from unrestricted internet sources) meeting syntactic patterns which are common in definitions of terms. 

We have a total amount of 5911 snippets. This number is limited by the number of snippets Describe returns for a given search input, i.e. only those terms (47 in total) which retrieved number of snippets is greater than or equal to 70 were considered. Plain text snippets are at the `~/txt` directory and CSVs are at the `~/csv` directory.

# Vector representations

Each text snippet was embedded into a sentence vector representation computed with the [WISSE](https://github.com/iarroyof/sentence_embedding) method. We used FastText word embeddings of 300d. Vectors are in plain text format at `~/vectors/vectors*.mtx` files.

FastText model was trained with the Wikipedia dump (year 2012).

## Work in progress 

Semantic textual similarity annotation tool: https://github.com/iarroyof/define-semantic-annotation (any contribution is welcome.)

## Remark

Not all text snippets contain definitions. Some of them are uniquely snippets containing definitional patterns (in the sense of the simplest regexs like, e.g., `x` is a `y`, `x` is defined as `y`, etc.), which do not introduces concepts (semantically speaking) in aproximately 30% of the cases.

# Citation

Please do not forget citing this repository in the case you use all/part materials collected here:

```
@misc{arroyo2016,
    author = {Arroyo-Fern\'andez, Ignacio},
    keywords = {sense definitions},
    note = {Grupo de ingenir\'ia ling\"u\'istica -- Universidad Nacional Aut\'onoma de M\'exico},
    title = {The Describe Corpus: A Recopilation of Text Snippets Containing Sense Definitions Retrieved from The Web and their Emebddings},
    url = {http://github.com/iarroyof/describe_corpus}
    year = {2016}
}
```
## Acknowledgements

This work wouldn't be possible without collaboration of some ex-members from the "Grupo de Ingeniería Lingüística -- UNAM".

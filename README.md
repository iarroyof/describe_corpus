# Describe_corpus
This is a dataset where each file is associated to a term (in english). Each file in turn contains text snippets (one by row) for the associated term. The mentioned snippets were extracted by using the information extraction system called Describe. Mentioned systems specializes in extracting sentences meeting syntactic patterns which are common in definitions of terms. Thus the general sentence form we can see in the snippets of the corpus is that of definitional sentences (i.e. definitons of terms). We have 5911 snippets in total.

# Vector representations

Each text snippet was embedded into document vector representations computed with Doc2Vec distributional semantics model. Different dimensions for these vectors were computed: 10, 20, 30, 40, 50, 100 and 300. 

For all dimensions, the Doc2vec model was trained with the Wikipedia corpus whose contents range up to 2012. The training was performed in such a way the vocabulary of the model considers 2e6 articles for the first training. Afterwards the model was re-trained with 1e6 additional articles (3.6e6 articles in total).

# Remark. 

Not all text snippets contain definitions. Some of them are uniquely snippets containing definitional patterns (in the sense of the simplest regexs).

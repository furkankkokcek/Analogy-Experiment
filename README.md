# Analogy-Experiment
# Introduction

Embeddings are generally learned on a large corpus. Once the embeddings are trained,
how can we measure the quality of learned embeddings? How good an embedding represents the word’s features? One of the methods to evaluate an embedding’s quality is the
analogy. Analogy is question to find the relationships between words. For example, man
is to woman, what king is to . Here, the answer is queen. An illustration is given
in figure. Therefore in this task, you will perform some analogy experiments.  
<p align="center"><img src="https://qph.fs.quoracdn.net/main-qimg-64cbe26e66e787403be0bc1d268462b4"></p>

In the analogy prediction task, for a given a pair of words < a, b > and a third word c,
choose a fourth word d so that the analogy is built so that a is to b as c is to d holds.
In other words, the relationship between c and d should be as close as possible to that
of between a and b.
Mikolov et al. proposed some simple algebraic operations to apply for embeddings
to find an analogy between words. Let va be the vector of a and vb the vector of b. For another word d with a vector Vd we expect the following analogy:  
<p align="center">Vb − Va ≈ Vd − Vc (1)  </p>  
<p align="center">For example, Vwoman − Vman ≈ Vqueen − Vking. We therefore seek:</p>      
<p align="center">d∈V −{a,b,c}  </p>
<p align="center">d = argmax cos(vd, vb − va + vc) (2)</p>

which means we will seek the word which has a vector closest to Vb − Va + Vc, that will
be Vd. Note that the given words a, b, and c are excluded from consideration. The cosine
similarity is often used as a similarity metric between nonzero vectors. So, cos(va, vb)
gives how similar/close the two vectors are.


# Analogy Dataset
You will be given a subset of Mikolovs analogy dataset, which includes four
semantic relations and four syntactic relations. In the test files, each line represents one
analogy question, in the form of four words < a, b, c, d >. For example:  
<p align="center">Bangkok Thailand Cairo Egypt  </p>
A question is counted as correctly answered only if the predicted word is the same as
the given word. For example, given the first three words “Bangkok Thailand Cairo”, the
task is to predict “Egypt”. Note that this relationship is semantic and gives the capital
of relation between the two words.

The full set of analogy questions can be found in the file word-test.v1.txt in the project path. The groups of relations are delimited by lines starting with a colon (:)
and only these relations were used: capital-world, currency, city-in-state, family,
gram1-adjective-to-adverb, gram2-opposite, gram3-comparative, and gram6-nationalityadjective.

# Word Embeddings
Preferred, pretrained word embeddings so that no need to train embeddings in this task. I used word2vec trained embeddings [https://code.google.com/archive/p/word2vec/](https://code.google.com/archive/p/word2vec/)

# Evaluation 
This algorithm's accuracy evaluated by this formula :  
(#of correctly answered questions)/(#of questions attempted)  
Then accuracy of this algorithm is about %80. That means 80 percentage of predicted answers is correct according to real answers.

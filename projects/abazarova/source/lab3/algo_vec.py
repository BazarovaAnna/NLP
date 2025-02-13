from lab3.neur import *
from lab3.vectorize import score_tf_idf, tf_idf
from lab3.corpus import corpus
import numpy as np


def doc2vec(w2v, text_corp, train_corp):
    sent_vec = []
    for sent in text_corp:
        for token in sent:
            if token in list(w2v.wv.index_to_key):
                tfidf_score = score_tf_idf(tf_idf(train_corp))[token]
                vzv_vec = w2v.wv.get_vector(token)*tfidf_score
                sent_vec.append(vzv_vec)

    averaged = []
    for vec in sent_vec:
        averaged.append(np.average(vec, axis=0))
    return averaged


def algo_vec(mod_path, text_path, train_path):
    w2v = Word2Vec.load(mod_path)
    train = read_from_file(train_path)
    train_corpus = []
    for line in train:
        tmp = corpus(line)
        train_corpus += tmp
    text_corpus = []
    text = read_from_file(text_path)
    for line in text:
        tmp = corpus(line)
        text_corpus += tmp
    return doc2vec(w2v, text_corpus, train_corpus)


def make_vector_file(mod_path, text_path, train_path, rez_path):
    with open(rez_path, "w+") as fout:
        w2v = Word2Vec.load(mod_path)
        train = read_from_file(train_path)
        train_corpus = []
        for line in train:
            tmp = corpus(line)
            train_corpus += tmp
        text = read_from_file(text_path)
        doc_count = 0
        for line in text:
            doc_count += 1
            tmp = corpus(line)
            doc_vect = doc2vec(w2v, tmp, train_corpus)
            # print(doc_vect)
            fout.write(str(doc_count)+"\t"+"\t".join(str(elem) for elem in doc_vect))
            fout.write("\n")
            print("обработан док номер:",doc_count)


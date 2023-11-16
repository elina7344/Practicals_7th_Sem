corpus = ["Rafael Nadal Joins Roger Federer in Missing U.S. Open",
          "Rafael Nadal Is Out of the Australian Open",
          "Biden Announces Virus Measures",
          "Biden's Virus Plans Meet Reality",
          "Where Biden's Virus Plan Stands"]

import nltk
nltk.download('stopwords')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import LatentDirichletAllocation as LDA
from nltk.corpus import stopwords

count_vect = CountVectorizer(stop_words=stopwords.words('english'),lowercase=True)
x_counts = count_vect.fit_transform(corpus)
x_counts.todense()

count_vect.get_feature_names()

tfidf_transformer = TfidfTransformer()
x_tfidf = tfidf_transformer.fit_transform(x_counts)

dimension = 2
lda = LDA(n_components = dimension)
lda_array = lda.fit_transform(x_tfidf)
lda_array

components = [lda.components_[i] for i in range(len(lda.components_))]
print("components:",components)
features = count_vect.get_feature_names()
important_words = [sorted(features,key = lambda x: components[j][features.index(x)], reverse = True)[:3] for j in range(len(components))]
important_words

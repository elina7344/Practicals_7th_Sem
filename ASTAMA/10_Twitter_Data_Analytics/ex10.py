import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras

data = pd.read_csv("Twitter_Data.csv")
data.head(5)

data.isnull().sum()

data.shape

data.category.nunique(), data.category.unique()

data = data.dropna()
data.isnull().sum()

#Shuffling the data
data = data.sample(frac = 1).reset_index(drop = True)
data.head(5)

#one hot encoding
labels = pd.get_dummies(data.category)
labels.columns = ["negative", "neutral", "positive"]
labels.head(5)

#Dropping instances with null values
data = data.drop(columns = "category")
data.head(3)

#Tokenization
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
tokenizer = Tokenizer(num_words = 8150, lower = True, split = " ", oov_token = "~")
tokenizer.fit_on_texts(data["clean_text"])

word_index = tokenizer.word_index
len(word_index)

print(list(word_index.keys())[:100]) #first 100 tokens in word_index

data["clean_text"] = tokenizer.texts_to_sequences(data["clean_text"])
data.head(3)

len(data.clean_text[0]), len(data.clean_text[1]), len(data.clean_text[2])
#length of the sequences are different

tweets = pad_sequences(data["clean_text"]) #padding the sequences to get same shapes

tweets[0].shape, tweets[1].shape, tweets[2].shape
#now length of each sequence is same

tweets.shape

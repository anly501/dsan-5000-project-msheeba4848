#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


# In[42]:


def text(text):
    if isinstance(text, str):
        return text.lower()  # Example: Convert text to lowercase
    return text  # If not a string, return as is


# In[6]:


baseURL = "https://newsapi.org/v2/everything?"
total_requests = 2
verbose = True
API_KEY = ['ab5b4817320d445a8b369a95be58c90a']
TOPIC = ['fiscal policy', 'macroeconomic']

post1 = {
    'apiKey': API_KEY,
    'q': '+' + TOPIC[0],
    'sortBy': 'relevancy',
    'totalRequests': 1
}

post2 = {
    'apiKey': API_KEY,
    'q': '+' + TOPIC[1],
    'sortBy': 'relevancy',
    'totalRequests': 1
}


# In[7]:


def dumpjson(baseURL,URLpost):
    response = requests.get(baseURL, URLpost)
    return response.json()

result1 = dumpjson(baseURL,post1)
result2 = dumpjson(baseURL,post2)


# In[11]:


# Define the filenames for the JSON files
file1_path = '/Users/sheebamoghal/Downloads/hello.json'
file2_path = '/Users/sheebamoghal/Downloads/hi.json'

# Create a list of (data, filename) pairs
data_and_files = [(result1, file1_path), (result2, file2_path)]

# Iterate over the data and filenames, and write each pair to a JSON file
for data, filename in data_and_files:
    with open(filename, 'w') as fp:
        json.dump(data, fp)


# In[12]:


news1 = pd.read_json('/Users/sheebamoghal/Downloads/hello.json')
news2 = pd.read_json('/Users/sheebamoghal/Downloads/hi.json')


# In[33]:


news1.head(5)


# In[43]:


news1['articles'] = news1['articles'].apply(lambda article: {
    'source': article.get('source'),
    'title': text(article.get('title')),
    'description': text(article.get('description'))
})

print(news1)


# In[44]:


news2['articles'] = news2['articles'].apply(lambda article: {
    'source': article.get('source'),
    'title': text(article.get('title')),
    'description': text(article.get('description'))
})


# In[45]:


news1.head(10)


# In[46]:


news2.head(10)


# In[47]:


from sklearn.feature_extraction.text import CountVectorizer

def countvectorizer(corpus):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names_out()
    return feature_names, X.toarray()

# Define your corpora
news1_title_corpus = news1['articles'].apply(lambda x: x['title']).to_list()
news1_description_corpus = news1['articles'].apply(lambda x: x['description']).to_list()
news2_title_corpus = news2['articles'].apply(lambda x: x['title']).to_list()
news2_description_corpus = news2['articles'].apply(lambda x: x['description']).to_list()


# Perform count vectorization and print the results
print("-------------NewsAPI Corpus Count Vectorized-------------")
print(countvectorizer(news1_title_corpus))
print(countvectorizer(news1_description_corpus))
print(countvectorizer(news2_title_corpus))
print(countvectorizer(news2_description_corpus))


# In[ ]:





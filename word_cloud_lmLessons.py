# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:20:01 2020

@author: Low
"""

import pandas as pd
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import warnings 
warnings.filterwarnings('ignore')

import nltk
#nltk.download('punkt')

#df = pd.read_csv('learnmienLessons.csv')
df = pd.read_csv('mien_primer.csv')
#print(lmlessons.shape)
#print(lmlessons.describe)
#print(lmlessons.sentences)

"""
df_book2 = pd.read_table('mien_primer_2.txt', delim_whitespace=False,header=None)
df_book3 = pd.read_table('mien_primer_3.txt', delim_whitespace=False,header=None)
df_book4 = pd.read_table('mien_primer_4.txt', delim_whitespace=False,header=None)
df_allBooks = pd.concat([df_book2,df_book3,df_book4])
df_allBooks.rename(columns={0:'sentences'}, 
                 inplace=True)

print(df_allBooks.shape)
print(df_allBooks.head(10))
"""



print(df.shape)

all_tokenized = []
for i in range(len(df)):
    tokenized = nltk.word_tokenize(df.sentences[i])
    #print(tokenized)
    for i in tokenized:
        i = i.replace(".","donotaddoolist")
        i = i.replace(",","donotaddoolist")
        i = i.replace("``","donotaddoolist")
        i = i.replace("''","donotaddoolist")
        i = i.replace("?","donotaddoolist")
        i = i.lower()
        if i != "donotaddoolist":
            all_tokenized.append(i)

#print(all_tokenized)

fdist = nltk.FreqDist(all_tokenized)

wordCloudText = fdist.most_common(400)
#print(fdist)

#print(wordCloudText)

df_mostCommon = pd.DataFrame(wordCloudText)

print(df_mostCommon.head(30))
print(df_mostCommon.shape)

"""
text = " ".join(words for words in df.sentences)
print ("There are {} words in the combination of all lessons.".format(len(text)))

image_mask = np.array(Image.open("logoBig2.png"))
#image_mask

# Create and generate a word cloud image:
wordcloud = WordCloud(max_font_size=200,
                      max_words=400,
                      mask=image_mask,
                      contour_width=3,
                      contour_color='white',
                      background_color="black").generate(text)

# Display the generated image:

plt.imshow(wordcloud, interpolation='bilinear')
plt.title("Longc Camv Jiex Wuov Jioux Waac")
plt.axis("off")
plt.show()

# Save the image in the img folder:
wordcloud.to_file("allLessonsHighRes.png")
"""

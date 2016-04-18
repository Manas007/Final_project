{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf460
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from __future__ import division\
import pandas as pd\
import numpy as np\
from collections import defaultdict\
import cPickle as p\
import sys\
\
\
transitionDictionary=dict()\
emissionDictionary=dict()\
countEmissionDictionary=dict()\
countTransitionDictionary=dict()\
WordDictionary=defaultdict(list)\
emissionP=[]\
filename= sys.argv[-1]\
with open(filename,"r")as f:\
    for line in f:\
        prevTag='START'\
        for y in line.split():\
            word=y.rsplit("/",1)[0]\
            currTag=y.split("/")[-1]\
            emissionKey=y\
            transitionKey=prevTag+"|"+currTag\
            if(word in WordDictionary):\
                listTags=WordDictionary[word]\
                if(currTag not in listTags):\
                     WordDictionary[word].append(currTag)\
            else:\
                WordDictionary[word].append(currTag)\
            if(prevTag in countTransitionDictionary):\
                countTransitionDictionary[prevTag]+=1\
            else:\
                countTransitionDictionary[prevTag]=1\
\
            if(currTag in countEmissionDictionary):\
                countEmissionDictionary[currTag]+=1\
            else:\
                countEmissionDictionary[currTag]=1\
\
            if(emissionKey in emissionDictionary):\
                emissionDictionary[emissionKey]+=1\
            else:\
                emissionDictionary[emissionKey]=1\
            if(transitionKey in transitionDictionary):\
                transitionDictionary[transitionKey]+=1\
            else:\
                transitionDictionary[transitionKey]=1\
            prevTag=currTag\
\
\
\
model=[transitionDictionary,countTransitionDictionary,emissionDictionary,countEmissionDictionary,WordDictionary]\
p.dump(model,open("hmmmodel.txt","wb"))}
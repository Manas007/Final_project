{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf460
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from __future__ import division\
import numpy as np\
from collections import defaultdict\
import ast\
import cPickle as p\
import math\
import sys\
import os\
\
transitionDictionary=dict()\
countTransitionDictionary=dict()\
emissionDictionary=dict()\
countEmissionDictionary=dict()\
WordDictionary=defaultdict(list)\
\
listModels=[]\
listModels=p.load(open("hmmmodel.txt","rb"))\
transitionDictionary=listModels[0]\
countTransitionDictionary=listModels[1]\
emissionDictionary=listModels[2]\
countEmissionDictionary=listModels[3]\
WordDictionary=listModels[4]\
setTags=countTransitionDictionary.keys()\
filename=sys.argv[-1]\
\
\
with open(filename,"r")as f,open("hmmoutput.txt","w")as r:\
    for line in f:\
        prevTag='START'\
        count=0\
        viterbi=[]\
        backpointer=[]\
        for word in line.split():\
            count+=1\
            tempTags=WordDictionary[word]\
            if not tempTags:\
                tempTags=setTags\
            if(count==1):\
                first_viterbi=\{\}\
                first_backpointer=\{\}\
                for tag in tempTags:\
                    if tag=='START':\
                        continue\
                    if prevTag+"|"+tag in transitionDictionary:\
                    	Num1=transitionDictionary[prevTag+"|"+tag]\
                        Den1=countTransitionDictionary[prevTag]\
                    else:\
                    	Num1=1\
                        Den1=95673\
                    \
                    if word+"/"+tag in emissionDictionary:\
                        Num2=emissionDictionary[word+"/"+tag]\
                        Den2=countEmissionDictionary[tag]\
                    else:\
                        Num2=1\
                        den2=95673\
                    \
                    Prob=(Num1/Den1)*(Num2/Den2)\
                    first_viterbi[tag]=Prob\
                    first_backpointer[ tag ] = 'START'\
                viterbi.append(first_viterbi)\
                backpointer.append(first_backpointer)\
            else:\
                this_viterbi = \{\}\
                this_backpointer = \{\}\
                prev_viterbi = viterbi[-1]\
                for tag in tempTags:\
                    if tag=='START':\
                        continue\
                    max=0\
                    best_previous=""\
                    for key in prev_viterbi:\
                        if key+"|"+tag in transitionDictionary:\
                            Num1=transitionDictionary[key+"|"+tag]\
                            Den1=countTransitionDictionary[key]\
                        else:\
                            Num1=1\
                            Den1=95673\
                        \
                        if word+"/"+tag in emissionDictionary:\
                            Num2=emissionDictionary[word+"/"+tag]\
                            Den2=countEmissionDictionary[tag]\
                        else:\
                            Num2=1\
                            Den2=95673\
                        \
                        if prev_viterbi[key]< math.pow(10,-300):\
                            prev_viterbi[key]*=math.pow(10,200)\
                        Prob=prev_viterbi[key]*(Num1/Den1)*(Num2/Den2)\
                        if (Prob>max):\
                            max=Prob\
                            best_previous=key\
                    this_viterbi[tag] = max\
                    this_backpointer[tag] = best_previous\
                viterbi.append(this_viterbi)\
                backpointer.append(this_backpointer)\
\
        #print backpointer\
        prev_viterbi = viterbi[-1]\
        max=0\
        best_previous=""\
        for key in prev_viterbi:\
            if(prev_viterbi[key]>max):\
                max=prev_viterbi[key]\
                best_previous=key\
\
        best_tagsequence = [ "END", best_previous ]\
        # invert the list of backpointers\
        backpointer.reverse()\
\
        # go backwards through the list of backpointers\
        # (or in this case forward, because we have inverter the backpointer list)\
        # in each case:\
        # the following best tag is the one listed under\
        # the backpointer for the current best tag\
        current_best_tag = best_previous\
        #print line\
        for bp in backpointer:\
            best_tagsequence.append(bp[current_best_tag])\
            current_best_tag = bp[current_best_tag]\
\
        tempL=best_tagsequence[::-1]\
        tempx=tempL[1:-1]\
        #print tempx\
        count1=0\
        for word in line.split():\
            r.write(word+"/"+tempx[count1]+" ")\
            count1+=1\
        r.write("\\n")        \
\
\
\
\
\
\
}
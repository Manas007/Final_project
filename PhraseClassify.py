#coding: utf - 8
import codecs
import re
import math
import urllib
from textblob import TextBlob
from collections import OrderedDict

swapPointsList=["और","भी","था","थी","मे","से","पर","की","है","जो" ,"कोई" ,"तक","की"]
conjunctions=[",","और","मगर","इसलिए","लेकिन","पर","चाहे","या","तो","जबकि","एंव","या","फिर","नहीं","तो","जैसे","कि",]
auxVerb=[]
ChunkList=[]
ChunkListSecond=[]

def findDel(tempLine):
      diff=100000
      conj=""
      for x in conjunctions:
          if x in tempLine:
              tempSentences=tempLine.split(x,2)
              firstPart=[y for y in tempSentences[0].split()]
              len_x=len(firstPart)
              secondPart=[y for y in tempSentences[1].split()]
              len_y=len(secondPart)
              if(abs(len_x-len_y)<=diff):
                  conj=x
                  diff=abs(len_x-len_y)
      return tempLine.split(conj,2)


def findSwapPoint(tempLine):
    for x in swapPointsList:
        if x in tempLine:
            tempSentences=tempLine.split(x,2)
            print tempSentences
            firstPart=[y for y in tempSentences[0].split()]
            fList=list(firstPart)
            len_x=len(firstPart)
            secondPart=[y for y in tempSentences[1].split()]
            sList=list(secondPart)
            len_y=len(secondPart)
            if(abs(len_x-len_y)<=3):
                firstPart.extend(x)
                return firstPart,secondPart


    words=tempLine.split()
    for word,wordTag in words,ListWordTags:
        Tag=wordTag.split("/")[1]
        Tag=Tag="|"





    Chunks=["Determiner|Noun","Determiner|Adjective|Noun","Noun|Preposition","Noun|AuxVerb","Verb|AuxVerb","Verb|Pronoun","Pronoun|Verb","Adverb|Verb",
            "Noun|Noun","Adverb|Noun","Adjective|Noun","Adjective|Noun|Verb","Pronoun|Adjective|Noun","Pronoun|Noun|Adjective","Adverb|Adverb|Verb"]

    low=0
    mid=len(words)/2
    high=len(words)
    while(mid<=high):
        if(str(wordTag[mid-2]+"|"+wordTag[mid-1]+"|"+wordTag[mid]) in Chunks):
            tempSentences=tempLine.split(words[mid],2)
            tempSentences[0].extend(words[mid])
            return [tempSentences[0],tempSentences[1]]
        elif(str(wordTag[mid-1]+"|"+wordTag[mid]) in Chunks):
            tempSentences=tempLine.split(words[mid],2)
            tempSentences[0].extend(words[mid])
            return [tempSentences[0],tempSentences[1]]
        else:
            mid=mid+1






def matchRhyme(word1,word2):
    #str1 = "tekst"
    #word1+="टेक्स्ट"
    str1 = ""
    str2 = ""

    word1+= "टेक्स्ट"
    word2+= "टेक्स्ट"

    str1 += " " + word1
    str2 += " " + word2

    hindi_blob1 = TextBlob(str1)
    hindi_blob2 = TextBlob(str2)

    transliteratedtxt1 = hindi_blob1.translate(from_lang="hi", to='en')
    transliteratedtxt1=transliteratedtxt1.substring[:-5]
    transliteratedtxt2 = hindi_blob2.translate(from_lang="hi", to='en')
    transliteratedtxt2= transliteratedtxt2.substring[:-5]

    word1Index= len(transliteratedtxt1)
    word2Index= len(transliteratedtxt2)
    ##Matcing last charater if they are same!!
    if (transliteratedtxt1[word1Index-1] == transliteratedtxt2[word2Index-1]):

        #rhymeMeter=3;
        ##Matching if second Last character is any of the Matras!!
        if ( ((transliteratedtxt1[word1Index-2]=='a') and (transliteratedtxt2[word2Index-2]=='a')) or ((transliteratedtxt1[word1Index-2]=='e') and (transliteratedtxt2[word2Index-2]=='e'))or ((transliteratedtxt1[word1Index-2]=='o') and (transliteratedtxt2[word2Index-2]=='o')) or ((transliteratedtxt1[word1Index-2]=='i') and (transliteratedtxt2[word2Index-2]=='i')) or ((transliteratedtxt1[word1Index-2]=='u') and (transliteratedtxt2[word2Index-2]=='u')) ):
            rhymeMeter=5
        else:
            if(transliteratedtxt1[word1Index-2]!=transliteratedtxt1[word1Index-2]):
                rhymeMeter=4
    return rhymeMeter

ListWordTags=[]
with open("PosTag.txt","r") as posTagf:
    linef=posTagf.read()
    lines=linef.split("।")
    for line in lines:
        wordTags=line.split()
        ListWordTags.extend(wordTags)

with open("readHindi.txt","r")as f:
    linet=f.read()
    lines=linet.split("।")
    print len(lines)
    for line in lines:
        sentences=findDel(line)
        truncatedSentences=[]
        count=0
        firstList,secondList=findSwapPoint(sentences[0])
        firstList2,secondList2=findSwapPoint(sentences[1])
        count+=1
        rhymeMeter=0
        for e in firstList:
            for s in secondList:
                for m in e:
                    lastm=m.rsplit(" ",2)[-1]
                    for n in s:
                        lastn=n.rsplit(" ",2)[-1]
                        rMeter=matchRhyme(lastm,lastn)
                        if (rMeter>rhymeMeter):
                            Sentences=[]
                            rhymeMeter=rMeter
                            Sentences.append(m)
                            Sentences.append(n)

            Phrases[0].remove(Sentences[0])
            Phrases[1].remove(Sentences[1])


        #chunks=findChunks(line,pos,pod)


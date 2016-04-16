{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf460
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset77 KohinoorDevanagari-Regular;}
{\colortbl;\red255\green255\blue255;\red16\green19\blue26;\red255\green255\blue255;\red45\green68\blue134;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl358\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # coding: utf-8\
import codecs\
from bs4 import BeautifulSoup\
import re\
import urllib\
from textblob import TextBlob\
from collections import defaultdict\
import pickle\
dictglobalwordmeaning=\{\}\
hindipoem=u""\
globallist=[]\
word1=[]\
dictwordsposi=\{\}\
def posWord(hindipoem):\
    partOf=u""\
    partOf=hindipoem.split(" ")\
   # with codecs.open("C:/Users/Akanksha/Desktop/hindicleaneddata.txt", 'r', 'utf8') as f:\
    each=u""\
    val_itr=10\
    for each in partOf:\
        count_match=0\
        each=each.encode('utf-8')\
        #tempV = line.split(" ")[0].encode('utf-8')\
        r = urllib.urlopen('{\field{\*\fldinst{HYPERLINK "http://dict.hinkhoj.com/hindi-dictionary.php?word="}}{\fldrslt \cf4 \strokec4 http://dict.hinkhoj.com/hindi-dictionary.php?word=}}' + each + '&ie=UTF-8').read()\
        soup = BeautifulSoup(r)\
        lettersx = soup.find_all("a", \{'class': "hin_dict_span"\})\
        keyslist = []\
        elements=u""\
        for elements in lettersx:\
            # print "text:"+elements.text\
            comp=elements.text.encode('utf-8')\
            if each==comp:\
                count_match=count_match+1\
                keyslist.append(elements.text)\
        valuesList = []\
        letters = soup.find_all("span", class_="gram_dict_span")\
        elements=u""\
        for elements in letters:\
            if count_match<=0:\
                break\
            count_match=count_match-1\
            # print "POS:"+elements.text\
            valuesList.append(elements.text.encode('utf-8'))\
        for i in range(0,keyslist.__len__()):\
            if keyslist[i] in dictglobalwordmeaning:\
                dictglobalwordmeaning[keyslist[i]][valuesList[i]]=val_itr\
                val_itr=val_itr-1\
                if i==0 and valuesList[i]=="Noun":\
                    break\
            else:\
                dictglobalwordmeaning[keyslist[i]]=\{\}\
                dictglobalwordmeaning[keyslist[i]][valuesList[i]]=val_itr\
                val_itr=val_itr-1\
                if i == 0 and (valuesList[i] == "Noun" or valuesList[i]=="Conjunction" or valuesList[i]=="Pronoun"):\
                    break\
def posTag():\
    list_aux=u"
\f1 \uc0\u2352 \u2361 \u2366 
\f0 ,
\f1 \uc0\u2361 \u2370 \u2305 
\f0 ,
\f1 \uc0\u2341 \u2366 
\f0 ,
\f1 \uc0\u2361 \u2379 
\f0 ,
\f1 \uc0\u2361 \u2376 
\f0 ,
\f1 \uc0\u2361 \u2379 \u2327 \u2366 
\f0 ,
\f1 \uc0\u2361 \u2379 \u2340 \u2375 
\f0 ,
\f1 \uc0\u2361 \u2379 \u2306 \u2327 \u2375 
\f0 ,
\f1 \uc0\u2341 \u2375 
\f0 ,
\f1 \uc0\u2361 \u2379 \u2306 
\f0 ,
\f1 \uc0\u2361 \u2376 \u2306 
\f0 ,
\f1 \uc0\u2361 \u2379 \u2340 \u2375 
\f0 ,
\f1 \uc0\u2341 \u2368 
\f0 ,
\f1 \uc0\u2361 \u2370 \u2305 \u2327 \u2368 
\f0 ,
\f1 \uc0\u2361 \u2379 \u2340 \u2368 
\f0 ,
\f1 \uc0\u2361 \u2379 \u2306 \u2327 \u2368 
\f0 ,
\f1 \uc0\u2361 \u2379 \u2327 \u2368 
\f0 ,
\f1 \uc0\u2352 \u2361 \u2368 
\f0 ,
\f1 \uc0\u2352 \u2361 \u2375 
\f0 ,
\f1 \uc0\u2342 \u2375 \u2344 \u2366 
\f0 ,
\f1 \uc0\u2342 \u2375 \u2344 \u2375 
\f0 ,
\f1 \uc0\u2342 \u2379 
\f0 ,
\f1 \uc0\u2342 \u2375 \u2325 \u2375 
\f0 ,
\f1 \uc0\u2342 \u2375 \u2325 \u2352 
\f0 "\
    list_pronouns=""\
    line=u"
\f1 \uc0\u2357 \u2361 
\f0  
\f1 \uc0\u2346 \u2325 \u2381 \u2359 \u2367 \u2351 \u2379 \u2306 
\f0  
\f1 \uc0\u2344 \u2366 \u2330 
\f0  
\f1 \uc0\u2342 \u2375 \u2326 
\f0  
\f1 \uc0\u2325 \u2352 
\f0  
\f1 \uc0\u2361 \u2376 \u2352 \u2366 \u2344 
\f0  
\f1 \uc0\u2341 \u2366 
\f0 "\
    posWord(line)\
    final_dict=\{\}\
    outputstr1=u""\
    outputstr2 = u""\
    final_dict=dictglobalwordmeaning\
    file1=open("output.txt",'w')\
    # for key, val in dictglobalwordmeaning[.items():\
    #     file1.write(key[0].encode('utf-8') + ':' + key[1].encode('utf-8') + ';')\
    #     file1.write("\\n")\
    # print dictglobalwordmeaning\
    # for key,values in dictglobalwordmeaning:\
    #     outputstr1=key[0]\
    #     outputstr2=key[1]\
    #     print outputstr1,outputstr2\
    word1=line.split(" ")\
    str1="tekst"\
    str2=u""\
    for word in word1:\
        word+=u"
\f1 \uc0\u2335 \u2375 \u2325 \u2381 \u2360 \u2381 \u2335 
\f0 "\
        str2+=" "+word\
#file=codecs.open(f1,"r","utf-8")\
#for line in file:\
    hindi_blob = TextBlob(str2)\
    transliteratedtxt=hindi_blob.translate(from_lang="hi", to='en')\
    translated=transliteratedtxt.split(" ")\
    finaltranslittxt=""\
    i=0\
    for each in translated:\
        each=each[:-5]\
        if i==0:\
            finaltranslittxt=each\
            i=1\
        else:\
            finaltranslittxt+=" "+each\
    print finaltranslittxt\
    dicttranslit=\{\}\
    listtrans=finaltranslittxt.split(" ")\
    #creating the mapping between the transliterated words and the original words\
    for i in range(0,listtrans.__len__()):\
        dicttranslit[word1[i]]=listtrans[i]\
    finalPOSdict=\{\}\
    #printing the dictionary\
    for word in word1:\
        if word in dictglobalwordmeaning:\
            if dictglobalwordmeaning[word].keys()>0:\
                for key,val in dictglobalwordmeaning[word].items():\
                    print(dicttranslit[word]+" "+key)\
    # pickle.dump(dictglobalwordmeaning,file1)\
    for i in range(0,word1.__len__()):\
        if word1[i] in dictglobalwordmeaning:\
            mylist = dictglobalwordmeaning[word1[i]].keys()\
            if mylist.__len__()==1:\
                for key, value in dictglobalwordmeaning[word1[i]].items():\
                    finalPOSdict[word1[i]] = key\
            else:\
                continue\
                #rules\
        else:\
            continue\
            #rules\
    for i in range(0,word1.__len__()):\
        if word1[i] in list_aux:\
            finalPOSdict[word1[i]]="AuxVerb"\
            if i!=0:\
                if word1[i-1] not in finalPOSdict:\
                    finalPOSdict[word1[i-1]]="Verb"\
    for key,values in finalPOSdict.items():\
        globallist.append(key)\
    # for i in range(0,)\
    # while globallist.__len__()!=word1.__len__():\
posTag()\
}
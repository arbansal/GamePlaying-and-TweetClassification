Tweet Classification:
Steps followed:
1) fetching training data
2) Cleaning data: Removed special characters
3) Used BAG OF WORDS, ie, collected all the words in a variable]
4) classified words based on cities, ie.Classified words into diffrent groups based on cities
5) Found probablity of the word, given it belongs to city. ie P(word|city= Chicago),P(word|city= San Francisco) etc
6) Found probablity of tweet given the city. ie probablity that tweet belongs to particular city
7) multiply 5 and 6 to get the probablity required.
8) Assigned low probablity ie 0.0000000001 for new words.
9) Fetched training data
10)cleaned as its done for testing data
11)Removed some words with highest frequency like "the" 
12)If tweet has words like NY, San Francisco it had high probablity of belonging to that particular city, so have given max probablity for it

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import re
import sys
#import operator
#import more_itertools
#fname = "C:/Users/LENOVO/Downloads/tweets.train.clean.txt"
fname= sys.argv[1]
words=[]
num_words = 0
tweets=[]
label=[]

#Extracting Training data
with open(fname, 'r',errors='ignore') as f:
    for line in f:
        tweet = line
        tweet1=str(tweet.split(' ',1))
        tweet1.replace(",_","")
        tweet1.replace("_","")
        #tweet1.replace(",","")
        #tweet1=re.sub("[^A-Za-z0-9]+",' ',str(tweet1))
        tweets.append(tweet1)
        
        ltweet=tweet.split(' ', 1)[:1]
        label.append(ltweet)
        #print(tweets) 
        #for word in line.split():
        # word = re.sub(r"[^a-zA-z0-9]","",word.lower())
        # words.append(word)
        # num_words = num_words+1 
#print("Number of words:")
#print(num_words)
#print(tweets[1])
#print(label[1])
tweets[1]
len(tweets)


########################

########################

word=[]


#re.sub("[^A-Za-z0-9]+",' ',str(tweets[0]))
for i in range(0, len(tweets)):
    word_tweet=tweets[i].split(" ")
    
    word.append(word_tweet)
voc=[]
len(tweets)
(word[31000])
 
for i in range(0, len(word)):
  for k in range(0, len(word[i])):
    word[i][k]=word[i][k].replace("\\n","")
    word[i][k]=re.sub("[^A-Za-z0-9_]+",' ',word[i][k])
    word[i][k]=word[i][k].replace(" _","_")
    word[i][k]=word[i][k].replace(" ","")
    word[i][k]=word[i][k].upper()
    
    voc.append(word[i][k])
word[1]

##############################Cleaning DATA
#removing few words which used frequently and have less weight
 
stopwords = ['THE',"N", "", "A", "OF" , 'IN' ,"FOR", "",'']
for pk in range(0, len(word)):  # iterating on a copy since removing will mess things up
   for w in word[pk]:
       if w in stopwords:
        word[pk].remove(w)
#print(op_final)

###############################Getting the labels
label=np.unique(label)
voc=list(set(voc))
len(voc)
#label=list(flatten(label))
#label=set(label)
label[2]
# Creating BAG OF WORDS
#print(label[1])
for k in range(0, len(label)):
    label[k]=str(label[k]).replace("\\n","")
    label[k]=re.sub("[^A-Za-z0-9_]+",' ',label[k])
    label[k]=label[k].replace(" _","_")
    label[k]=label[k].replace(" ","")
    label[k]=label[k].upper()
all_words=[]  

total_tweets_of_city=[]
tt=0
city_words=[]
city_word=[]
## collecting words cityy wie! 
for m in range(0, len(label)):
    
    for n in range(0, len(word)):
        if label[m]== word[n][0]:
            tt=tt+1
            for b in range(1,len(word[n])):
                all_words.append(word[n][b])
                city_word.append(word[n][b])
    city_words.append(city_word)
    city_word=[]
    total_tweets_of_city.append(tt)
    
    tt=0
label[0]   
#city_words[0][0]

#len(city_words)

from collections import Counter
 
word_freq_city_wise=[]
for i in range(0, len(city_words)):
    count=Counter(city_words[i]) 
    word_freq_city_wise.append(count)
    

#cc=word_freq_city_wise[0]
#cc['And']

    
label=list(label)
total_tweets_of_city
sum(total_tweets_of_city)

len(all_words)
    
countall=Counter(all_words)
countall[""]
max(countall)
################################TEST DATA############################################
#fname = "C:/Users/LENOVO/Downloads/tweets.test1.clean.txt"
fname=sys.argv[2]
test_tweets=[]

test_labels=[]
test_full_tweets=[]
with open(fname, 'r',errors='ignore') as f:
    for line in f:
        tweet = line
        test_full_tweets.append(tweet)
        tweet2=(tweet.split()[1:])
        #tweet2.replace(",_","")
        #tweet2.replace("_","")
        #tweet1.replace(",","")
        #tweet1=re.sub("[^A-Za-z0-9]+",' ',str(tweet1))
        test_tweets.append(tweet2)
        
        ltweet=tweet.split(' ', 1)[:1]
        test_labels.append(ltweet)
        
len(test_tweets)

test_tweets[1]
test_labels[2]
test_pred=[]
###################################CLEANING OF TEST DATA
for i in range(0, len(test_tweets)):
  for k in range(0, len(test_tweets[i])):
    test_tweets[i][k]=test_tweets[i][k].replace("\\n","")
    test_tweets[i][k]=re.sub("[^A-Za-z0-9_]+",' ',test_tweets[i][k])
    test_tweets[i][k]=test_tweets[i][k].replace(" _","_")
    test_tweets[i][k]=test_tweets[i][k].replace(" ","")
    test_tweets[i][k]=test_tweets[i][k].upper()

for k in range(0, len(test_labels)):
    test_labels[k]=str(test_labels[k]).replace("\\n","")
    test_labels[k]=re.sub("[^A-Za-z0-9_]+",' ',test_labels[k])
    test_labels[k]=test_labels[k].replace(" _","_")
    test_labels[k]=test_labels[k].replace(" ","")
    test_labels[k]=test_labels[k].upper()
    


##########################PROBABLITY CALCULATION #################################################
def prob_word_given_city(city_number, word_in_tweet):
    #print("gi")
    val=len(voc)-len(label)
    val2=int(total_tweets_of_city[city_number])
    den=val+val2
    b=word_freq_city_wise[city_number]
    num=b[word_in_tweet]
    #return((num+1)/den)
    return 0.0000000001 if num ==0 else ((num+1)/den) 
#reurn very less probablity for new words  
prob_matrix =[] 

    
def prob_city(city_number):
    return(total_tweets_of_city[city_number]/sum(total_tweets_of_city))

#if tweet has keywords mentioned in the states list: 
    # there is high probablit that they will belong to that city tweet
states=["PHILADELPHIA","PA","WASHINGTON","DC","TX","HOUSTON","TORONTO ONTARIO","ONTARIO","LOS ANGELES","BOSTON", "MA", "CHICAGO","IL", "NY", "SAN FRANCISCO", "MANHATTAN","NY", "ATLANTA", "GA", "SAN DIEGO"]
#ba=["BOS" ,"Lo"]
#common=set(ba)&set(states)
#print(len(common))
label[0]
label_splitted=[]

for i in range(0, len(label)):
    sp= label[i].split("_")
    label_splitted.append(sp)

len(label_splitted)
#for b in ba:
    
 #print(b)
 #if b in states:
  #  print("YES")
 #else:
  #   print("n")
def checker(tester):
    tester_words= tester
    common= set(tester_words)&set(states)
    if len(common)>0:
        for k in range(0, len(tester_words)):
            if tester_words[k] in states:
                for mn in range(0, len(label)):
                    if tester_words[k] in label_splitted[mn]:
                        A=0.80
                        prob_matrix.append(A)
                        #assigning high probablity
                    else:
                        A=0.0000000000001
                        prob_matrix.append(A)
                    
    else:
      for i in range(0, len(label)):
    
        A=prob_city(i)
        
    #tester_words= tester.split(" ")
        for k in range(0, len(tester_words)):
            
                B= prob_word_given_city(i,tester_words[k] )
                A= A*B
        prob_matrix.append(A)
cm=[]
final_labels=[]
checker_matrix=[]       
for pp in range(0, len(test_tweets)):
    tester=test_tweets[pp]
    prob_matrix=[]
    checker(tester)
    m= max(prob_matrix)
    ind=prob_matrix.index(m)
#print(prob_matrix)
    #print(label[ind])
    test_labels[pp]
    final_labels.append(label[ind])
    cm.append(test_labels[pp])
    cm.append(label[ind])
    checker_matrix.append(cm)
    cm=[]


#Finding accuracy 
def accuracy(checker_matrix):
    cnt=0
    for i in range(0, len(checker_matrix)):
        if checker_matrix[i][0]==checker_matrix[i][1]:
            cnt=cnt+1
    print("Accuracy:",(cnt/len(checker_matrix)*100))
accuracy(checker_matrix)

#######################################################

## OUTPUT FILE 
for i in range(0, len(final_labels)):
    v=final_labels[i].split("_")
    if len(v)==2:
        final_labels[i]=final_labels[i].replace("_",",_")
    else:
        p=final_labels[i]
        q=list(p)
        lb=len(p)
        lb

        c=lb
        for b in range(0, len(p)):
            if q[c-1]=="_":
        
        
                q[c-1]=",_"
        
                break 
            c=c-1
        final_labels[i]=''.join(q)
        

#final_labels

###################################################


#Final labels are in list final_labels
total_tweets_of_city[0]
city_words[0]   

new_list=[]


for i in range(0, len(city_words)):
   cv=Counter(city_words[i])

   ll=sorted(cv, key=cv.get, reverse=True)
   new_list.append(ll)
label[0]    
new_list[0][1]
#def topfive():
    
########################################
new_label=[]
for i in range(0, len(label)):
    v=label[i].split("_")
    if len(v)==2:
        label[i]=label[i].replace("_",",_")
    else:
        p=label[i]
        q=list(p)
        lb=len(p)
        lb

        c=lb
        for b in range(0, len(p)):
            if q[c-1]=="_":
        
        
                q[c-1]=",_"
        
                break 
            c=c-1
        label[i]=''.join(q)
        
#label[0]

#######################################
op_list=[]
op_final=[]
for ik in range(0, len(label)):
    op_list.append(label[ik])
    for i in range(0,5):
        op_list.append(new_list[ik][i])
    op_final.append(op_list)
    op_list=[]
for i in range(0, len(op_final)):
    print(op_final[i])


#output_file= "C:/Users/LENOVO/Desktop/out.txt"
output_file=sys.argv[3]
with open(output_file,'w+') as out_file:
    for i in range(0, len(final_labels)):
        out_file.write(final_labels[i]+' '+test_full_tweets[i])

 #break

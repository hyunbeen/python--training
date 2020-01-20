import csv
import operator
from pykospacing import spacing
from konlpy.tag import Twitter

def findfeq(worddict,data):
    pass
twitter = Twitter()
f = open('practice/train.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
i = 0
worddict = {};
wordlist = []
wordfreq = []

# str = "히라마블로그에온걸^^환영해1993!"
# print(spacing(str))
for line in rdr:
    
    if(i!=0):
        
        message =list(line) 
        sms = message[2]
        sentencelist = list(sms.split('.'))
       
        
        for sentence in sentencelist :
            sentence = sentence.replace(' ','')
            sentence = spacing(sentence)
        
            word = list(sentence.split(' '))
        
            for j in word:
            
                divlist = list(twitter.pos(j))
    
                for (word,wordtype) in divlist :
                
                    if((wordtype=='Noun')|(wordtype=='Adjective')|(wordtype=='Numver')):
                    
                        if(worddict.get(j)==None):
                            worddict[j]=1
                        else:
                            worddict[j]+=1
                        pass
                
                    pass

                pass

            # print("===========================================================")
            # print(j)
            # print(twitter.pos(j))
            # print("==========================================================")
            
            # if(i==2):
            #     print(type(spacing(j)))
            # if(worddict.get(j)==None):
            #     worddict[j] = 1
            # else:
            #     worddict[j]+=1
            # pass
        
            pass


        pass

        

    i += 1    
    if(i==1000):
        break
        
        
            
     
        
    


    
    
    

print("\n")
# sorted_worddict = sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
sorted_worddict = sorted(worddict.items(),key=operator.itemgetter(1))
print("------------------------------------------------------------------------------------------------------------------------------")
print(sorted_worddict)
print("------------------------------------------------------------------------------------------------------------------------------")

f.close()    


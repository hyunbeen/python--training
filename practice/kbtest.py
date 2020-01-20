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


for line in rdr:
    
    if(i!=0):
        
        message =list(line) 
        sms = message[2]        #문자 한개  
        sms = sms.replace(' ','')           #띄어쓰기 제거
        divlist = list(twitter.pos(sms))        #의미있는 단어 추출    


        #단어 리스트 검사
        for (word,wordtype) in divlist :
                
            if((wordtype=='Noun')|(wordtype=='Adjective')|(wordtype=='Numver')):
                    
                if(worddict.get(word)==None):
                    worddict[word]=1
                else:
                    worddict[word]+=1
                pass
                
            pass

        pass

            

        

    i += 1    
    if(i==100):
        break
        
        
            
     
        
    


    
    
    

print("\n")
# sorted_worddict = sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
sorted_worddict = sorted(worddict.items(),key=operator.itemgetter(1))
print("------------------------------------------------------------------------------------------------------------------------------")
print(sorted_worddict)
print("------------------------------------------------------------------------------------------------------------------------------")

f.close()    


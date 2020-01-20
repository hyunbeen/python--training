from konlpy.tag import Twitter
 
twitter = Twitter()
str = "히라마블로그에온걸^^환영해1993!"
divlist = list(twitter.pos(str))

for (word,wordtype) in divlist :
    print(word)
    print(wordtype) 
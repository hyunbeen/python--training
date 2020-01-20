#sample9.py
word = "Yoseph, Kim";
shape = "=";
it = 80;
spacenum = int((it-len(word))/2)
space = ' ';
newline = '\n';
result = shape*it+newline+space*spacenum+word+space*spacenum+newline+shape*it
print(result)

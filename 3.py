
import chardet

f = open('lin.txt','r')

fencoding=chardet.detect(f.read())

print (fencoding)
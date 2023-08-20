f1 = open('transcript.txt','r')
f2 = open('opLower.txt','w')
#print(f.read())
for line in f1:
    low = line.lower()
    f2.write(low)
f1.close()
f2.close()

f3 = open('opLower.txt','r')
print(f3.read(100))
f3.close()
from alphabet import alphabet

rows = 11

text = raw_input('Enter text:\n')
c = map(lambda x: ord(x)-ord('a'),text)
s = ""
for i in range(rows):
    for j in c:
        s+= alphabet[j][i]
    s+= "\n"

print s

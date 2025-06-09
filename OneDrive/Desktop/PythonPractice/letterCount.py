letter = "Hello I am a man from Nepal"
count = {}

for i in letter: 
    if i != ' ':
        count.setdefault(i, 0)
        count[i] += 1

print(count)
sentence = "I am from Nepal"
sentence = sentence.split()
count = {}

for k in sentence:
    count.setdefault(k, 0)
    count[k] += 1

print(count)
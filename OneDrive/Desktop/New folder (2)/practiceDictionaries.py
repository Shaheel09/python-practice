# pc = {'motherboard': 45000, 'cpu':55000, 'graphics card': 98000, 'Ram': 6000}

# for computer in pc.keys():
#     print(computer)

# for computer in pc.values():
#     print(computer)

# for comp, price in pc.items():
#     print(comp,price)

# pc.setdefault('rom', 4000)

# pc['motherboard'] = 50000

# print('motherboard' not in pc.keys())

# userEnter = input('Enter a Sentence: ')
# words = userEnter.split()

# capture = {}

# for i in words:
#     capture.setdefault(i,0)
#     capture[i] = capture[i] + 1

# print(capture)


# userEnter = input('Enter a Sentence: ')
# words = userEnter.lower()

# capture = {}

# for i in words:
#     if i != ' ':
#         capture.setdefault(i,0)
#         capture[i] += 1

# print(capture)

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

capture = {}

for i in items:
    capture.setdefault(i, 0)
    capture[i] = capture[i] + 1
print(capture)
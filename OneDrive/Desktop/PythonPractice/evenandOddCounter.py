def evenAndOddCounter(number):
    evenCount = 0
    oddCount = 0
    for num in number:
        if num % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    
    return evenCount,oddCount

spam = [1,2,3,4,5,6,7,8,9,10]

print(evenAndOddCounter(spam))


# def posNegCounter(number):

#     postiveCount = 0
#     negativeCount = 0
#     zeroCount = 0

#     for num in number:
#         if num > 0:
#             postiveCount += 1
#         elif num < 0:
#             negativeCount += 1
#         else:
#             zeroCount += 1
        
#     return postiveCount,negativeCount,zeroCount

# spam = [3, -1, 0, 5, -4, 0, 7, -2]

# print(posNegCounter(spam))



# def vowelsCounter(vowels):

#     vowelsCount = 0
#     for letter in vowels:
#         if 'a' in letter:
#             vowelsCount +=1
#         elif 'e' in letter:
#             vowelsCount += 1
#         elif 'i' in letter:
#             vowelsCount += 1
#         elif 'o' in letter:
#             vowelsCount += 1
#         elif 'u' in letter:
#             vowelsCount += 1 
#         elif 'A' in letter:
#             vowelsCount += 1
#         elif 'E' in letter:
#             vowelsCount += 1
#         elif 'I' in letter:
#             vowelsCount += 1
#         elif 'O' in letter:
#             vowelsCount += 1
#         elif 'U' in letter:
#             vowelsCount += 1
        
#     return vowelsCount

# word = 'I am a man and Iam from Nepal Thank You'

# print(vowelsCounter(word))


# def vowelsCounter(vowels):
#     vowelsCounter = 0

#     for letter in vowels:
#         if letter in 'aeiouAEIOU':
#             vowelsCounter += 1
        
#     return vowelsCounter

# word = 'hello world'

# print(vowelsCounter(word))

# def listReverser(manual):
#     reversedList = []

#     for i in range(len(manual)-1,-1,-1):
#         reversedList.append(manual[i])

#     return reversedList

# spam = [1,2,3,4,5]

# print(listReverser(spam))
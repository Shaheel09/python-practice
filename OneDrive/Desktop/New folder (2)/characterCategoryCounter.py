sentence = 'Hello world. This is python code 123 ***'

def charCatCounter(stuff):

    specialChar = r"!@#$%^&*()_+=-`~[]\{}|;':\",./<>?"
    count = {}

    for i in stuff:
        if i in 'aeiouAEIOU':
            count.setdefault('Vowels', 0)
            count['Vowels'] += 1
        elif i in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            count.setdefault('Consonants', 0)
            count['Consonants'] += 1
        elif i in specialChar:
            count.setdefault('Special', 0)
            count['Special'] += 1
        elif i == ' ':
            count.setdefault('Spaces', 0)
            count ['Spaces'] += 1
        elif i.isdigit():
            count.setdefault('Digits', 0)
            count['Digits'] += 1
        else:
            count.setdefault('Others', 0)
            count['Others'] += 1
    
    return count

print(charCatCounter(sentence))
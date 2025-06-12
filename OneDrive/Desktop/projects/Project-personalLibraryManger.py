books = [
    {'title': '1984', 'author': 'George Orwell', 'year': '1949', 'genre': 'Dystopian'},
    {'title': 'Dune', 'author': 'Frank Herbert', 'year': '1965', 'genre': 'Sci-Fi'}
]

print('''
[1] Add Book
[2] View All Books
[3] Search by Title 
[4] Delete Book
[5] Print Table View
[6] Exit
          ''')
    
# for i in books:

def libraryManager(datas):
    userChoose = int(input('Choose from the options: '))
    
    if userChoose == 1:
        addTitle = input('Add Title of Book: ')
        addAuthor = input('Add author of Book: ')
        addYear = input('Add Year of Book: ')
        addGenre = input('Add Genre of Book: ')
    
        books1 = {
            'title': addTitle,
            'author': addAuthor,
            'year': addYear,
            'genre' : addGenre
        }
        print('Book added Successfully: ')
        books.append(books1)
        print(datas)
    
    elif userChoose == 2:
        while True:
            print('Library Menu:')
            print('[1] View All Books')
            print('[2] Exit')

            choice = int(input('Enter your choice here: '))

            if choice == 1:
                print('BOOK 1')
                print(datas[0])
                print('BOOK 2')
                print(datas[1])
                break
            elif choice == 2:
                print('Good Bye')
                break
            else: 
                print('Invalid Option. Please Try again!!!')
    
    elif userChoose == 3:
        inputTitle = input('Enter a title name: ')
        if inputTitle == '1984':
            print(books[0])
        elif inputTitle == 'Dune':
            print(books[1])

    elif userChoose == 4:
        userInput = int(input('Please Select the book You wanna delete. \nFor \'BOOK 1\' Type 1.  \nFor \'BOOK2\' Type 2.: '))
        if userInput == 1:
            datas.pop(0)
            print('You have successfully removed Book 1')
            print('Book 2 left')
            print(datas)
        elif userInput == 2:
            datas.pop(1)
            print('You have successfully removed Book 2')
            print('Book 1 left')
            print(datas)
        else:
            print('Invalid Option. Please Try again!!')
        
    elif userChoose == 5:
        headers = ['Title', 'Author', 'Year', 'Genre']
        rows = [[value for value in d.values()] for d in datas]

        print('|',headers[0].center(10),'|',headers[1].center(10),'|',headers[2].center(10),'|',headers[3].center(10),'|')
        print('|',''.center(10,'-'),'|',''.center(10,'-'),'|',''.center(10,'-'),'|',''.center(10,'-'),'|')
        print('|',rows[0][0].center(10),'|',rows[0][1].center(10),'|',rows[0][2].center(10),'|',rows[0][3].center(10),'|')
        print('|',rows[1][0].center(10),'|',rows[1][1].center(10),'|',rows[1][2].center(10),'|',rows[1][3].center(10),'|')

    elif userChoose == 6:
        print('Exited')

libraryManager(books)
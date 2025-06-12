
manageGroceryItems = [{'Name':'Milk','Category': 'Drinks','Quantity':5,'Price':50,'Total': 5 * 50},
                      {'Name':'Hersys','Category': 'Chocolate','Quantity':10,'Price':20,'Total': 10 * 20}]


print('''
[1] Add a New Item
[2] View all Items
[3] Search items by category
[4] Update quantity of an item
[5] Print a table view
[6] Exit

''')
def addNewItem(items):
        itemName = input('Enter a Grocery Name: ')
        itemCategory = input('Enter a Grocery Category: ')
        itemQuantity = float(input('Enter a Grocery Quantity: '))
        itemPrice = float(input('Enter a Grocery Price: '))
       
        items.append({'Name': itemName, 'Category': itemCategory, 'Quantity': itemQuantity, 'Price': itemPrice, 'Total': itemQuantity * itemPrice})
        print('Items added sucessfully', {itemName})

def viewAllItems(adding):
    print('All items')
    print(adding)

def searchItemsByCategory(category):
    userEnter = input('Enter a category name: ')

    if userEnter not in category:
         print('This category is not in Grocery')
    elif userEnter in category:
         print(category)
    else:
         print('Invaid options')

def updateItem(update):
     userEnter = (input('Enter to an item Name to change the quantity of an Item: '))         

     found = False
     for item in update:
          if item['Name'] == userEnter:
               found = True
     
     change = float(input('Enter amount to add/remove (Use negative number to subtract): '))
     item['Quantity'] += change
     item['Total'] = item['Quantity'] * item['Price']

def tableView(view):
     if not view:
          print('No Groceries to display!')
          return
     
     headers = ['Name', 'Category', 'Quantity', 'Price','Total']
     rows = [[value for value in d.values()] for d in view]

     print('|',headers[0].center(10),'|',headers[1].center(10),'|',headers[2].center(10),'|',headers[3].center(10),'|',headers[4].center(10),'|')
     print('|',''.center(10,'-'),'|',''.center(10,'-'),'|',''.center(10,'-'),'|',''.center(10,'-'),'|',''.center(10,'-'),'|')
     print('|',rows[0][0].center(10),'|',rows[0][1].center(10),'|',str(rows[0][2]).center(10),'|',str(rows[0][3]).center(10),'|',str(rows[0][4]).center(10),'|')
     print('|',rows[1][0].center(10),'|',rows[1][1].center(10),'|',str(rows[1][2]).center(10),'|',str(rows[1][3]).center(10),'|',str(rows[1][4]).center(10),'|')



def exit():
     print('Exited')

def chooseItem():
    
     userInput = int(input('Choose a option: '))
     
     if userInput == 1:
         addNewItem(manageGroceryItems)
     elif userInput == 2:
         viewAllItems(manageGroceryItems)
     elif userInput == 3:
         searchItemsByCategory(manageGroceryItems)
     elif userInput == 4:
         updateItem(manageGroceryItems)
     elif userInput == 5:
          tableView(manageGroceryItems)
     elif userInput == 6:
          exit()
     else: 
          print("Invalid Option Try again....")


chooseItem()

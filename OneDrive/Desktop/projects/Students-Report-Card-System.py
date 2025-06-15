import numpy as np 

students = [{
    'name': 'Alice',
    'class': '10A',
    'score': {'Math': 95, 'Science': 88, 'English': 76}
},
{
    'name': 'Bob',
    'class': '10B',
    'score': {'Math': 89, 'Science': 92, 'English': 81}

},
{
    'name' : 'Manu',
    'class' : '8A',
    'score': {'Math': 78, 'Science': 82, 'English': 92}
}
]

print('FEATURES')
print('''
[1] Add Student
[2] View All Student
[3] Search Student
[4] Update Score
[5] Class Averages
[6] Top Scorers   
[7] Exit
    ''')

def addStudent(newStudent):
    studentName = input('Enter a name: ')
    studentClass = input('Enter a class: ')
    mathScore = int(input('Enter a Math score: '))
    scienceScore = int(input('Enter a Science score: '))
    englishScore = int(input('Enter a English score: '))

    studentsCard = {
        'name' : studentName,
        'class' : studentClass,
        'score' : {'Math': mathScore, 'Science': scienceScore, 'English': englishScore} 
    }
    newStudent.append(studentsCard)
    print(newStudent)

def viewStudent(view):
    print('Students List')
    for i in view:
        for value in i.values():
            print(value,'\n' ,end='')

def searchStudent(search):
    userEnter = input('Enter a name to search: ').strip().capitalize()
    found = False

    for i in search:
        if userEnter in i['name']:
            print(i)
            found = True
    if not found:
        print('No student found')

def updateStudentScore(update):
    userEnter = input('Enter a name to choose a student and update score: ').strip().capitalize()
    found = False

    for i in update:
        if userEnter in i['name']:
            print(i)
            print('Which Subjects do you wanna update \'Math\', \'Science\' or \'English\' ')
            userInput = input('Choose: ').strip().capitalize()

            if userInput in i['score']:
                if userInput == 'Math':
                    mathInput = int(input('Update: '))
                    i['score'].update({'Math': mathInput}) 
                    print(i, ' Updated')

                elif userInput == 'Science':        
                    scienceInput = int(input('Update: '))
                    i['score'].update({'Science': scienceInput})
                    print(i,' Updated')
                
                elif userInput == 'English':
                    englishInput = int(input('Update: '))
                    i['score'].update({'English': englishInput})
                    print(i,' Updated')
            
            else:
                print('Please enter a valid subject')

            found = True
    
    if not found:
        print('Student not found!!')
  
def printClassAverage(average):
    # userInput = input('Choose a subject to see average: ').strip().capitalize()

    total_scores = {'Math': 0, 'Science': 0, 'English': 0}
    count = {'Math':0, 'Science':0, 'English':0}
    
    for student in average:
        for subject,score in student['score'].items():
            total_scores[subject] += score
            count[subject] += 1
    
    for subject in total_scores:
        average = total_scores[subject] / count[subject]
        print(f'{subject} average: {average:.2f}')

def showTopScorer(scorer):
    topScore = {
        'Math': {'score': 0, 'student': []},
        'Science': {'score': 0, 'student': []},
        'English': {'score': 0, 'student': []}    
    }
    for i in scorer:
        for subject,score in i['score'].items():
            if score > topScore[subject]['score']:
                topScore[subject]['score'] = score
                topScore[subject]['students'] = [i['name']]
            elif score == topScore[subject]['score']:
                topScore[subject]['students'].append(i['name'])
    
    for subject,data in topScore.items():
        print(f'Top scorer(s) in {subject} with {data['score']}: {', '.join(data['students'])}')

def exitMenu():
    print('Exited')

def chooseOption():
    userEnter = int(input('Choose an option: '))

    if userEnter == 1:
        addStudent(students)
    elif userEnter == 2:
        viewStudent(students)
    elif userEnter == 3:
        searchStudent(students)
    elif userEnter == 4:
        updateStudentScore(students)
    elif userEnter == 5: 
        printClassAverage(students)
    elif userEnter == 6:
        showTopScorer(students)
    elif userEnter == 7: 
        exitMenu()
    else: 
        print('Invalid option please choose input a Number between 1-7')
    
    return userEnter

while True:
    choice = chooseOption()
    if choice == 7:
        break
def passStrenthChecker(basic):

    specialCharacter = r"!@#$%^&*()_+=-`~[]\{}|;':\",./<>?"
    score = 0
    
    if len(basic) >= 8 :
        # return 'Your password should be at least 8 characters'
        score += 1
    if any(char.isdigit() for char in basic):
        # return 'Your password should atleast contain 1 number'
        score += 1
    if any(char.isupper() for char in basic):
        # return 'Your password should at least contain 1 Upper case letter'
        score += 1
    if any(char.islower() for char in basic):
        # return 'Your password should at least contain 1 Lowers case letter'
        score += 1
    if any(char in specialCharacter for char in basic):
        # return 'Your password should at least contain 1 special character'
        score +=1

    if score <= 2:
        return f'weak password (score: {score}/5)'
    elif score <= 4:
        return f'medium password (score: {score}/5)'
    else:
        return f'string password (score: {score}/5)'
    

password = 'HElloWOrld152@#'

print(passStrenthChecker(password))
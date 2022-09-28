listOfScores = []
score = 'not done'
totalScore = 0
countOfScores = 0

while score != 'done':
    score = input('\nWhat is the score you would like to add to the list to get the average and highest score?\nType [Done] to finish entering scores.\n').lower()
    print(f'\nThank you, {score} has been registered.')

    if score != 'done':
        if isinstance(float(score), float) == True:
            listOfScores.append(score)
            countOfScores += 1
        else:
            print('\nPlease enter a number.')
            
for i in listOfScores:
    totalScore += float(i)
    
print(f'\nThe average score is {totalScore/countOfScores}, with {countOfScores} scores entered.')
print(f'\nThe top score is {max(listOfScores)}')

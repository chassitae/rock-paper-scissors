import random

def main():
    
    computerchoice = 'nothing'
    
    print('This is the rock paper, scissors game! Let\'s play!')

    user = input('Enter your choice of rock, paper, or scissors: ')
    print('')

    while user != 'rock' and user != 'paper' and user != 'scissors' :
        print(user)
        user = input('Choice is not valid. Enter a choice of rock, paper, or scissors: ')

    comp = random.randint(1, 3)
    if comp == 1 :
        computerchoice = 'rock'
    elif comp == 2 :
        computerchoice = 'paper'
    elif comp == 3 :
        computerchoice = 'scissors'
    else:
        print('Error')
        


    if user == computerchoice:
        print('DRAW!')
        print('')
    elif user == 'rock' :
            if computerchoice == 'paper' :
                print('COMPUTER WINS!')
                print('')
            else:
                print('YOU WIN!')
                print('')
    elif user == 'paper' :
            if computerchoice == 'scissors' :
                print('COMPUTER WINS!')
                print('')
            else:
                print('YOU WIN')
                print('')
    elif user == 'scissors' :
            if computerchoice == 'rock' :
                print('COMPUTER WINS!')
                print('')
            else:
                print('YOU WIN!')
                print('')

    print('Your choice was: ' + str(user) + ' \nComputer choice was: ' + str(computerchoice) + '\nThanks for playing!')
    input('Enter any key to exit ')

main()

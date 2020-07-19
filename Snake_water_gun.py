import random

list1 = ['snake', 'water', 'gun']

user = 0
comp = 0
print('Enter number of attempts: ')
n = int(input())
while n > 0:
    r = random.choice(list1)
    print("Enter your input: ")

    user_input = input()

    if user_input == r:
        print('Match tied')
        user = user + 1

    elif user_input == 'water' and r == 'snake':
        print('Computer won')
        comp = comp + 1

    elif user_input == 'gun' and r == 'water':
        print('Computer won')
        comp = comp + 1

    elif user_input == 'snake' and r == 'water':
        print('You Won')

    elif user_input == 'snake' and r == 'gun':
        print('computer won')
        comp = comp + 1

    elif user_input == 'water' and r == 'gun':
        print('You won')
        user = user + 1

    elif user_input == 'gun' and r == 'snake':
        print('You Won')
        user = user + 1

    n = n-1

if user > comp:
    print('Congratulations You Won!!')

else:
    print('Sorry You Lost, better luck next time!')

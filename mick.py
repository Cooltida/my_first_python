import sys
import random
import emoji

choices = ['rock' , 'paper', 'scissors']
player_choice = False
if len(sys.argv) > 1:
    player_choice = sys.argv[1]
if len(sys.argv) != 2 or player_choice not in choices:
    c_str = ""
    for c in choices:
        c_str = c_str + c + " "
    print("you must pick between " + c_str)
    exit(1)


c_choice = choices[round(random.random() * 2)]

print(player_choice)
print(c_choice)

if player_choice == c_choice:
    print('draw')

elif player_choice == choices[0] and c_choice == choices[2]:
    print('won')

elif player_choice == choices[1] and c_choice == choices[0]:
    print('won')

elif player_choice == choices[2] and c_choice == choices[1]:
    print('won')

else:
    print('lost')


# Testing random distribution
# tot = 0
# for i in range(0, 1000000):
#     r = round(random.random() * 2)
#     print(r)
#     tot = tot + r
# print(tot / 1000000)

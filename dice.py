import random
import logging

logging.basicConfig(level=logging.DEBUG)
# rounds to the closes integer
round(
    # returns number between  0.0 and 1.0
    random.random() * 5
)


def dice(sides=6):
    logging.debug("A {} sided dice has been selected".format(sides))
    result = round((random.random() * (sides - 1) + 1))
    logging.debug("The dice show with a {}".format(result))
    return result


def hand(number_of_dice=1, sides=6):
    total = 0
    for i in range(0, number_of_dice):
        current_dice = dice()
        if current_dice == sides:
            total = total + hand(number_of_dice=2, sides=sides)
        else:
            total = total + current_dice
    return total


print("Your total is {}".format(hand(number_of_dice=5, sides=6)))

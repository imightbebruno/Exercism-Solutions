"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    return [number, number + 1, number +2]
    
def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand)/len(hand)

def approx_average_is_average(hand):
    first_and_last = (hand[0] + hand[-1])
    average_of_first_and_last = first_and_last/2
    middle_card = hand[len(hand)//2]
    return average_of_first_and_last == card_average(hand) or middle_card == card_average(hand)

def average_even_is_average_odd(hand):
    return card_average(hand[::2]) == card_average(hand[1::2])

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if (last := hand[-1]) == 11: hand[-1] = last*2
    return hand

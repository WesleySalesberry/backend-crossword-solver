#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""
from difflib import get_close_matches
__author__ = "Wesley Salesberry"

# YOUR HELPER FUNCTION GOES HERE

# Get the input and make sure it is not a number and only a string


def get_input():

    while True:
        try:
            test_word = input(
                'Please enter a word to solve.\nUse * to signify unknown letters: ').lower().strip()
            if test_word.isdigit():
                print(str(test_word) + " is not letters..")
                continue

            break

        except ValueError:
            print("Sorry, I didn't understand that.")

        return test_word

# remove the asterisks from the word


def cleanup_word(word):
    striped = word.replace('*', '')
    return striped

# Grab the users input and the dictionary.txt words to find the closest matches


def find_closest_matches(user, word):
    #user_input = get_input()
    #cleaned_word = cleanup_word(user_input)
    print(get_close_matches(user, word, 50, 0.7))

    return get_close_matches(user, word, 50, 0.7)


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = input(
        'Please enter a word to solve.\nUse * to signify unknown letters: ').lower()

    striped = test_word.replace('*', '')

    print("Word is: " + striped)

    print(get_close_matches(striped, words, 50, 0.7))

    return get_close_matches(striped, words, 50, 0.7)
    # if done == alphabetize(element):
    #     print(element)
    #     my_list.append(element)

    # show_list = ''.join(my_list)
    # print(show_list)
    # return show_list

    # YOUR ADDITIONAL CODE HERE
    raise NotImplementedError('Please complete this')


if __name__ == '__main__':
    main()

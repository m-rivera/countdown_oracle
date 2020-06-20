#!/usr/bin/env python
"""
Command line utility to win at Countdown letters.

"""
import sys
import argparse
import countdown_oracle.src.explore as ex

def main(in_args):
    letter_str = in_args.letter_str
    out_words = ex.permut_words(letter_str)
    for word in out_words:
        print(word)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Print out all of the\
            English words that can be made by picking letters out of the\
            input.")
    parser.add_argument("letter_str", help="The input letters.")

    user_input = sys.argv[1:]
    args = parser.parse_args(user_input)

    main(args)

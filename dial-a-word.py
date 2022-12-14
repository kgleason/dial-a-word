import argparse
import string
import requests

letters = {
    '1': ['1'], 
    '2': ['A', 'B', 'C'], 
    '3': ['D', 'E', 'F'], 
    '4': ['G', 'H', 'I'], 
    '5': ['J', 'K', 'L'], 
    '6': ['M', 'N', 'O'], 
    '7': ['P', 'Q', 'R', 'S'], 
    '8': ['T', 'U', 'V'], 
    '9': ['W', 'X', 'Y', 'Z'], 
    '0': ['0']
    }


def letters_to_digits() -> dict:
    """ Return a dict of mapping letters to phone digits 
    :return: dict of digits mapped to letters
    """
    d = {}
    for k,v in letters.items():
        for letter in v:
            d[letter] = k
    return d


def get_words_from_file(fname:str) -> list:
    """ Load a word file, return a list of words in the file 
    :param fname: Filename to get word list from
    :return: List of words
    """
    with open(fname, 'r') as f:
        wl = f.read().replace("\n", " ").split()
    return wl


def word_to_digits(word:str, dm:dict) -> str:
    """ Use the provided dict to convert a word to digits.
    :param word: A word to turn into a string of digits
    :param dm: A dict of digits mapped to letters
    :return: A string of digits
    """
    v = ""
    for letter in word:
        v += dm[letter]
    return v


def swap_digits_for_word(num:str, word:str, d:dict) -> str:
    """ Return a string that has replaced the relevant digits with letters 
    :param num: a Phone Number
    :param word: a word to put into the phone number
    :param d: a dict of letters mapped to digits
    :return: a string of digits and letters that represent a phone number with a word
    """
    digit_string = ""
    for ltr in word:
        digit_string += d[ltr.upper()]
    
    return num.replace(digit_string, word.upper())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--min', help='Minimum number of characters for the potential word', type=int)
    parser.add_argument('-x', '--max', help='The maximum number of characters for the potential word', type=int)
    parser.add_argument('-n', '--num', help='A comma separated list of numbers to test', required=True)
    parser.add_argument('-f', '--files', help='A comma separated list of filles to use as the word list')
    parser.add_argument('-u', '--url', help='A URL whence to fetch a word list. Assumes raw text, as in GitHub raw urls')

    args = parser.parse_args()

    if not args.files and not args.url:
        raise ValueError("Either the files or the URL parameter is required")

    numbers = args.num.split(',')
    min_chars = args.min if args.min else 3
    max_chars = args.max if args.max else 7

    digit_map = letters_to_digits()
    lexicon = []

    if args.files:
        lexicon += get_words_from_file(file for file in args.files.split(','))

    if args.url:
        resp = requests.get(args.url)
        lexicon += resp.text.replace("\n", " ").split()

    for number in numbers:        
        for word in lexicon:
            if min_chars < len(word) < max_chars + 1:
                worddigits = word_to_digits(word.upper(), digit_map)
                if str(worddigits) in number:
                    print(f"{number}, {word.upper()}, {swap_digits_for_word(number, word, digit_map)}")
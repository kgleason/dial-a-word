import argparse
import sys

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

def letters_to_digits():
    d = {}
    for k,v in letters.items():
        for letter in v:
            d[letter] = k
    return d

def get_words(fname):
    with open(fname, 'r') as f:
        wl = f.read().replace("\n", " ").split()
    return wl

def word_to_digits(word, dm):
    v = ""
    for letter in word:
        v += dm[letter]
    return v

def swap_digits_for_word(num, word, d):
    digit_string = ""
    for ltr in word:
        digit_string += d[ltr.upper()]
    
    return num.replace(digit_string, word.upper())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--min', help='Minimum number of characters for the potential word', type=int)
    parser.add_argument('-x', '--max', help='The maximum number of characters for the potential word', type=int)
    parser.add_argument('-n', '--num', help='The number to test', required=True)

    args = parser.parse_args()

    number = args.num
    min_chars = args.min if args.min else 3
    max_chars = args.max if args.max else 7

    digit_map = letters_to_digits()
    lexicon = get_words('short-words.txt')
    lexicon += get_words('medium-words.txt')

    for word in lexicon:
        if min_chars < len(word) < max_chars + 1:
            worddigits = word_to_digits(word.upper(), digit_map)
            if str(worddigits) in number:
                print(f"{word.upper()}: {swap_digits_for_word(number, word, digit_map)}")
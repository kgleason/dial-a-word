from itertools import combinations_with_replacement
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
    if not sys.argv[1]:
        raise IndexError("Need a parameter.")
    
    number = sys.argv[1]

    digit_map = letters_to_digits()
    lexicon = get_words('short-words.txt')
    lexicon += get_words('medium-words.txt')

    for word in lexicon:
        if 3 < len(word) < 8:
            worddigits = word_to_digits(word.upper(), digit_map)
            if str(worddigits) in number:
                print(f"{word.upper()}: {swap_digits_for_word(number, word, digit_map)}")
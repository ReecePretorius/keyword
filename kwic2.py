#!/usr/bin/env python3

import sys
import string

def get_data():
    read_lines = [line.strip() for line in sys.stdin.readlines()]
    data = [l.split(',') for l in ','.join(read_lines).split('::')]
    return(data)

def get_keywords(phrases, exclude):
    keywords = []
    for i in range(len(phrases)):
        phrase = phrases[i].split(',')
        words = phrase[0].split(' ')
        
        for j in range(len(exclude)):
            if (exclude[j] in words):
                words[:] = [x for x in words if x != exclude[j]]
        keywords.extend(words)

    return(keywords)

def sort_phrases(keywords, phrases):
    for i in range(len(keywords)):
        key = keywords[i]
        for j in range(len(phrases)):
            phrase = phrases[j]
            if(key in phrase):
                words = phrases[j].split()
                ind = words.index(keywords[i])
                words[ind] = words[ind].upper()
                
                left_words = words[0:ind]
                left_string = ' '.join(left_words)
                right_words = words[ind + 1:]
                right_string = ' '.join(right_words).strip()
                if(not right_string):
                    print('{:>29} {:<}'.format(left_string, words[ind]))
                else:
                    print('{:>29} {:} {:<}'.format(left_string, words[ind], right_string))

def main():
    data = get_data()
    
    exclude = data[1]
    exclude.remove('')
    
    phrases = data[2]
    phrases.remove('')

    keywords = get_keywords(phrases, exclude)
    keywords_sorted = sorted(set(keywords), key = lambda x:keywords.index(x))
    keywords_sorted.sort()

    sort_phrases(keywords_sorted, phrases)

if __name__ == '__main__':
    main()

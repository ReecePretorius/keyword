#!/usr/bin/env python3

import sys
import string

def get_data():
    _read = [line.strip() for line in sys.stdin.readlines()]
    data = [l.split(',') for l in ','.join(_read).split('::')]
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
                temp = phrases[j].split()
                ind = temp.index(keywords[i])
                temp[ind] = temp[ind].upper()
                
                temp2 = temp[0:ind]
                temp3 = ' '.join(temp2)
                temp4 = temp[ind + 1:]
                temp5 = ' '.join(temp4).strip()
                if(not temp5):
                    print('{:>29} {:<}'.format(temp3, temp[ind]))
                else:
                    print('{:>29} {:} {:<}'.format(temp3, temp[ind], temp5))

def main():
    data = get_data()
    exclude = data[1]
    exclude.remove('')
    phrases = data[2]
    phrases.remove('')

    keywords = get_keywords(phrases, exclude)
    keywords_ = sorted(set(keywords), key = lambda x:keywords.index(x))
    keywords_.sort()

    sort_phrases(keywords_, phrases)

if __name__ == '__main__':
    main()

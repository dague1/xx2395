#!/usr/bin/env python3

def filter_text(text):
    #init rules list!
    rList = {}
    #split text into word array
    wordArr = text.split("\n")

    #fill rules list
    for word in wordArr:
          if word.startswith("#"):
            (keys, values) = map(str.strip, word[1:].split("="))
            rList[keys] = values
            continue

    #check rules
    for key in rList.keys():
        for value in rList.values() :
            if key in value:
                return False    

    return True
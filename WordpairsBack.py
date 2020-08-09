
import random
import re

def create_list() :
    f_words = []
    with open("Words.txt") as file : 
        content = file.readlines()
    f_words = []
    for words in content :
        f_words.append(str.rstrip(words))
    random.shuffle(f_words)
    sf_words = list(zip(f_words[:50], f_words[50:]))
    sff_words = [] 
    for tuple in sf_words :
        sff_words.append((tuple[0], '-----', tuple[1]))
    return sff_words

def add_to_highscore(name, level) :
    with open("Highscore.txt", 'a+' ) as file : 
        file.write(f"Name : {name}, Score reached : {level} \n")


def check_highscore():
    with open("Highscore.txt", 'r') as file :
        content = file.readlines()
    highscores = [str.rstrip(words) for words in content]
    integer = []
    string = []

    for highscore in highscores:
        integer1 = []
        string1 = []
        for x in highscore : 
            try :
                int(x)
                integer1.append(x)
            except : 
                string1.append(x)
        integer.append(integer1)
        string.append(string1)

    integer2= ["".join(x) for x in integer]
    string2 = ["".join(x) for x in string]

    f_list = [(x, y) for x, y in zip(string2, integer2)]

    f_list.sort( key = lambda x : int(x[1]))
    f_list.reverse()

    return f_list






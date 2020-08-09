from tkinter import *
import WordpairsBack
from time import time
import random

class Game :

    def __init__(self, name, level, list):
        self.name = name
        self.level = level
        self.list = list
    
    def intro(self) :
        welcome_statement = str(f"Welcome {self.name}, you are on level {self.level}, with each level you will be shown an increasing number of word pairs for a period of time. You must enter all the corresponding word pairs to move on to the next level. Press hide and begin when you have remembered the wordpairs in the left box")
        format_dialogue(welcome_statement)
    
    def intro_new_level(self) :
        intro_statement = str(f"Well done {self.name}! You completed level {self.level}! You are now on level {(self.level + 1)}. Some words have been added to your list, press hide and begin when you are ready.")
        format_dialogue(intro_statement)
    
    def level_up(self) :
        self.level += 1
        b_hide.configure(state = NORMAL)
        b_check.configure(state = DISABLED)
        return self.level

    def game_over(self) :
        game_over_statement = str(f"That was not the correct pair, you've failed. The correct pairing was {this_level.current_pair[0]} and {this_level.current_pair[2]}. However you reached level {self.level} and your score has been added to the Highscore board.")
        format_dialogue(game_over_statement)
        WordpairsBack.add_to_highscore(self.name, self.level)
        b_hide.configure(state = DISABLED)
        b_check.configure(state= DISABLED)



class Level :

    def __init__(self, level, c_answers, t_answers, pairs, current_pair = ""):
        self.level = level
        self.c_answers = c_answers
        self.t_answers = t_answers
        self.pairs = pairs
        self.current_pair = current_pair

    def get_question(self) :
        try : 
            this_pair = random.choice(self.pairs)
            self.pairs.remove(this_pair)
            self.current_pair = this_pair
        except IndexError :
            print("level complete")
    
    def correct_answer(self) :
        self.c_answers += 1
        
        
    def correct_answer_statement(self):
        format_dialogue(f"That answer was correct! You are {self.c_answers}/{self.t_answers} of the way through this level")


    

        
def format_dialogue(string) : 
    list_dialogue.delete(0, END)
    split_string = string.split()
    max = len(split_string)
    a = 0
    b = 8
    f_dialogue = []
    while b <= max :
        f_dialogue.append(split_string[a : b])
        a +=8
        b +=8
    else: 
        f_dialogue.append(split_string[(a) : ])
    ff_dialogue = []
    for rows in f_dialogue :
        ff_dialogue.append(" ".join(rows))
    for rows in ff_dialogue :
        list_dialogue.insert(END, rows)
    return (ff_dialogue)
    



def start_game () : 
    if not name_entry.get() :
        format_dialogue("You need to enter a username to begin")
    
    else :
        wordpairs_list = WordpairsBack.create_list() 
        name = name_entry.get()                                 #Set's Game
        level = 1
        list =  (wordpairs_list)
        global user
        user = Game(name, level, list)
        user.intro()

        list_wordpairs.delete(0, END)                           #Creates and prints list
        for wordpairs in wordpairs_list[0:user.level] :
            list_wordpairs.insert(END, wordpairs)
        disable_sandh()
        b_hide.configure(state = NORMAL)


        
def ent_control(event) :
    state_c = str(b_check['state'])
    state_s = str(b_start['state'])
    state_h = str(b_hide['state'])
    if state_c == 'normal' :
        check_entry()
    elif state_s == 'normal' :
        start_game()
    elif state_h == 'normal' :
        begin_level()
    else :
        pass




def check_entry() :
    global this_level
    list_dialogue.delete(0, END)
    if not list_wordpairs.get(0, END) :
        answer = pf_answer.get()
        if answer == this_level.current_pair[2] :     #this needs to be taken from list not this pair os function is cyclable
            this_level.correct_answer()
            list_given_word.delete(0, END)
            e_answer.delete(0, END)
            if this_level.c_answers < this_level.t_answers :
                this_level.correct_answer_statement()
                this_level.get_question()
                list_given_word.insert(END, this_level.current_pair[0])
            else :
                user.intro_new_level()
                user.level_up()
                list_wordpairs.delete(0, END)                           #Creates and prints list
                for word_pairs in user.list[0 : user.level] :
                    list_wordpairs.insert(END, word_pairs)
        else : 
            user.game_over()
            enable_sandh()
    else : 
        format_dialogue("You need to press hide and begin before you can enter the pair. No cheating")
        pass



def begin_level():
    list_given_word.delete(0, END)
    list_wordpairs.delete(0, END)
    global this_level
    this_level = Level(user.level, 0, user.level, user.list[0:user.level])
    this_level.get_question()
    list_given_word.insert(END, this_level.current_pair[0])
    b_check.configure(state = NORMAL)
    b_hide.configure(state = DISABLED)



def check_highscore():
    highscores = WordpairsBack.check_highscore()
    list_wordpairs.delete(0, END)
    for scores in highscores :
        list_wordpairs.insert(END, scores)


def disable_sandh() :
    b_start.configure(state = DISABLED)
    b_highscore.configure(state = DISABLED)

def enable_sandh() :
    b_start.configure(state = NORMAL)
    b_highscore.configure(state = NORMAL)
        
window = Tk()

window.wm_title("WordPairs")



b_start = Button(window, text = "Start", width = 12, command = start_game)
b_start.grid(row = 1, column = 2)
b_start.configure(state = NORMAL)

b_highscore = Button(window, text = "Highscores", width = 12, command = check_highscore)
b_highscore.grid(row = 1, column = 1)
b_highscore.configure(state = NORMAL)

b_check = Button(window, text = "Check Entry", width = 40, command = check_entry)
b_check.grid(row = 5 , column = 1, columnspan = 2)
b_check.configure(state= DISABLED)

b_hide = Button(window, text = "Hide and Begin", width = 40, command = begin_level)
b_hide.grid(row = 7, column = 0, padx = 15, pady= 20)
b_hide.configure(state = DISABLED)

l_name = Label(window, text = "Enter your name: ")
l_name.grid( row = 0, column = 1)

l_word = Label(window, text = "Given word")
l_word.grid(row = 3, column = 1)

l_entry = Label(window, text = "Enter pair")
l_entry.grid(row = 3, column = 2)

list_dialogue = Listbox(window, height = 7, width = 40)
list_dialogue.grid(row = 2, column = 1, rowspan = 1, columnspan = 2, padx= 15)

list_wordpairs = Listbox(window, height = 20, width = 40)
list_wordpairs.grid(row = 0, column  = 0, rowspan = 6, pady = 15, padx =15, ipady = 15, ipadx = 15)

list_given_word = Listbox(window, height = 1, width = 20)
list_given_word.grid(row = 4, column = 1)


name_entry = StringVar()
e_name = Entry(window, textvariable = name_entry)
e_name.grid(row = 0, column = 2)


pf_answer = StringVar()
e_answer = Entry(window, textvariable = pf_answer)
e_answer.grid(row = 4, column = 2)

window.bind('<Return>', ent_control)



window.mainloop()



import tkinter as tk
import random



background_1 = "white"
background_2 = "#bbbbbb"
background_3 = "green"
background_4 = "yellow"

foreground_1 = "black"
foreground_2 = "white"

guess_label_list_1 = []
guess_label_list_2 = []
guess_label_list_3 = []
guess_label_list_4 = []
guess_label_list_5 = []
parent_guess_label_list = []

#configure letter guess labels
def configure_labels():
    index = 0
    
    while index<5:
        a = 0
        while a<5:
            parent_guess_label_list[index][a].config(
                background = background_2,
                foreground = foreground_1,
                width = 2,
                height = 1,
                text = "_"
            )
            a += 1
    
        index += 1
   
    



#build list of words
word_bank = []
with open("word_list") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())

#pick random word from list
word_to_guess = random.choice(word_bank)


#define the variables
incorrect_letters = []
initial_focus = 0
max_turns = 5
turns_taken = 0
incorrect = "incorrect letters will go here"





#Function to clear the guess entry box
def entry_clear(e):
    guess_entry_box.delete(0, "end")

#functions to change the guess labels
def change_guess_label_1(guess):
    
    c = 0
    while c < 5:
        guess_label_list_1[c].config(text=guess[c])
        c += 1
    
    


def change_guess_label_2(guess):
    c = 0
    while c < 5:
        guess_label_list_2[c].config(text=guess[c])
        c += 1

def change_guess_label_3(guess):
    c = 0
    while c < 5:
        guess_label_list_3[c].config(text=guess[c])
        c += 1

def change_guess_label_4(guess):
    c = 0
    while c < 5:
        guess_label_list_4[c].config(text=guess[c])
        c += 1

def change_guess_label_5(guess):
    c = 0
    while c < 5:
        guess_label_list_5[c].config(text=guess[c])
        c += 1

#function to check answer
def check_answer():
    
    global max_turns
    global turns_taken
    global incorrect_letters_label
    
    # Get the player's guess
    guess = guess_entry_box.get().lower()
    
    
    
    # Check if the guess length equals 5 letters and is all alpha letters
    if len(guess) != len(word_to_guess) or not guess.isalpha():
        incorrect_letters_label.config(text="please input a 5 letter word")
    else:
        if turns_taken < max_turns:
            
            index = 0

            if turns_taken == 0:
                change_guess_label_1(guess)
                for c in guess:
                    if c == word_to_guess[index]:
                        parent_guess_label_list[turns_taken][index].config(
                            text = c,
                            bg = background_3
                        )
                    elif c in word_to_guess:
                        parent_guess_label_list[turns_taken][index].config(
                            text = c,
                            bg = background_4
                        )
                    else:
                        if c not in incorrect_letters:
                            incorrect_letters.append(c)
                    index +=1

            if turns_taken == 1:
                change_guess_label_2(guess)
                for c in guess:
                    if c == word_to_guess[index]:
                        parent_guess_label_list[turns_taken][index].config(
                            text = c,
                            bg = background_3
                        )
                    elif c in word_to_guess:
                        parent_guess_label_list[turns_taken][index].config(
                            text = c,
                            bg = background_4
                        )
                    else:
                        if c not in incorrect_letters:
                            incorrect_letters.append(c)
                    index +=1

            if turns_taken == 2:
                change_guess_label_3(guess)
                for c in guess:
                    if c == word_to_guess[index]:
                        parent_guess_label_list[turns_taken][index].config(
                            text = c,
                            bg = background_3
                        )
                    elif c in word_to_guess:
                        parent_guess_label_list[turns_taken][index].config(
                            text = c,
                            bg = background_4
                        )
                    else:
                        if c not in incorrect_letters:
                            incorrect_letters.append(c)
                    index +=1

            if turns_taken == 3:
                change_guess_label_4(guess)
                for c in guess:
                    if c == word_to_guess[index]:
                        parent_guess_label_list[turns_taken][index].config(
                            text = c,
                            bg = background_3
                        )
                    elif c in word_to_guess:
                        parent_guess_label_list[turns_taken][index].config(
                            text = c,
                            bg = background_4
                        )
                    else:
                        if c not in incorrect_letters:
                            incorrect_letters.append(c)
                    index +=1

            if turns_taken == 4:
                change_guess_label_5(guess)
                for c in guess:
                    if c == word_to_guess[index]:
                        parent_guess_label_list[turns_taken][index].config(
                            text = c,
                            bg = background_3
                        )
                    elif c in word_to_guess:
                        parent_guess_label_list[turns_taken][index].config(
                            text = c,
                            bg = background_4
                        )
                    else:
                        if c not in incorrect_letters:
                            incorrect_letters.append(c)
                    index +=1
        
        
        
        
        turns_taken += 1
    incorrect_letters_label.config(text = incorrect_letters)

    #check if the guess is immediately correct
    if guess == word_to_guess:
        incorrect_letters_label.config(text="Correct!")

    
    
    
    
    


    
   

    


#initialize tk window
root = tk.Tk()

root.config(background=background_1)


#topmost frame containing game title
frame_top = tk.Frame(root)


game_title = tk.Label(
    frame_top,
    text= "Word Hunter",
    bg=background_1,
    fg=foreground_1
)
game_title.pack()

#middle frame containing guesses and letter squares
frame_middle = tk.Frame(root)

#first guess frame
frame_guess_1 = tk.Frame(frame_middle)

#letter 1/1
guess_letter_1_1 = tk.Label(
    frame_guess_1
   
    
)
guess_letter_1_1.pack(side = "left")

#letter 1/2
guess_letter_1_2 = tk.Label(
    frame_guess_1
    
)
guess_letter_1_2.pack(side = "left")

#letter 1/3
guess_letter_1_3 = tk.Label(
    frame_guess_1
    
)
guess_letter_1_3.pack(side = "left")

#letter 1/4
guess_letter_1_4 = tk.Label(
    frame_guess_1
    
)
guess_letter_1_4.pack(side = "left")

#letter 1/5
guess_letter_1_5 = tk.Label(
    frame_guess_1
    
)
guess_letter_1_5.pack(side = "left")

frame_guess_1.pack()

#second guess frame
frame_guess_2 = tk.Frame(frame_middle)

#letter 2/1
guess_letter_2_1 = tk.Label(
    frame_guess_2
    
)
guess_letter_2_1.pack(side = "left")

#letter 2/2
guess_letter_2_2 = tk.Label(
    frame_guess_2
    
)
guess_letter_2_2.pack(side = "left")

#letter 2/3
guess_letter_2_3 = tk.Label(
    frame_guess_2
    
)
guess_letter_2_3.pack(side = "left")

#letter 2/4
guess_letter_2_4 = tk.Label(
    frame_guess_2
   
)
guess_letter_2_4.pack(side = "left")

#letter 2/5
guess_letter_2_5 = tk.Label(
    frame_guess_2
    
)
guess_letter_2_5.pack(side = "left")

frame_guess_2.pack()

#third guess frame
frame_guess_3 = tk.Frame(frame_middle)

#letter 3/1
guess_letter_3_1 = tk.Label(
    frame_guess_3
   
)
guess_letter_3_1.pack(side = "left")

#letter 3/2
guess_letter_3_2 = tk.Label(
    frame_guess_3
    
)
guess_letter_3_2.pack(side = "left")

#letter 3/3
guess_letter_3_3 = tk.Label(
    frame_guess_3
    
)
guess_letter_3_3.pack(side = "left")

#letter 3/4
guess_letter_3_4 = tk.Label(
    frame_guess_3
   
)
guess_letter_3_4.pack(side = "left")

#letter 3/5
guess_letter_3_5 = tk.Label(
    frame_guess_3
   
)
guess_letter_3_5.pack(side = "left")

frame_guess_3.pack()

#fourth guess frame
frame_guess_4 = tk.Frame(frame_middle)

#letter 4/1
guess_letter_4_1 = tk.Label(
    frame_guess_4
    
)
guess_letter_4_1.pack(side = "left")

#letter 4/2
guess_letter_4_2 = tk.Label(
    frame_guess_4
    
)
guess_letter_4_2.pack(side = "left")

#letter 4/3
guess_letter_4_3 = tk.Label(
    frame_guess_4
)
guess_letter_4_3.pack(side = "left")

#letter 4/4
guess_letter_4_4 = tk.Label(
    frame_guess_4
   
)
guess_letter_4_4.pack(side = "left")

#letter 4/5
guess_letter_4_5 = tk.Label(
    frame_guess_4
 
)
guess_letter_4_5.pack(side = "left")

frame_guess_4.pack()


frame_guess_5 = tk.Frame(frame_middle)

#letter 5/1
guess_letter_5_1 = tk.Label(
    frame_guess_5
   
)
guess_letter_5_1.pack(side = "left")

#letter 5/2
guess_letter_5_2 = tk.Label(
    frame_guess_5
    
)
guess_letter_5_2.pack(side = "left")

#letter 5/3
guess_letter_5_3 = tk.Label(
    frame_guess_5
    
)
guess_letter_5_3.pack(side = "left")

#letter 5/4
guess_letter_5_4 = tk.Label(
    frame_guess_5
   
)
guess_letter_5_4.pack(side = "left")

#letter 5/5
guess_letter_5_5 = tk.Label(
    frame_guess_5
  
)
guess_letter_5_5.pack(side = "left")

frame_guess_5.pack()

#bottom frame containing the guess entry box and guess button
frame_bottom = tk.Frame(
    root,
    bg=background_1
    
)

incorrect_letters_label = tk.Label(
    frame_bottom,
    text = incorrect,
    bg=background_1,
    fg=foreground_1
   
)
incorrect_letters_label.pack()

guess_entry_box = tk.Entry(
    frame_bottom,
    bg=background_1,
    fg=foreground_1
)
guess_entry_box.insert(0, "Type Guess Here")

guess_entry_box.pack()

guess_entry_box.bind("<FocusIn>", entry_clear)

check_guess_button = tk.Button(
    frame_bottom,
    text = "Check your word",
    command = check_answer,
    bg=background_1
)
check_guess_button.pack()

frame_top.pack()
frame_middle.pack()
frame_bottom.pack()

#lists of each label element for configuration
guess_label_list_1 = [guess_letter_1_1, guess_letter_1_2, guess_letter_1_3, guess_letter_1_4, guess_letter_1_5]
guess_label_list_2 = [guess_letter_2_1, guess_letter_2_2, guess_letter_2_3, guess_letter_2_4, guess_letter_2_5]
guess_label_list_3 = [guess_letter_3_1, guess_letter_3_2, guess_letter_3_3, guess_letter_3_4, guess_letter_3_5]
guess_label_list_4 = [guess_letter_4_1, guess_letter_4_2, guess_letter_4_3, guess_letter_4_4, guess_letter_4_5]
guess_label_list_5 = [guess_letter_5_1, guess_letter_5_2, guess_letter_5_3, guess_letter_5_4, guess_letter_5_5]

#main list of each label element list
parent_guess_label_list = [guess_label_list_1, guess_label_list_2, guess_label_list_3, guess_label_list_4, guess_label_list_5]


#configure each guess letter label element
configure_labels()
    
    


root.mainloop()
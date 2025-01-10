import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk() #create the main widget
root.title("Number Guessing Game") #set the title for the window
root.geometry("900x600") #set the default opening size
root.minsize(900,600) #set the minimum size so the user can't minimize more

root.configure(bg='#D9EAFD') #set the background color

mode_options = ["1 to 100!", "Pick your Range", "Impossible Mode", "Riddles","Mind Reading Computer"] #game modes
selected_mode = tk.StringVar() #global variable for the selected mode

difficulty_options = ["Easy", "Medium", "Hard"] #dificulties
difficulty_var = tk.StringVar() #global variable for selected difficulty

num_riddles_options = list(range(1, 8)) #empty list with 7 options so it can be set when the user chooses game mode
num_riddles_var = tk.StringVar() #global variable for riddles

# the list of riddles
easy_riddles=[("If you multiply me by any other number, the answer will always remain the same. Who am I?","0"),
              ("I am a 2-digit number, less than 8 + 8, more than 6 + 6 and I am even. What number am I?","14"),
              ("I am a 2-digit number, less iron 8 + 5, more than 7 + 3 and I am odd. What number am I?","11"),
              ("Start with 6 then add the number that comes after 2, subtract the number that comes before 5 and add 1. What number am I? ","6"),
              ("I am greater than 40, less than 50 and my ones digit is the number of sides on a triangle. What number am I? ","43"),
              ("I am an even number. My ones digit is the number of wheels on 3 bikes and I am between 50 and 60. What number am I?","56"),
              ("What becomes smaller when you turn it upside down?","9")
             ]

medium_riddles=[("I am greater than 80. I am even, less than 90 and my digits add up to 12. What number am I?","84"),
                ("I am between 30 and 50. The sum of my digits is 10. My ones digit is greater than my tens digit. I am not 37. What number am I?","46"),
                ("I am greater than 70. My ones digit is less than my tens digit. I am less than 90. I am not 76. What number am I?","87"),
                ("I am a 2-digit number. I am between 60 and 80. My tens digit is 2 more than my ones digit. I am not 64. What number am I?","75"),
                ("I am a 2-digit number, less than 9 + 9, more than 7 + 8. Add my digits together, and you get 8. What number am I? ","17"),
                ("I am an odd number. Take away a letter and I become even. What number am I?","7"),
                ("If there are three apples and you take away two, how many apples do you have?","2")
               ]
hard_riddles=[("You’re sitting down for breakfast and realize you have 4 bagels left. You know you’ll run out in four days so you cut them in half. How many bagels do you have now?","4"),
              ("A boy blows 18 bubbles, then pops 6, then pops another 7, and then he pops 5 and blows 1. How many are left?","1"),
              ("When Michael was 6 years old, his little sister, Laura, was half is age. If Michael is 40 years old today, how old is Laura?","37"),
              (" I am a three-digit number. My tens digit is six more than my ones digit. My hundreds digit is eight less than my tens digit. What number am I?","193"),
              ("A man is twice as old as his little sister, half as old as their dad. Over a period of 50 years, the age of the sister will become half of their dad’s age. What's the age of the man?","50"),
              ("I am a three-digit number. My second digit is 4 times bigger than the third digit. My first digit is 3 less than my second digit. Who am I?","141"),
              ("Three-digit number, the hundred’s digit is an even number between 5 and 8, the ten’s digit is 3 less than the hundred’s digit, one’s digit is the hundred’s plus the ten’s digit.","639")
             ]
tricks=[("Think of a number. Double it. Add ten. Half it. Take away the number you started with. ","5"),
       ("Think of a number. Multiply the number with 3. Now add 45 .Double the result. Divide by 6. Take away the number you started with.","15"),
       ("Pick a number from 1 to 100 now add 50, then add 20, then subtract with the number you started with","70"),
       ("Pick a number between 1-10. Add 8. Add 5. Subtract the original number you picked.","13"),
       ("Think of a number. Double it. Add six. Half it. Take away the number you started with.","3"),
       ]

#the following are global variables so that they can be used within all functions
button_start = any
entry_guess = any
chances = any
numtoguess = 0
triescount = 0
label_tries = any
label_guess = any
button_check_guess = any
label_lowest = any
label_highest = any
lowest = any
highest = any
answer_entries = []
riddles_chosen = []
difficulty_label= any
difficulty_dropdown= any
num_riddles_label= any
num_riddles_dropdown= any
start_button= any
trick_label=any
ready_forpc_label=any
ready_forpc_button=any
check_button=any
riddlelabel=any
answer_entry=any
riddle_labels = []
trickanswer_label=any
pc_checks_trickanswer_label=any
no_button=any
yes_button=any


frame = tk.Frame(root) #create the main window for the widget
frame.pack(padx=10, pady=10) #pack the window with 10cm paddings
frame.configure(bg='#D9EAFD') #background color for the window
image_pil = Image.open("main.png")  #open the image with the text "guess the number"
imagemain = ImageTk.PhotoImage(image_pil) #decode the image
labelimage = tk.Label(frame, image=imagemain,bg="#D9EAFD") #add the image to the frame
labelimage.pack() #pack the image

#function to create the main widgets (select mode)
def create_widgets():
    global entry_guess
    global mode_options
    
    button_start.destroy()
   
    tk.Label(frame, text="Select a mode:", font='Calibri 16 bold',bg="#D9EAFD").pack()

    # Combo box for the game mode
    selected_mode.set(mode_options[0])

    tk.OptionMenu(frame, selected_mode, *mode_options).pack()

    tk.Button(frame, text="Choose Mode", command=choose_mode, font='Calibri 16 bold',bg="#FFAE03",activebackground="red").pack()
button_start=tk.Button(frame,text="Start",bg="#FFAE03",font=('Calibri', 30, 'bold'),activebackground="red",command=create_widgets,width=5,height=1)
button_start.pack()

#function to try and delete all the labels for the current game mode when it ends
def delete_labels():
    try:
        entry_guess.destroy()
    except:
        pass
    try:
        label_tries.destroy()
    except:
        pass
    try:
        chances.destroy()
    except:
        pass
    try:
        label_guess.destroy()
    except:
        pass
    try:
        button_check_guess.destroy()
    except:
        pass
    try:
        label_lowest.destroy()
    except:
        pass
    try:
        lowest.destroy()
    except:
        pass
    try:
        label_highest.destroy()
    except:
        pass
    try:
        highest.destroy()
    except:
        pass
    try:
        difficulty_label.destroy()
    except:
        pass
    try:
        difficulty_dropdown.destroy()
    except:
        pass
    try:
        num_riddles_label.destroy()
    except:
        pass
    try:
        num_riddles_dropdown.destroy()
    except:
        pass
    try:
        start_button.destroy()
    except:
        pass
    try:
        trick_label.destroy()
    except:
        pass
    try:
        ready_forpc_label.destroy()
    except:
        pass
    try:
        ready_forpc_button .destroy()   
    except:
        pass
    try:
        check_button.destroy()
    except:
        pass
   
    try:
        for label in riddle_labels:
            label.destroy()

        riddle_labels.clear()
    except:
       pass

    try:
        for entry in answer_entries:
            entry.destroy()

        answer_entries.clear()
    except:
        pass
  
    try:
        trickanswer_label.destroy()
    except:
        pass
    try:
        pc_checks_trickanswer_label.destroy()
    except:
        pass
    try:
        no_button.destroy()
    except:
        pass
    try:
        yes_button.destroy()
    except:
        pass

#function to check which game mode the user chose, then create the labels required for it, then call the correct function for this mode
def choose_mode():
    global numtoguess
    global triescount
    global entry_guess
    global chances
    global label_tries
    global label_guess
    global button_check_guess
    global label_lowest
    global label_highest
    global lowest
    global highest
    global difficulty_label
    global difficulty_dropdown
    global num_riddles_label
    global num_riddles_dropdown
    global start_button
    global trick_label
    global ready_forpc_label
    global ready_forpc_button
   
    delete_labels()
   
    mode = mode_options.index(selected_mode.get())

    if mode == 0: #1 to 100
        label_tries = tk.Label(frame, text="How many tries do you want", font='Calibri 14 bold',bg='#D9EAFD')
        label_tries.pack()

        chances = tk.Entry(frame, justify=tk.CENTER, relief=tk.FLAT,
             borderwidth=2, font='Calibri 14 bold')
        chances.pack()
       
        label_guess = tk.Label(frame, text="Guess a number between 1 and 100:", font='Calibri 14 bold',bg='#D9EAFD')
        label_guess.pack()

        entry_guess = tk.Entry(frame, justify=tk.CENTER, relief=tk.FLAT,
             borderwidth=2, font='Calibri 15 bold')
        entry_guess.pack()
       
        numtoguess = random.randint(1, 100)
        triescount = 0
       
        button_check_guess = tk.Button(frame, text="Check Guess", command=guess_game,font='Calibri 16 bold',bg="#88D18A",activebackground="red")
        button_check_guess.pack()
       
    elif mode == 1: #PICK Your Range    
        label_tries = tk.Label(frame, text="How many tries do you want", font='Calibri 14 bold',bg='#D9EAFD')
        label_tries.pack()

        chances = tk.Entry(frame, justify=tk.CENTER, relief=tk.FLAT,
             borderwidth=2, font='Calibri 14 bold')
        chances.pack()
       
        label_lowest = tk.Label(frame, text="Lowest Number to Guess from", font='Calibri 14 bold',bg='#D9EAFD')
        label_lowest.pack()

        lowest = tk.Entry(frame, justify=tk.CENTER, relief=tk.FLAT,
             borderwidth=2, font='Calibri 14 bold')
        lowest.pack()
       
        label_highest = tk.Label(frame, text="Highest Number to Guess from", font='Calibri 14 bold',bg='#D9EAFD')
        label_highest.pack()

        highest = tk.Entry(frame, justify=tk.CENTER, relief=tk.FLAT,
             borderwidth=2, font='Calibri 14 bold')
        highest.pack()
       
        label_guess = tk.Label(frame, text="Guess a number", font='Calibri 14 bold',bg='#D9EAFD')
        label_guess.pack()

        entry_guess = tk.Entry(frame, justify=tk.CENTER, relief=tk.FLAT,
             borderwidth=2, font='Calibri 15 bold')
        entry_guess.pack()
       
        triescount = 0
       
        button_check_guess = tk.Button(frame, text="Check Guess", command=guess_game,font='Calibri 16 bold',bg="#88D18A",activebackground="red")
        button_check_guess.pack()
       
    elif mode == 2: #IMPOSSIBLE
        label_tries = tk.Label(frame, text="You only have 1 chance to guess the number", font='Calibri 14 bold',bg='#D9EAFD')
        label_tries.pack()
       
        chances = 1
         
        label_guess = tk.Label(frame, text="Guess the number between 1 and 100:", font='Calibri 14 bold',bg='#D9EAFD')
        label_guess.pack()

        entry_guess = tk.Entry(frame, justify=tk.CENTER, relief=tk.FLAT,
             borderwidth=2, font='Calibri 15 bold')
        entry_guess.pack()
       
        numtoguess = random.randint(1, 100)
        triescount = 0
       
        button_check_guess = tk.Button(frame, text="Check Guess", command=guess_game,font='Calibri 16 bold',bg="#88D18A",activebackground="red")
        button_check_guess.pack()
       
    elif mode == 3: #RIDDLES
        difficulty_label = tk.Label(frame, text="Choose difficulty:",font='Calibri 14 bold',bg='#D9EAFD')
        difficulty_label.pack()

        difficulty_dropdown = tk.OptionMenu(frame, difficulty_var, *difficulty_options)
        difficulty_dropdown.pack()
        
        num_riddles_label = tk.Label(frame, text="How many riddles? (1 to 7)",font='Calibri 14 bold',bg='#D9EAFD')
        num_riddles_label.pack()

        num_riddles_dropdown = tk.OptionMenu(frame, num_riddles_var, *num_riddles_options)
        num_riddles_dropdown.pack()
        
        start_button = tk.Button(frame, text="Start Game", command=start_game,font='Calibri 16 bold',bg="#88D18A",activebackground="red")
        start_button.pack()
        
    elif mode==4: #Mind Reading Computer
        global trickanswer, trick
        trick,trickanswer=random.choice(tricks)
        trick_label = tk.Label(frame, text=trick,font='Calibri 14 bold',bg='#D9EAFD')
        trick_label.pack()
        ready_forpc_label = tk.Label(frame, text="Ready for me to guess?",font='Calibri 14 bold',bg='#D9EAFD')
        ready_forpc_label.pack()
        ready_forpc_button = tk.Button(frame, text="Yes", command=show_mindread_answer,font='Calibri 16 bold',bg="#88D18A",activebackground="red")
        ready_forpc_button.pack()
    
#the main game function for the first 3 modes
def guess_game():
    global chances
    global numtoguess
    global triescount
   
    if numtoguess == 0:
            numtoguess = random.randint(int(lowest.get()), int(highest.get()))

    guess = int(entry_guess.get())

    try:
        chancesss = int(chances.get())
    except:
        chancesss = chances

    triescount += 1

    if numtoguess == guess:
        messagebox.showinfo("Congratulations", "You guessed the correct number!\nIt was on try number " + str(triescount))

        numtoguess = 0
        triescount = 0

        delete_labels()

        return
    elif numtoguess > guess:
        messagebox.showinfo("Incorrect", "Too low!")
        entry_guess.delete(0, tk.END)
    elif numtoguess < guess:
        messagebox.showinfo("Incorrect", "Too high!")
        entry_guess.delete(0, tk.END)

    if triescount >= chancesss:
        messagebox.showinfo("You lost!", "Tries done.\nThe number is " + str(numtoguess))

        numtoguess = 0
        triescount = 0

        delete_labels()

        return
        
#mindreader game function
def show_mindread_answer():
    global trickanswer_label,pc_checks_trickanswer_label,no_button,yes_button
    try:
        trickanswer_label.destroy()
    except:
        pass
    try:
        pc_checks_trickanswer_label.destroy()
    except:
        pass
    try:
        no_button.destroy()
    except:
        pass
    try:
        yes_button.destroy()
    except:
        pass
    trickanswer_label = tk.Label(frame, text=trickanswer,font='Calibri 14 bold',bg='#D9EAFD')
    trickanswer_label.pack()
    pc_checks_trickanswer_label = tk.Label(frame, text="Did I guess right?",font='Calibri 14 bold',bg='#D9EAFD')
    pc_checks_trickanswer_label.pack()
    no_button = tk.Button(frame, text="No", command=show_message_no,font='Calibri 16 bold',bg="red",activebackground="#094D92")
    no_button.pack()
    yes_button = tk.Button(frame, text="Yes", command=show_message_yes,font='Calibri 16 bold',bg="#88D18A",activebackground="#094D92")
    yes_button.pack()
    
#show messagebox if answer was incorrect
def show_message_no():
    messagebox.showinfo("Incorrect", "Maybe next time. For now I will work on my mind reading skills")
    delete_labels()
    
#show msgbox if answer is correct
def show_message_yes():
    messagebox.showinfo("Correct", "I can read your mind!")
    delete_labels()
    
#riddles game function
def start_game():
    global difficulty_var, num_riddles_var, riddles_chosen

    difficulty = difficulty_var.get().lower()
    num_riddles = int(num_riddles_var.get())

    if difficulty == "easy":
        riddles_chosen = random.sample(easy_riddles, num_riddles)
    elif difficulty == "medium":
        riddles_chosen = random.sample(medium_riddles, num_riddles)
    else:
        riddles_chosen = random.sample(hard_riddles, num_riddles)

    delete_labels()
    display_riddles()

#display the riddles
def display_riddles():
    global answer_entries
    global check_button
    global riddlelabel
    global answer_entry
    global riddle_labels
  
    riddle_labels = []  
    answer_entries = [] 

    index = 1
    for riddle, _ in riddles_chosen:
        riddlelabel = tk.Label(frame, text=f"{index}: {riddle}",font='Calibri 13 bold',bg='#D9EAFD')
        riddlelabel.pack()
        index += 1
        riddle_labels.append(riddlelabel)
        
        answer_entry = tk.Entry(frame,font='Calibri 14 bold')
        answer_entry.pack()
        answer_entries.append(answer_entry)
    check_button = tk.Button(frame, text="Check Answers", command=check_answers,font='Calibri 16 bold',bg="#88D18A",activebackground="#094D92")
    check_button.pack()
    
#check if riddles answers were correct
def check_answers():
    global correct_answers
    correct_answers = 0
    incorrect_answers = []
   
    index = 1
    for _, correct_answer in riddles_chosen:
        user_answer = int(answer_entries[index - 1].get())
        if user_answer == int(correct_answer):
            correct_answers += 1
            
        else:
            incorrect_answers.append(f"Riddle {index}: {user_answer} (Correct Answer: {correct_answer})")
        index += 1
    display_result(correct_answers, incorrect_answers)
    return correct_answers

#display result of riddles
def display_result(correct_answers, incorrect_answers):
    result_message = f"You solved {correct_answers} out of {len(riddles_chosen)} riddles correctly."

    if incorrect_answers:
        result_message += "\nIncorrect answers:\n" + "\n".join(incorrect_answers)

    messagebox.showinfo("Result", result_message)
    
    delete_labels()
 
#open the game window
root.mainloop()
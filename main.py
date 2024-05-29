import random

fruit_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince"]

#Holding random chosen fruit 
chosen_fruit = random.choice(fruit_list)

#Calculate word lengnt to generate display group 
word_length = len(chosen_fruit)

hangman_intro = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""
print(hangman_intro)

#Create list with blank spaces 
display = []
for _ in range(word_length):
    display += "_"

#bool to check if user hasnt guessed all letters
end_of_game = False

print(f'TIP: It is a fruit and has {word_length} letters')

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_fruit[position]
    
        if letter == guess:
            display[position] = letter

    print(display)

    #check if there is more "_" in the display otherwise user wins
    if "_" not in display:
        end_of_game = True
        print("You win.")
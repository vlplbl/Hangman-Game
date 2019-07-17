import re

class Hangman:
    def __init__(self):
        self.running = True
        self.guesses = 9
        print("This is a Hangman game. You have 9 tries to guess the word. Good Luck!")
        self.img = {
            '8':"""
            
                |    
                |    
                |   
                |    
                |   
            """,
            
            '7':"""
                 _____
                |    
                |    
                |    
                |    
                |   
            """,
            
            
            '6':"""
                 _____
                |    |
                |    
                |    
                |    
                |   
            """,
            
            
            '5':"""
                 _____
                |    |
                |    O
                |    
                |    
                |   
            """,
            
            '4':"""
                 _____
                |    |
                |    O
                |    |
                |    |
                |   
            """,
            
            '3':"""
                 _____
                |    |
                |    O
                |   /|
                |    |
                |   
            """,
            
            '2':"""
                 _____
                |    |
                |    O
                |   /|\\
                |    |
                |   
            """,
            
            '1':"""
                 _____
                |    |
                |    O
                |   /|\\
                |    |
                |   / 
            """,
            
            '0':"""
                 _____
                |    |
                |    O
                |   /|\\
                |    |
                |   / \\
            """
            }
    

    def start_screen(self):
        incorrect = True
        while incorrect:
            self.word = input('Please enter the secret word: ').lower()
            if re.match('^[a-zA-Z]+', self.word) and len(self.word) > 2:
                self.masked_word = list(len(self.word) * '_')
                incorrect = False
            else:
                print("Please enter a valid word containing letters only (a-z): ")
            
    def guess(self):
        run = True
        while run:
            char = input('guess a letter: ').lower()
            if re.match('^[a-zA-Z]', char) and len(char) == 1:
                if char in self.word and char not in self.masked_word:
                    for index, letter in enumerate(self.word):
                        if char == letter:
                            self.masked_word[index] = char
                    print(self.masked_word)
                    if "_" not in self.masked_word:
                        print('You win! The word is:', self.word, '\nUnused guesses:', str(self.guesses))
                        run = False
                else:
                    self.guesses -= 1
                    print('Wrong! Guesses left:', self.guesses, self.img[str(self.guesses)], '\n', self.masked_word)
                if self.guesses <= 0:
                    print('You suck! Try again later')
                    run = False
                    
            else:
                print("Enter a single letter (a-z)!")

    def game_over_screen(self):
        waiting = True
        while waiting:
            answer = input("Play again? (Y/N): ").upper()
            if answer == 'N':
                self.running = False
                waiting = False
            elif answer == 'Y':
                self.guesses = 9
                waiting = False
            else:
                print("Enter Y or N")

game = Hangman()
while game.running:
    game.start_screen()
    game.guess()
    game.game_over_screen()


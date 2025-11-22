import random as rnd


def main():
        difficulty_level = int(input("Enter your choice: "))
        levels = {1:["Easy", 10], 2:["Medium", 5], 3:["Hard", 3]}
        
        while True:
            if difficulty_level <= 3 and difficulty_level >=1:
                print(f"Great! You've chosen {levels[difficulty_level][0]} difficulty level with {levels[difficulty_level][1]} choices!")
                print("Let's Start!!!\n\n")
                break   
            else:    
                print("Invalid Level Choice. Please enter an integer between 1 to 3.")
                difficulty_level = int(input("Enter your choice: "))
        
        num = rnd.randint(0,100)
        i = 0
        while i<= levels[difficulty_level][1]-1:
            guess = int(input("Make a Guess: "))
            if guess > num:
                print("Too High!\n")
            elif guess < num:
                print("Too Low!\n")
            else:
                print(f"Congratulations! You've guessed the number {num} correctly!\n")
                break
            
            if i == levels[difficulty_level][1]-1:
                print(f"Sorry! You've used all your chances. The correct number was {num}.\n")
            i += 1 
        
            
        
if __name__ == "__main__":
    while True:    
        print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
        print("Please Select the Difficulty Level")
        print("1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")
        main()
        user_input = input("Do you want to play again? (yes/no): ").lower()
        if user_input != 'yes':
            print("Thank you for playing! Goodbye!")
            break
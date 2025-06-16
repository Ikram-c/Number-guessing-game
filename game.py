import random

class Game:
    """
    A class to represent the Number Guessing Game.

    Attributes:
        total_attempts (int): The total number of guesses made across all games played.
        correct_guesses (int): The total number of games won.
    """
    def __init__(self):
        """Initializes the game with zero total attempts and correct guesses."""
        self.total_attempts = 0
        self.correct_guesses = 0

    def play_round(self):
        """Plays a single round of the number guessing game."""
        secret_number = random.randint(1, 10)
        guesses_this_round = 0
        user_guesses = []

        print("\nI am guessing a number between 1 and 10.")

        while guesses_this_round < 3:
            try:
                guess = int(input(f"Attempt {guesses_this_round + 1}/3 - Enter your guess: "))
                user_guesses.append(guess)
                guesses_this_round += 1
                self.total_attempts += 1

                if guess < secret_number:
                    print(f"Your guess of {guess} is too low.")
                elif guess > secret_number:
                    print(f"Your guess of {guess} is too high.")
                else:
                    self.correct_guesses += 1
                    print(f"Congratulations! You guessed the number {secret_number} correctly in {guesses_this_round} tries!")
                    print(f"Your guesses were: {user_guesses}")
                    return # Exit the round since the number was guessed
            
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        # This code runs if the loop finishes without a correct guess
        print("\nSorry, you've run out of attempts.")
        print(f"The correct number was {secret_number}.")
        print(f"Your guesses were: {user_guesses}")

    def start(self):
        """Starts and manages the game loop, allowing the user to play multiple rounds."""
        play = True
        while play:
            self.play_round()
            
            while True:
                again = input("\nDo you want to play again? (Y/N): ").upper()
                if again in ["Y", "N"]:
                    break
                print("Invalid input. Please enter 'Y' or 'N'.")

            if again == "N":
                play = False
        
        print("\nThanks for playing!")
        print(f"Total attempts made: {self.total_attempts}")
        print(f"Total games won: {self.correct_guesses}")


if __name__ == "__main__":
    number_game = Game()
    number_game.start()

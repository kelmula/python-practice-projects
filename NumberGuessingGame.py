import random

play_game = 'play'

while play_game == 'play':
    random_num = random.randint(1,10)
    user_num = int(input("Guess a number between 1 and 10: "))

    if user_num == random_num:
        print(f"The number is {random_num}.  Your guess was correct!")
        print()
    elif user_num < 1 or user_num > 10:
        print("Number must be between 1 and 10 (inclusive).")
        print()
        continue
    elif user_num != random_num:
        print(f"The number is {random_num}.  Your guess was incorrect.")
        print()

    while True:
        play_game = str(input("Type 'play' to play again or 'quit' to quit the game: ")).lower()
        if play_game == 'play':
            print()
            break
        elif play_game == 'quit':
            print()
            print("Thanks for playing!")
            exit()
        elif play_game != 'quit' or play_game != 'play':
            print()
            print("Invalid entry")
            continue
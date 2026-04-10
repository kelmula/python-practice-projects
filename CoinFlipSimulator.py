import random

print("Let's flip a coin.")

while True:
    flip_coin = str(input("Type 'flip' to flip the coin or 'quit' to quit playing: ")).lower()
    if flip_coin == 'flip':
        break
    elif flip_coin == 'quit':
        print("Maybe next time.  Goodbye.")
        exit()
    else:
        print("Invalid entry")
        continue

while flip_coin == 'flip':
        coin_flip = random.randint(0, 1)
        if coin_flip == 0:
            print("Heads")
        elif coin_flip == 1:
            print("Tails")

        while True:
            flip_coin = str(input("Type 'flip' to flip the coin again or 'quit' to quit playing: ")).lower()
            if flip_coin == 'flip':
                break
            elif flip_coin == 'quit':
                print("Thanks for playing!")
                exit()
            else:
                print("Invalid entry")
                continue
import random


def play():
    secret = random.randint(1, 100)
    tries = 0

    while True:
        guess = int(input("Guess (1-100): "))
        tries += 1

        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print(f"Correct in {tries} tries!")
            break


if __name__ == "__main__":
    play()

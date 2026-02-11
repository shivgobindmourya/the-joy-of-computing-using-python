"""
Permutations - Jumbled Word Game

Two-player game:
- Computer picks word
- Jumbles it
- Players guess
- Score updates
"""

import random


def choose_word():
    words = [
        "rainbow", "computer", "science",
        "programming", "mathematics",
        "player", "condition", "reverse",
        "water", "boat"
    ]
    return random.choice(words)


def jumble_word(word):
    shuffled = random.sample(word, len(word))
    return "".join(shuffled)


def show_result(p1, p2, s1, s2):
    print("\nFinal Scores:")
    print(f"{p1}: {s1}")
    print(f"{p2}: {s2}")
    print("Thanks for playing!")


def play():
    p1 = input("Enter Player 1 name: ")
    p2 = input("Enter Player 2 name: ")

    score1 = 0
    score2 = 0
    turn = 0

    while True:
        picked = choose_word()
        question = jumble_word(picked)

        print("\nJumbled Word:", question)

        if turn % 2 == 0:
            print(f"{p1}'s Turn")
            answer = input("Guess the word: ")
            if answer == picked:
                score1 += 1
                print("Correct!")
            else:
                print("Wrong! Word was:", picked)
        else:
            print(f"{p2}'s Turn")
            answer = input("Guess the word: ")
            if answer == picked:
                score2 += 1
                print("Correct!")
            else:
                print("Wrong! Word was:", picked)

        turn += 1

        cont = input("Press 1 to continue, 0 to quit: ")
        if cont == "0":
            show_result(p1, p2, score1, score2)
            break


if __name__ == "__main__":
    play()

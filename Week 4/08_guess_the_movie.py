import random

movies = [
    "sholay",
    "lagaan",
    "swades",
    "queen",
    "barfi",
    "pk",
    "raazi",
    "war",
    "sultan",
    "dangal",
    "drishyam",
    "andhadhun",
    "kahaani",
    "tumbbad",
    "kick",
    "don",
    "rockstar",
    "ghajini",
    "baazigar",
    "veer zaara",
    "chandni",
    "mohra",
    "lootera",
    "badhaai ho",
    "article fifteen",
    "tamasha",
    "padmaavat",
    "raanjhanaa",
    "blackmail",
    "krrish"
]

def create_question(movie):
    temp = []
    for ch in movie:
        if ch == " ":
            temp.append(" ")
        else:
            temp.append("*")
    return "".join(temp)

def is_present(letter, movie):
    return movie.count(letter) > 0

def unlock(question, movie, letter):
    new_question = ""
    for i in range(len(movie)):
        if movie[i] == " ":
            new_question += " "
        elif movie[i] == letter:
            new_question += letter
        else:
            new_question += question[i]
    return new_question

def play():
    p1 = input("Player 1 enter your name: ")
    p2 = input("Player 2 enter your name: ")

    score1 = 0
    score2 = 0
    turn = 0
    willing = True

    while willing:
        if turn % 2 == 0:
            player = p1
        else:
            player = p2

        print("\n", player, "it's your turn!")

        movie = random.choice(movies)
        question = create_question(movie)
        print("Movie:", question)

        not_said = True

        while not_said:
            choice = input("Enter 1 to guess letter, 2 to guess movie: ")

            if choice == "1":
                letter = input("Enter letter: ").lower()

                if is_present(letter, movie):
                    question = unlock(question, movie, letter)
                    print("Updated:", question)
                else:
                    print("Letter not found!")

            elif choice == "2":
                guess = input("Enter movie name: ").lower()
                if guess == movie:
                    print("Correct Answer!")
                    if turn % 2 == 0:
                        score1 += 1
                    else:
                        score2 += 1
                    not_said = False
                else:
                    print("Wrong Answer! Try again.")

        print("\nScores:")
        print(p1, ":", score1)
        print(p2, ":", score2)

        cont = input("Enter 1 to continue, 0 to quit: ")
        if cont == "0":
            willing = False
        else:
            turn += 1

    print("\nFinal Scores:")
    print(p1, ":", score1)
    print(p2, ":", score2)
    print("Thanks for playing!")

if __name__ == "__main__":
    play()

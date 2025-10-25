import random

words = {"cat": "кошка", "apple": "яблоко", "house": "дом"}


def get_random_word():
    return random.choice(list(words.keys()))


def setup_game():
    try:
        number_of_words = int(input("How many word do you want to guess?: "))
    except ValueError:
        number_of_words = 5
    except Exception as e:
        print(f"Unknown exeption {e}")
    return 0, number_of_words, number_of_words


print("Hello! Let's start game!")
is_game = True
points, number_of_words, total_words = setup_game()
while is_game:
    word = get_random_word()
    answer = input("Translate this word: «{}» ".format(word))
    if answer == words[word]:
        print("Correct!")
        points += 1
    else:
        print("Incorrect! Correct answer is «{}»".format(words[word]))
    number_of_words -= 1
    if number_of_words <= 0:
        print("Your result is {} from {}".format(points, total_words))
        if input("Do you want play again? yes/no") == "yes":
            points, number_of_words, total_words = setup_game()
        else:
            is_game = False

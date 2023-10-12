import requests
import random


def generate_word_list():
    response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
    word_list = response.content.splitlines()
    word_list = [word.decode("utf-8") for word in word_list]
    return word_list


hangman_words = generate_word_list()

random_word_list = random.sample(hangman_words, 5)

# print(random_word_list)

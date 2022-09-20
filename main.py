import random
from termcolor import colored
import os

def load_word():
    with open("words.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def display_graph(turn, guess, word, graph):
    for i in range(len(word)):
        if word[i] == guess[i]:
            graph[turn][i] = colored(word[i], 'green')
        elif guess[i] in word:
            graph[turn][i] = colored(guess[i], 'yellow')
        else:
            graph[turn][i] = colored(guess[i], 'red')

    for lines in graph:
        print(*lines)
    return ''


def main():

    word = load_word()
    turn = 0

    graph = [['*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*']]

    print('Welcome to Wurdle!')
    for lines in graph:
        print(*lines)
    guess = input('Guess a word: ')

    while turn <= 4:
        if len(guess) != 5:
            for lines in graph:
                print(*lines)
            guess = input('Enter a 5 letter word: ')
        elif guess == word:
            for i in range(len(word)):
                graph[turn][i] = colored(word[i], 'green')
            for lines in graph:
                print(*lines)
            return 'Congrats, you win!'
        elif turn == 4:
            display_graph(turn, guess, word, graph)
            print(f'You lose! The word was: {word}')
            break
        else:
            display_graph(turn, guess, word, graph)
            guess = input('Guess a word: ')
            turn += 1
    return ''


if __name__ == "__main__":
    print(main())



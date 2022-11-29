import random
from words import words
from monito import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print('Tienes', lives, 'restantes, has usado las siguientes letras: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('La palabra a encontrar es: ', ' '.join(word_list))

        user_letter = input('Ingresa una letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1
                print('\nLa letra,', user_letter, 'no está en la palabra')
        elif user_letter in used_letters:
            print('\nYa has usado esta letra, intenta con otra.')
        else:
            print('\nEsta letra no es válida.')
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Te ahorcaron :( tu palabra es: ', word)
    else:
        print('Adivinaste la palabra:', word,', ¡¡Felicidades!!')
if __name__ == '__main__':
    hangman()

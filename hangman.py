import requests
import random
import string


class Game:
    
    def __init__(self):
        self.api = 'https://api.dicionario-aberto.net/random'

    def get_data(self):
        response = requests.get(self.api)
        if response.status_code == 200:
            self.word = response.json()
            return self.word['word']

        else:
           print(f"Olá, ocorreu o erro {response.status_code} com a sua requisição.")

    def hangman(self, word):
        word_letters = set(word) #letters in the word
        alphabet = set(string.ascii_lowercase + 'çãíõéàýêîâôẽ')
        used_letters = set() #what the user has guessed

        lives = 6

        #getting user input
        while len(word_letters) > 0 and lives > 0:
            print(f'\nVocê tem {lives} vidas restantes e usou essas letras:', ' '.join(used_letters).upper())

            word_list = [letter if letter in used_letters else '-' for letter in word]
            print('\nPalavra atual:', ' '.join(word_list).upper())

            user_letter = input('\nTente adivinhar uma letra: ').lower()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)

                else:
                    lives -= 1
                    print('\nEssa letra não está na palavra')

            elif user_letter in used_letters:
                print('\nVocê já usou essa letra.')
            
            else:
                print('\nCaractere inválido.')

        if lives == 0:
            print(f'\nVocê morreu a palavra era "{word.upper()}"')
            play_again = input('\nQuer jogar novamente? s/n: ').lower()     
            if play_again !='s':
                quit('\nOk, tchau!')
            else:
                Game().call_class()

        else:
            print(f'\nVocê acertou a palavra "{word.upper()}"')
            play_again = input('\nQuer jogar novamente? s/n: ').lower()
            if play_again !='s':
                quit('\nOk, tchau!')
            else:
                Game().call_class()

    def call_class(self):
        game = Game()
        data = game.get_data()
        hangman = game.hangman(data)

dashs = '-' * 40









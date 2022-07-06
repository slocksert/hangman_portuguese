import hangman

def main():
    welcome = input(f'{hangman.dashs}\nVocê quer jogar o jogo da forca? s/n\n{hangman.dashs}\n\n')

    if welcome != 's':
        quit('\nOk, tchau!')

    else:
        hangman.Game().call_class()

if __name__ == '__main__':
    main()
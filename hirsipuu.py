from ctypes.wintypes import WORD
import random
import string
from valinta import sana
#print (words)


#def get_valid_word(sana):
    #word = random.choice(words)
    #while '-' in word or ' ' in word:
    #    word = random.choice(words)
    
    #return word

def hangman():
    # word = get_valid_word(sana)
    word = sana
    word_letters = set(word) # sanan kirjaimet
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # käyttäjän veikkaukset

    lives = 10

    while len(word_letters) > 0 and lives > 0:
        # käytetyt kirjaimet
        print('Sinulla on ', lives, ' elämää jäljellä ja olet käyttänyt nämä kirjaimet: ', ' '.join(used_letters))

        # nykyinen sana on esim. SIP-T-I (sipatti)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Nykyinen sana: ', ' '.join(word_list))

        user_letter = input('Veikkaa kirjain: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # vähennetään yksi elämä
                print('Kirjain ei sisälly sanaan')
        elif user_letter in used_letters:
            print('Olet jo käyttänyt tämän kirjaimen. Veikkaa uudestaan: ')
        else:
            print('Epäsopiva merkki. Yritä uudestaan. ')

    # pääsee tänne kun len(word_letters) == 0
    if lives == 0:
        print('Kuolit. Sana olisi ollut', word)
    else:
        print('Arvasit sanan',word, '!!')

hangman()

#while True:
    #print('Haluatko pelata uudestaan?')
    #if input('Haluatko pelata uudestaan? Valitse "kyllä" tai "ei"') == 'kyllä':
        #hangman()
    #else:
        #False

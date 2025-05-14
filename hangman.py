#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    word =open(file_name, "r")
    txt =   word.readlines()
    word.close()
    return txt

    

def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    word_index = random.randint (0,len(words)-1)
    word_choice = words[word_index]
    letter_index = random.randint (0,len(word_choice)-1)
    random_choice = word_choice[letter_index]
    letter_renewal = word_choice.replace(random_choice,'_')

    output = "Guess the word: "+ letter_renewal
    print (output)
    return word_choice

    

def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    a = input("Guess the missing letter: ")
    return a


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')
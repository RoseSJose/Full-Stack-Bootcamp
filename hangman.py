import random

#symbolic constants
SUCCESS = 10
CORRECT = 200
WRONG = 300
DEAD = 400
REPEAT = 500

def get_word(fname):
    good_words = []
    f = open(fname)
    for i in f:
        i = i.strip()
        if len(i) < 5:
            continue
        if i.istitle():
            continue
        if not i.isalpha():
            continue
        #print(good_words)
        
        good_words.append(i)
        #return good_words
    f.close()
    return random.choice(good_words)
    
def mask_word(word, letter_to_show):
    op = []
    for i in word:
        if i in letter_to_show:
            op.append(i)
        else:
            op.append("_")
    return " ".join(op)
    
def create_status(word, guesses, turn_left):
    guesses = " ".join(guesses)
    word = mask_word(word, guesses)
    return f"Word : {word} Guesses : {guesses} Turns left : {turn_left}"
    
def check_guess(word, letter, guesses, turn_left):
    all_guessed = True
    t = guesses + [letter]
    for i in word:
        if i not in t:
            all_guessed = False
            break
    if all_guessed:
        return SUCCESS
        
    if letter in guesses:
        return REPEAT
    elif letter in word:
        return CORRECT
    else:
        if turn_left == 1:
            return DEAD
        else:
            return WRONG
            
def main():
    turn_left = 10
    guesses = []
    word = get_word("/usr/share/dict/words")
    while True:
        status = create_status(word, guesses, turn_left)
        print(status)
        guess = input("Enter input")
        r = check_guess(word, guess, guesses, turn_left)
        if r == CORRECT:
            guesses.append(guess)
        elif r == WRONG:
            turn_left-=1
            guesses.append(guess)
        elif r == REPEAT:
            print(f"Sorry you have already guessed {guess}")
        elif r == DEAD:
            print(f"Sorry! You have run out of moves. The word was {word}")
            break
        elif r == SUCCESS:
            print(f"Congratulations! You got it, The word was {word}")
            break
    
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

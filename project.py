import random

letters = [['h','o','l','i','d','a','y'],
           ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm','i','n','g'],
           ['b','o','o','t','c','a','m','p'],
           ['f','l','o','w','c','h','a','r','t'],
           ['w', 'o', 'r', 'd', 's', 'c', 'a','p','e','s']]

words = [["hi","hay","day","had","lay","dal","lad","lid","hold","lady","hail"],
         ["go","an","in","no","on","map","mom","gap","gag","pig","man","ping",
          "pong","pram","prom","ramp"],
         ["am","at","to","cab","cap","cob","cop","map","mop","act","bat","camp",
          "comb","boom","pact","atom"],
         ["of","at","or","to","caw","cow","how","who","calf","claw","flaw","flow",
          "fowl","wolf","crow","half"],
         ["we","do","as","cap","caw","cop","cow","paw","cod","dew","pad","cape",
          "cope","crap","crew","crop","pace"]]







wrong_guesses = 0
level = 0

while level < len(letters):
    three_letter_words = []
    for three_char_word in words[level]:
        if all (i in letters[level] for i in three_char_word) and len(three_char_word) == 3:
            three_letter_words.append(three_char_word)
    
    print("Guess a 3-letter word from level" ,level+1,":")
    guess = input().strip().lower()

    if guess in three_letter_words:
        print("Your guess is correct !")
        level += 1
        if level == len(letters):
            print("!!! Congratulations !!!  You've completed the game successfully.")
            break
        print("Proceeding to the next level.")
    else:
        print("Your guess is incorrect.")
        wrong_guesses += 1
        if wrong_guesses ==5:
            
            print("You made 5 wrong guesses. Game over.")
            break

    if level == 2:
        choice = input("Do you want to continue to the next level ? (yes/no): ")
        if choice.lower() == 'no':
            print("You have discontinued the game after level", level + 1)
            break
        print("Continuing to the next level.")
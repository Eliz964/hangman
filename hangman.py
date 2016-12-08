import random
myword = random.choice(open("hangmanwords.txt").read().split())

word_len = len(myword)
myword_list = list(myword)
alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]

def diagram(i):
    file_name = "".join(["hangman", str(i), ".txt"])
    with open(file_name, "r") as file:
      for line in file:
        print line

word_progress = ["_"] * word_len

print ('\nWelcome to Liz\'s first "Big Girl Program", Hangman. You get 6 wrong guesses. Ready? Begin.\n')
print "Your word: ",
print (" ".join(word_progress))

count = 0
guess_list = []
while count < 6:
    guess = raw_input("Guess a letter: ").lower()
    if guess not in alphabet:
        print "Please guess a single letter."
        print ("\n------------------------------------------\n")
        continue
    if guess not in guess_list:
        guess_list.append(guess)
        guess_list.sort()
        if guess in myword:
            diagram(count)
            print ("Success!")
            for n,i in enumerate(myword_list):
                if i == guess:
                    word_progress[n] = guess
            if word_progress == myword_list:
                print (" ".join(word_progress))
                print ("You won!\n"),
                count = 8
            else:
                print ("Incorrect guesses: %i") % count
                print ("Letters guessed: "),
                print (', '.join(guess_list))
                # indeces = find(myword, guess)
                print (" ".join(word_progress))
        else:
            count += 1
            diagram(count)
            print ("Sorry! Try again.")
            print ("Incorrect guesses: %i") % count
            print ("Letters guessed: "),
            print (', '.join(guess_list))
            print (" ".join(word_progress))
    else:
        print ("You already tried that letter.")
    print ("\n------------------------------------------\n")
    continue
if count == 6:
    count += 1
    diagram(count)
print ("\nGAME OVER. Your word was '%s'.\n") % myword

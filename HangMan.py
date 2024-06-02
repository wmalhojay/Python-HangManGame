import random

print('''
                        ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
                        ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
                        ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
                        ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
                        ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
                        ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
''')

guessWords = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
    "watermelon", "xigua", "yam", "zucchini", "apricot",
    "blueberry", "coconut", "dragonfruit", "eggplant", "feijoa",
    "grapefruit", "huckleberry", "jackfruit", "kumquat", "lime",
    "melon", "nectar", "olive", "peach", "plum",
    "pineapple", "pomegranate", "quinoa", "rhubarb", "starfruit",
    "tomato", "uva", "violet", "walnut", "xylophone",
    "yellow", "zebra", "aardvark", "bison", "cheetah",
    "dolphin", "elephant", "flamingo", "gorilla", "hippopotamus"
]

stages = ['''  
  +---+
      |
      |
      |
      |
      |
=========
''','''
  +---+
  |   |
      |
      |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

counter = 0
def printStickMan(boolean):
    global counter
    if boolean == False:
       counter += 1 
    print(stages[counter])
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ \n") 

def randomWordChooser(guess):
    return guess[random.randint(0, len(guess))-1]

def isCorrect(guessLetter, word, listCopy):
    for i in range(0, len(word)):
        if word[i] == guessLetter:
            listCopy[i] = guessLetter
            return True

def isRepeat(listCopy):
    while True:
        a = ''
        temp = input("𝕘𝕦𝕖𝕤𝕤 𝕒 𝕝𝕖𝕥𝕥𝕖𝕣 : ")
        for i in listCopy:
            if i == temp:
                print(f"You already guessed {temp} ... TRY AGAIN")
                break
            else:
                 a = 'notEqual'
        if a == 'notEqual':
             break
    return temp

word = list(randomWordChooser(guessWords))
listCopy = list()

for i in range(0, len(word)):
    listCopy.append('_')

while counter != 7:
    guessLetter = isRepeat(listCopy)
    if isCorrect(guessLetter, word, listCopy):
        print(f'''                                      {' '.join(listCopy)}''')
        print("Guessed it right !")
        printStickMan(True);
    else:
        print(f'''                                      {' '.join(listCopy)}''')
        print("Wrong Guess Sorry. You loose a life .Try again ")
        printStickMan(False);

if listCopy == word.copy():
        print('''
            
                        ██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗░█████╗░███╗░░██╗
                        ╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██╔══██╗████╗░██║
                        ░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║░░██║██╔██╗██║
                        ░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║░░██║██║╚████║
                        ░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║
                        ░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝
    ''')
else:
        print('''

                    ██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░█████╗░░██████╗███████╗
                    ╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔══██╗██╔════╝██╔════╝
                    ░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║██║░░██║╚█████╗░█████╗░░
                    ░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║██║░░██║░╚═══██╗██╔══╝░░
                    ░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝╚█████╔╝██████╔╝███████╗
                    ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░░╚════╝░╚═════╝░╚══════╝
    ''')


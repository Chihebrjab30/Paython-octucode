HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random

words = ["power", "fight", "world"]
computer = random.choice(words)
space = ["_"] * len(computer)
print(" ".join(space))
print(HANGMANPICS[0])

lives = 6
guessd = []

while "_" in space and lives > 0:
    user = input("Choose a letter: ").lower()
    if user in guessd:
        print("⚠️ You already guessed this letter!")
        continue
    guessd.append(user)
    if user not in computer:
        lives -= 1
        print(HANGMANPICS[6 - lives])
    else:
        for i in range(len(computer)):
            if user == computer[i]:
                space[i] = user
        print(" ".join(space))
        print(f"You have {lives} attempts left")

if lives == 0:
    print("""
    **************
        You lost 👾
    **************
    """)
    print(HANGMANPICS[-1])
else:
    print("""
    ••••••••••••••
        You win 🎉
    ••••••••••••••
    """)
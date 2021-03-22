import random

images = ['''
------------
|         |
|
|
|
|
|


''', '''


------------
|         |         
|         O
|
|
|
|
''', '''


------------
|         | 
|         O 
|        / 
|   
|
|
''', '''


------------
|         | 
|         O 
|        / \\
|   
|
|
''', '''

------------
|         | 
|         O 
|        / \\ 
|         |
|
|
 ''',  '''


------------
|          |
|          O
|         / \\
|          |
|         / 
|
|            ''', '''


------------
|          |
|          O 
|         / \\
|          |
|         / \\ 
|
|            ''']


word_list = '''apple ant banana bat bear beaver camel cat clam cobra caterpillar
crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama
monkey moose mouse newt owl panda parrot pigeon python rabbit
rat seal shark sheep skunk sloth snake spider stork swan tiger
trout turkey turtle weasel whale wolf wombat yak zebra'''.split()
print(word_list)


# chosing random word from the list
chosen_word = random.choice(word_list)
print(chosen_word)

# create the emty list for _ _ _ ...
display = ['_'] * len(chosen_word)
print(display)

# images length = 7
images_len = 0
word_len = len(chosen_word)
count = 0


dic = {}


while(images_len < 7 and count != word_len):
    print(display)

    # ask the user to guess a letter
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        z = 0

        # check if the guessed letter in the the chosen word or not
        if guess == chosen_word[i] and i not in dic:
            display[i] = chosen_word[i]
            count += 1
            z = 1
            dic[i] = i
            break
    if z == 0:
        print(images[images_len])
        images_len += 1

x = "".join(display)
if x == chosen_word:
    print(display)
    print(x)
    print('You Won')
else:
    print('\n\n')
    print('You Lose')
# print(display, chosen_word)

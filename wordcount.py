# put your code here.
"""
Write a program, wordcount.py, that opens a file and counts how many 
times each space-separated word occurs in that file. 
Your program should then print those counts to the screen.

open the file
figure out how to space-separate the words.
set up a dictionary
contains word and count
print the counts to the screen
we'll need a for loop to parse the words.
"""
count_the_words = open("test.txt")
word_map = {}
words = {}
for line in count_the_words:
        line = line.rstrip()
        words = line.split(' ')
        for word in words:
            key = word
            word_map[key] = word_map.get(key, 0) + 1
            print(f"{key}, {word_map.get(key, 0) + 1}")
#print(word_map)    
        

"""
for key, value in words.items():
    print(f'{key}, {value}')
"""

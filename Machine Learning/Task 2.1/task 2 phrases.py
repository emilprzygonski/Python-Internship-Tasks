import numpy as np

f = open("skychallenge_skyphrase_input.txt", "r")

count_valid = 0
count_nonvalid = 0

for test_string in f:
    phrase = test_string.split()
    all_words = len(phrase)
    unique_words = len(np.unique(np.array(phrase)))
    if all_words == unique_words:
        count_valid += 1
    else:
        count_nonvalid += 1

print(f'There are {count_valid} valid skyphrases.')


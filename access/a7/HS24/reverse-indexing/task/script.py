from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):
    index_dictionary = {}
    for idx in range(len(dataset)):
        for word in dataset[idx].split():
            word = word.lower()
            # Check if word exists, if it does, append the value, else create a new list entry
            if word in index_dictionary:
                index_dictionary[word].append(idx)

            else:
                index_dictionary[word] = [idx]

    return index_dictionary

# You can see the output of your function here
print(reverse_index(dataset))


# Your task is to write an algorithm that takes a list of strings as input and returns a dictionary, containing an index of the words to the matching strings.

# In the dictionary, each key will be a word k, while the value will be a list of indices of the input strings where the word k appears.

# Words should be treated as lowercase only. i.e. Hello and hello should be treated the same.

# You can assume that the dataset will contain only lists of strings. You don't need to check the type of the elements in the dataset.

# The string data in the dataset will be clean. This means you don't need to worry about cleaning i.e. removing punctation marks or numbers.

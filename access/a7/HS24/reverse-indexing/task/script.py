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

import pickle


example_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
pickle_out = open('dict.pickle', 'wb')
print(pickle.dump(example_dict, pickle_out))
pickle_out.close()

# to read the file
pickle_in = open("dict.pickle", 'rb')
example_dict2 = pickle.load(pickle_in)
print(example_dict2)

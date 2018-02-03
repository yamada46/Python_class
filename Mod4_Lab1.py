'''
Module 4 - Lab 1

We're going to use sets in python to analyze text.

Given the following two sentences, determine:

The number of unique words in each sentence
The number of words that appear in both sentences
The number of words that are contained in either one sentence or the other, but not in both


'''
# Here are 2 sentences,
# Pick out unique words


s1 = "For instance, on the planet Earth, man had always assumed that he was more intelligent than dolphins because he had achieved so much — the wheel, New York, wars and so on — whilst all the dolphins had ever done was muck about in the water having a good time. But conversely, the dolphins had always believed that they were far more intelligent than man — for precisely the same reasons."
set_s1 = set(s1.split(" "))
s1_num = (len(set_s1))
# print(s1_num)


s2 = "The last ever dolphin message was misinterpreted as a surprisingly sophisticated attempt to do a double-backwards-somersault through a hoop whilst whistling the ‘Star Spangled Banner’, but in fact the message was this: So long and thanks for all the fish."
set_s2 = set(s2.split(" "))
s2_num = (len(set_s2))
#print(s2_num)

print("\nThere are {} unique words in sentence s1, and {} uniques words in sentence s2. ".format(str(s1_num), str(s2_num)))

# Where the words that appear in both sentences
s1_s2_common = set_s1.intersection(set_s2)
len(s1_s2_common)
print("\nThere are {} unique words that appear in both sentences. ".format(len(s1_s2_common)))
print(s1_s2_common)


# For an extra challenge, can you figure out how to remove all the punctuation from the sentences before turning them into a set? See here (Links to an external site.)Links to an external site. for some help.


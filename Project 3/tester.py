# Function to count the number of unique words
# in the given text file.


def countUniqueWords(fileName):
    file = open(fileName, 'r')
    read_file = file.read().replace(',',' ').replace('-',' ').replace('--',' ').replace(':',' ').replace(';',' ').replace('\n', ' ').replace(".", " ").replace("?", " ").replace("!", " ").lower()
    words_in_file = read_file.split()
    count_map = {}
    for i in words_in_file:
        if i in count_map:
            count_map[i] += 1
        else:
            count_map[i] = 1
    print(count_map)
    file.close()
    return len(count_map)


# print('Number of unique words in the file are:',
#     countUniqueWords('tt2.txt'))

def cosine_similarity(vec1, vec2):
    dot_pr = 0
    for key in vec1:
        if key in vec2:
            dot_pr += vec1[key]*vec2[key]
    cos_sim = dot_pr/(norm(vec1)*norm(vec2))
    return cos_sim

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    results = []
    for i in range(len(choices)):
        if choices[i] not in semantic_descriptors or word not in semantic_descriptors or len(semantic_descriptors[word]==0):
            results.append(-1)
        else:
            vec1 = semantic_descriptors[word]
            vec2 = semantic_descriptors[choices[i]]
            results.append(similarity_fn(vec1, vec2))
    max_res = -100000
    max_ind = 0
    for i in range(len(results)):
        if results[i] > max_res:
            max_res = results[i]
            max_ind = i
    return choices[max_ind]


    # if both word and choice exist, then compute using similarity_fn and return the highest score
    # if word does not exist, all choices are -1 and return word
    # if choice does not exist, that choice gets -1 and return the highest score
    # if all choices do not exist, all choices get -1 and return word
    # if word is a dictionary with 0 values, all choices are -1 and return word

semantic_descriptors = {"hi": {"bye": 1, "trash": 1}, "bye": {"hi": 1}, "cool": {}}
print(most_similar_word("painting", ["hi", "bye", "death"], semantic_descriptors, cosine_similarity))
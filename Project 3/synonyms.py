'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 18, 2022.
'''

import math
import time


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    dot_pr = 0
    for key in vec1:
        if key in vec2:
            dot_pr += vec1[key]*vec2[key]
    cos_sim = dot_pr/(norm(vec1)*norm(vec2))
    return cos_sim

def build_semantic_descriptors(sentences):
    dict_words = {}
    for sentence in sentences:
        for j in range(len(sentence)):
            if sentence[j] not in dict_words:
                dict_words[sentence[j]] = {}
            if sentence[j] not in sentence[:j]:
                for i in range(len(sentence)):
                    if sentence[i] != sentence[j] and (sentence[i] not in sentence[:i]):
                        if sentence[i] not in dict_words[sentence[j]]:
                            dict_words[sentence[j]][sentence[i]] = 1
                        else:
                            dict_words[sentence[j]][sentence[i]] += 1
    return dict_words

def build_semantic_descriptors_from_files(filenames):
    sentences = []
    j = 0
    for i in range(len(filenames)):
        f = open(filenames[i], "r", encoding="latin1")
        sentences.append([])
        for line in f:
            for word in line.replace(',',' ').replace('-',' ').replace('--',' ').replace(':',' ').replace(';',' ').replace('\n', ' ').lower().split():
                if "." in word or "?" in word or "!" in word:
                    word = word.replace(".", " ").replace("?", " ").replace("!", " ").split()
                    for i in range(len(word)):
                        if i == 0:
                            sentences[j].append(word[i])
                            j+=1
                            sentences.append([])
                        else:
                            sentences[j].append(word[i])
                else:
                    sentences[j].append(word)
        if len(sentences[len(sentences)-1]) == 0:
            sentences.pop(len(sentences)-1)
    dict_allwords = build_semantic_descriptors(sentences)
    return dict_allwords

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    results = []
    for i in range(len(choices)):
        if choices[i] not in semantic_descriptors or word not in semantic_descriptors or len(semantic_descriptors[word]) == 0:
            results.append(-1)
        else:
            vec1 = semantic_descriptors[word]
            vec2 = semantic_descriptors[choices[i]]
            results.append(similarity_fn(vec1, vec2))
    max_res = -1
    max_ind = 0
    for i in range(len(results)):
        if results[i] > max_res:
            max_res = results[i]
            max_ind = i
    return choices[max_ind]

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    f = open(filename, "r")
    total = 0
    correct = 0
    for line in f:
        split_line = line.split()
        guess = most_similar_word(split_line[0], split_line[2:], semantic_descriptors, similarity_fn)
        if guess == split_line[1]:
            correct += 1
        total+=1
    return correct*100/total
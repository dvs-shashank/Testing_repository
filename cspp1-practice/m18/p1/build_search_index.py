'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re

# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    #temp_list1 = []
    #temp_list2 = []
    temp_list3 = temp_list2[:]
    temp_list1 = text.splitlines()
    for each_sentence in temp_list1:
        each_sentence.lower()
        temp_list2 = each_sentence.split(" ")
        re.sub("^[a-z]", "", temp_list2)
    stopwords = "stopwords.txt"
    #temp dict = {}
    for each_word in temp_list3:
        if each_word in stopwords:
            temp_list3.remove(each_word)
    return temp_list3




def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''
    # initialize a search index (an empty dictionary)
    search_index_dict = {}
    #doc_list = docs.splitlines()
    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop
    #doc_list = clean_up(doc_list)
    words_list = []
    docs_id = ()
    for i in range(len(docs)):
        if docs[i] != "\n":
            val_x = 0
            if val_x == 0:
                docs_id = docs_id+(val_x,)
            else:
                val_x += 1
                docs_id = docs_id+(val_x,)
        #doc_list = docs.splitlines()
    words_list = word_list(docs)
    for each_word in words_list:
        if each_word not in search_index_dict:
            search_index_dict[each_word] = [(docs_id, 1)]
        else:
            search_index_dict[each_word][0][1] += 1


        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    return search_index_dict

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()

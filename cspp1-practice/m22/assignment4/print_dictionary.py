'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''
import collections

def print_dictionary(dictionary):
    dictionary = collections.OrderedDict(sorted(dictionary.items()))
    print_values = ""
    for key,val in dictionary.items():
    #print(key)
        print_keys = ""
        print_keys += key
        print(print_keys,'-',val)

def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()

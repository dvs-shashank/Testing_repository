'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
import collections
def frequency_graph(dictionary):
    '''
    function for frequency graph
    '''
    dictionary = collections.OrderedDict(sorted(dictionary.items()))
    #print_values = ""
    for key, val in dictionary.items():
    #print(key)
        print_keys = ""
        print_keys += key
        print(print_keys, '-', val * '#')

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()

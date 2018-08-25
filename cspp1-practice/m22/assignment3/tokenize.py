'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    '''
    tokenise method
    '''
    token_dict = {}
    string_list = string.split(" ")
    #print(string_list)
    for each_val in string_list:
        if each_val not in token_dict:
            token_dict[each_val] = 1
        else:
            token_dict[each_val] += 1
    return token_dict

def main():
    num_lines = int(input())
    i = 1
    while i <= num_lines:
        user_input = input()
        i += 1
    print(tokenize(user_input))

if __name__ == '__main__':
    main()

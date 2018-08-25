'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    '''
    cleaning input function
    '''
    special_chars = ['!','@','#','$','%','^','&','*','(',')','_','+','.']
    string=string.replace(" ","")
    for each_char in string:
        if each_char in special_chars:
            string=string.replace(each_char,"")
    return string

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()

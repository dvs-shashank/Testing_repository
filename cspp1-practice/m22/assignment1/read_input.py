'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
	'''
	main method 
	'''
    num_lines = int(input())
    i = 1
    while (i <= num_lines):
        user_input = input()
        print(user_input)
        i += 1
    

if __name__ == '__main__':
    main()

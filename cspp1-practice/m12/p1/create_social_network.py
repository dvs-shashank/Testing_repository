'''
    Assignment-1 Create Social Network
'''
def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    var_list = data.splitlines()
    var_dict = {}
    temp = []
    for i in range(len(var_list)):
        var_list1 = var_list[i].split()
        if var_list1[1] == 'follows':
            if var_list1[0] not in var_dict:
                var_dict[var_list1[0]] = [var_list1[2]]
            else:
                if var_list1[2] not in var_dict[var_list1[0]]:
                    var_dict[var_list1[0]].append(var_list1[2])
    for i in  var_dict:
        temp = var_dict[i]
        str1 = ''.join(temp)
        str2 = str1.split(",")
        var_dict[i] = str2
    return var_dict

def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(string))

if __name__ == "__main__":
    main()

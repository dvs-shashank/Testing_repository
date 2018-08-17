'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
def get_freq_dictionary(doc1_list,doc2_list):
	'''
	calcualtes and returns frequency dictionary
	'''
	freq_dict = {}
	for each_word in doc1_list:
		if each_word not in freq_dict:
			freq_dict[each_word] = [1,0]
		else:
			freq_dict[each_word][0] += 1
	for each_word in doc2_list:
		if each_word not in freq_dict:
			freq_dict[each_word] = [0,1]
		else:
			freq_dict[each_word][1] += 1
	return freq_dict

def compute_score(freq_dict):
	'''
	calculates the score and returns
	'''
	cal_num = 0
	cal_denom1 = 0
	cal_denom2 = 0 
	cal_denum = 0
	for key in freq_dict:
		freq_list = freq_dict[key]
		cal_num += (freq_list[0] * freq_list[1])
		cal_denom1 += freq_list[0] ** 2
		cal_denom2 +=  freq_list[1] ** 2
	cal_denum = math.sqrt(cal_denom1) * math.sqrt(cal_denom2)
	return cal_num / cal_denum

def remove_stop_words(doc_list):
	'''
	removes stop words from our lists
	'''
	stopwords = load_stopwords("stopwords.txt")
	temp_doc_list = doc_list
	for each_word in temp_doc_list:
		if each_word in stopwords:
			doc_list.remove(each_word)
	return doc_list

def clean_up(D1):
	'''
	removes unnecessary characters
	'''
	D1 = D1.lower()
	data_list = D1.split()
	count = 0
	while count < len(data_list):
		data_list[count] = re.sub("[^a-z]","",data_list[count])
		count += 1
	return data_list

def similarity(doc1, doc2):
    '''
        Compute the document distance as given in the PDF
    '''
    doc1_list = clean_up(doc1)
    doc2_list = clean_up(doc2)
    doc1_list = remove_stop_words(doc2_list)
    doc2_list = remove_stop_words(doc1_list)
    freq_dict = get_freq_dictionary(doc1_list,doc2_list)
    final_score = compute_score(freq_dict)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()

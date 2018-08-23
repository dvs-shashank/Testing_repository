#define the simple_divide function here
def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   return item / denom

    

def main():
	data = raw_input()
	l=data.split()
	l1=[]
	for j in l:
		l1.append(float(j))
	s=raw_input()
	index=int(s)
	print fancy_divide(l1,index)
	

if __name__== "__main__":
	main()

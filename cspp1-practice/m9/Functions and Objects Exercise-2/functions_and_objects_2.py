#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]

def inc(val):
    val+=1
    return val

def apply_to_each(L, f):
	for i in range (len(L)):
		L[i]=f(L[i])
	print(L)

def main():
    data = input()
    data = data.split(",")
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, inc)

if __name__ == "__main__":
    main()

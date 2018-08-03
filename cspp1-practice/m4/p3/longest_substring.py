str = input()
start = 0
end = 0
count = 0
x = 0
temp = x
flag = 0
while x < (len(str)-1):
	y = x + 1
	if(str[x] > str[y]):
		flag = 1
	if y == (len(str) - 1):
			y += 1
	if (x == (len(str)-2) and count < (y-temp)):
		flag = 1
	if flag == 1:
		if count < (y-temp):
			start = temp
			end = y
			count = end - start
		temp = x + 1
		flag = 0
	x = x + 1
print(str[start:end])

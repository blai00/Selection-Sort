import random
my_array = random.sample(xrange(0,10000),5)
def selection_sort(num = []):
	for count in range(len(num)):
		min = count
		for i in range(count+1,len(num)):
			if num[i] < num[min] :
				min = i
				max = i 
		temp = num[count]
		num[count] = num[min]
		num[min] = temp 
	
		print num


selection_sort(my_array)


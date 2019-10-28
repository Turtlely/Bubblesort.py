import timeit

#code = """
def swap(ord):
	if ord[0] < ord[1]:
		return ord
	else:
		return ord[1],ord[0]

dataset = [5,4,3,2,1,9,8,6,4,5,2,10,11,24,693,3843,43282932,0]
counter = 0
flag = False
check = 0

print(dataset)

while flag==False:
	if counter < (len(dataset)-1):
		x = dataset[counter]
		y = dataset[counter+1]
		z = swap([x,y])
		dataset[counter] = z[0]
		dataset[counter+1] = z[1]
		counter+=1
	else: 
		counter = 0
	flag = all(dataset[i] <= dataset[i+1] for i in range(len(dataset)-1))

print(dataset)
#"""

#elapsed_time = timeit.timeit(code, number=100)
#print(elapsed_time)


#import timeit

#code = """
def swap(ord):
	if ord[0] < ord[1]:
		return ord
	else:
		return ord[1],ord[0]

dataset = [
#replace me with your dataset. This is of a list type.
]

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


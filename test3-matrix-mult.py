x = [[2,3,4],[2,3,4],[1,0,0],[1,0,0]]
y = [[0,1,0],[1000,100,10],[0,1,0],[1000,100,10]]
#z = [[0],[0],[0],[0]]
z = []
main_list = []
total = 0

for i in range(len(x)):
	for j in range(len(x[i])):
		total += (x[i][j] * y[i][j])
	z.append(total)
	
	if len(z) == 2: #len of 2 by 2
		main_list.append(z)
		z = []
	total = 0

print main_list
		
		

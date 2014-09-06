x=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#   0 1 2
y = [[2,3,3,2],[1,0,0,1],[2,1,1,2],[4,3,3,1]]

#list 1
t = 0
ctr = 0
for i in range(len(x)):
	for j in range(len(x[0])):
		if ctr < ((len(x) * len(x[i])) / len(y)):
			x[i][j] = y[t][j]
			ctr += 1
		
		if ctr == ((len(x) * len(x[i])) / len(y)):
			t += 1
			ctr = 0		

print x

#list 2
		
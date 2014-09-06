x=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
#   0 1 2
y = [[1,2],[4,5],[6,7]]

t = 0
ctr = 0
for i in range(len(x)):
	for j in range(len(x[0])):
		if ctr < ((len(x) * len(x[i])) / 2):
			x[i][j] = y[t][j]
			ctr += 1
		
	if ctr == ((len(x) * len(x[i])) / 2):		
		t = 0
		ctr = 0
	else:
		t += 1
print x
		
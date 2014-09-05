def convert_to_num_list(str):
	num_list = str.split(';')

	for i in range(len(num_list)):
		num_list[i] = num_list[i].split(',')
	
	for i in range(len(num_list)):
		for j in range(len(num_list[i])):
			num_list[i][j] = int(num_list[i][j])
			
	return num_list #list with integer elements

def scalar_multiplication(multiplier,num_list):
	for i in range(len(num_list)):
		for j in range(len(num_list[i])):
			num_list[i][j] = (multiplier * num_list[i][j])
	return num_list
	
def matrix_addition(list1, list2):
	sub_list = []
	sum_list = []
	if len(list1) == len(list2):
		for i in range(len(list1)):
			for j in range(len(list1[i])):
				if len(list1[i]) == len(list2[i]):
					sub_list.append(list1[i][j] + list2[i][j])
				
				if len(sub_list) == len(list1[i]):
					sum_list.append(sub_list)
					sub_list = []
	
	return sum_list

def transpose(plist):
	sub_list = []
	main_list = []
	#determine the length of the list, and its sub_list 
	
	for i in range(len(plist[0])):
		for j in range(len(plist):
			sub_list.append(0)
		main_list.append(sub_list)
		sub_list = []
		     
	for i in range(len(plist)): # 0, 1
		j = 0
		while (j < len(plist[i])):
			main_list[j][i] = plist[i][j]
			j += 1
			
	return main_list
	

def display_list(str):
	str_list = str.split(';')
	text = ""
	for i in range(len(str_list)):
		if i > 0:
			print "\n"
		for j in range (len(str_list[i])):
			if str_list[i][j] != ",":	
				print "    " + str_list[i][j] + "    ",

input = raw_input(">>")

revised_input = ""
new_list = []
for i in range(len(input)):
	if i == 0 or i == len(input) - 1:
		revised_input += ""
	else:
		revised_input += input[i]

#print matrix_addition([[1,2,3,4],[3,4,5,6]], [[3,4,5,6],[1,2,3,4]])
#print scalar_multiplication(2,[[1,2,3],[3,4,5]])
#print display_list(revised_input)
print transpose([[1,2,3],[4,5,6]])


		
		
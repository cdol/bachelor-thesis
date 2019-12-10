
arrays = open('Carrayfile','w')


arrays.write('([\n')	#open matrix
for j in range (-2, 76):			#outer loop, 2+75+1 lines
	arrays.write('[0,')		#first is bracket and 0
	arrays.write('0,')			#second is 0
	for k in range (0, 450):	#450 elements - 5x90
		if ((75+k-j)%180 < 90): #print 15 0's in first line and 90 in last line
			arrays.write('0,')
		else:
			arrays.write('1,')
	if (j < 76):
		arrays.write('0],\n')	#last is 0, bracket and newline
	else:
		arrays.write('0]\n')	#last line has no comma	
arrays.write('])')	#close matrix



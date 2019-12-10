
arrays = open('XYarrayfile','w')


arrays.write('([[-float(\'inf\'),0,')
for i in range(1, 451):	#x
	arrays.write(str(i)+'*reichweite,')
arrays.write('float(\'inf\')],\n')

arrays.write('[-float(\'inf\'),0,')
for j in range(1, 76):	#y
	arrays.write(str(j)+'*reichweite,')
arrays.write('float(\'inf\')]])')

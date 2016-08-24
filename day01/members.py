#!/usr/bin/env python
#conding=gbk

info = open('python_class_members.txt','r')
members = info.readlines()

while True:
	select = raw_input('please input select info:')
	
	if select == 'all':
		for i in members:
			print i
	
	elif '-' in select:
		x,y = select.split('-')
		for i in members[(int(x)-1):int(y)]:
			print i
			
	elif int(select) in range(1,27):
		print members[int(select)-1]
	
#	elif str(select):
#		print (select in members)
	elif select == 'q' or select == 'qiut':
		break
		
	elif select not in str(members):
		print 'your input error:'	
		
	else:
			continue

	
		
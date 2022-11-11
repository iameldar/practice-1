#!/usr/bin/python3

def sort_patch(patch):
	mapToInt = []
	mapToString = []
	for i in patch:
		mapToInt.append(list(map(int, i.split('.'))))
	mapToInt.sort(reverse=True)
	
	for i in mapToInt:
		mapToString.append('.'.join(list(map(str, i))))

	print(mapToString)




sort_patch(["3.9.5", "4.3.11", "8.1.2", "4.3.6", "4.5.6"])
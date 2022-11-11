#!/usr/bin/python3

def multiply(num_a, num_b):
	if num_a == 0 or num_b == 0:
		return 0
	return num_a + multiply(num_a, num_b - 1)
	

# 
# num_b will hit the recursive limit value at some point.
#

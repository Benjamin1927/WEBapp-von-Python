#!/usr/bin/python
# Filename: using_name.py
def ff():
	print('PI')

if __name__ == '__main__':
	print ('This program is being run by itself')
else:
	print ('I am being imported from another module')
	ff()

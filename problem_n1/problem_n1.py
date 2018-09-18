from bs4 import BeautifulSoup
import requests

def func(num):
	sum1 = ""

	for i in range(len(num)-1):
		if num[i] == num[i+1]:
			sum1 += (num[i])
	if num[-1] == num[0]:
		sum1 += (num[-1])
	print(sum(int(i) for i in sum1))

with open("/home/deanm/Documents/python\
_files/AdventOfCode2017/problem_n1.html",'r') as num_file:
	func(num_file.read()) 




#!/usr/bin/python3.4
#encoding:utf-8
import math
number1=input()
nu=int(number1)
h = 0
n = 2
while n <= nu:
   flag = 1
   i = 2
   while i <= math.sqrt(n):
       if n % i == 0:
           flag = 0
           break
       i=i+1
   if flag :
       print ('num: ',n)
       h = h + 1
   n = n+1           
print ('total: ',h)

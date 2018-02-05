x=int(raw_input())
f=1
while(x>0):
  for i in range(1,x+1):
	  f=f*i
	  x=x-1
  print f

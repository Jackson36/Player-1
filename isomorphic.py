x=raw_input()
y=raw_input()
z=0
t=0
if(len(x)==len(y)):
  for i in range(0,len(x)-1,1):
     if(x[i]==x[i+1]):
     	z=z+1
     if(y[i]==y[i+1]):
     	t=t+1
     if(z!=y):
     	print no
     	break
  if(z==t):
     print yes
else:
     print no

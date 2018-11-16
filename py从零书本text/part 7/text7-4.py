def exp(p1,p2,p3=0,*a,**b):
	print('p1=',p1,'p2=',p2,'p3=',p3,'a=',a,'b=',b)
exp(1,2)
exp(1,2,3)
exp(1,2,y=5)
exp(1,2,'a','b')
exp(1,2,3,'a')
exp(1,2,3,'ab','c',y=5,x=6)
print('\n')
args=(1,2,3,'b')
kw={'x':8,'y':'9','z':'10'}
exp(*args,**kw)
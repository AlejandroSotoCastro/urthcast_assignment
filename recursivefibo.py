de




f fibo(n):#Using recursive functions.
	if n==0:
		return(0)
	if n==1:
		return(1)# 0 and 1 are the "initial conditions" 
	else:#adding all the simpler solutions.
		return(fibo(n-1)+fibo(n-2))

print(fibo(6))#tring out with different values of n

print "Factorial code"
def fact(n):
    if n==1:
        return 1
    else:
        m=n
        f=1
	for i in range(1,m+1):
	    f*=i
	return f
	
o=raw_input("Enter a positive number")
print fact(int(o))
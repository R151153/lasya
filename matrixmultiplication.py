r1=input("enter no. of rows of matrix 1:")
c1=input("enter no. of columns of matrix 1:")
r2=input("enter no. of rows of matrix 2:")
c2=input("enter no. of columns of matrix 2:")
if(c1==r2):
	i=0
	a={}
	while(i<r1):
		j=0
		while(j<c1):
			m1=input("enter matrix1 elements:")
			a[i,j]=m1
			j=j+1
		i=i+1
	b={}
	i=0
	while(i<r2):
			j=0
			while(j<c2):
				m2=input("enter matrix2 elements:")
				b[i,j]=m2
				j=j+1
			i=i+1
	c={}
	i=0
	while(i<r1):
			j=0
			while(j<c2):
				c[i,j]=0
				k=0
				while(k<r2):
					c[i,j]=c[i,j]+a[i,k]*b[k,j]
					k=k+1
				j=j+1
			i=i+1
	i=0
	while(i<r1):
			j=0
			while(j<c2):
				print c[i,j]
				j=j+1
			i=i+1



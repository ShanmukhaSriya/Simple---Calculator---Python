def add (n1,n2):
	return n1+n2
def subtract (n1,n2):
	return n1-n2
def multiply (n1,n2):
	return n1*n2
def divide (n1,n2):
	return n1/n2
print('simple calculator')
print('-----------------')
print('choose an operation: \n' \
       '1.Add \n'\
	   '2.Subract\n' \
	   '3.Multiply\n' \
	   '4.Divide\n' \
	   '5.Quit\n' )
select = int(input('Enter the operation: 1,2,3,4,5 \n'))
n1 = int(input('Enter first number:'))
n2 = int(input('Enter second number:'))
if select == 1:
	print(n1,'+',n2,'=',add(n1,n2))
elif select == 2:
	print(n1,'-',n2,'=',subtract(n1,n2))
elif select == 3:
	print(n1,'*',n2,'=',multiply(n1,n2))
elif select == 4:
	print(n1,'/',n2,'=',divide(n1,n2))
else:
	print('******Quit******')
	

# using of for loop
for i in range (1,10):
    print (i)

#multiple table using loop
num= int (input ("enter your number"))
for i in range (1,11):
    print (num,"*",i,"=",num*i)

#using if and else
age =19
if age>=18:
    print (f"you are an adult")
else :
    print ("you are minor")  
 
 
#using if else  login
username ="admin "
password ="12345" 

input_username =input ("enter username")
input_password=input ("enter password")

if username==input_username:
    if password ==input_password:
        print (f" successfully login")
    else :
        print (f" username and password invalid")
else :
    print ( f"login failed")   
    
 
#arithmetic rule
num=-4
if num>0:
    print (f"it is positive number")
elif num==0:
    print (f"it is zero number") 
else:
    print (f" it is negative number")   
    
    
#print maximum 
a=int(input(" enter a number 1:"))    
b=int(input("enter a number 2:")) 
c=int(input("enter a number:"))
if a<=b>=c:
    print (f"b")
elif b<=a>=c:
    print (f"a")  
else:
    print (f"c")   
    
#using range identify prime number
n=int(input("enter a number"))

if n<2:
    print (f" not a prime number")
else:
    for i in range (2,n):
        if n%i==0:
            print (f" not a prime number")
            
            break
    else :
        print (f" number is prime")
        
        
#if else elif 
year =int(input("enter a year"))    
if year %400==0:
    print (f"leap year")     
elif year %4==0 and year %100!=0:
    print (f"leap year")
else: print (f"not leap year")   


num1=int(input("enter a number 1:"))
num2=int(input("enter a number 2:"))
if num1==num2:
    print ("number are equal")
elif num1>num2:
    print ("num1")  
else :
    print (" num2") 
    
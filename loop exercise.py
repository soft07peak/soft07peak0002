#using if else identify odd and even
num=int(input("enter a num:"))
if num%2==0:
    print (f"even")
else :
    print (f"odd")
    
    
#for in range sum  square

sum_squares=0
for i in range (1,5):
    sum_squares +=i** 2
print ("sum of squares:", sum_squares)


#for loop
sentence =input ("enter a string:")
vowel_count=0
vowel ="aeiou"
for i in sentence: 
    if i in vowel:
         vowel_count=vowel_count+1
print("total vowel_count:", vowel_count) 

#palindrome num
i=int(input(" enter a num:"))
rev=0
x=i
while (i>0):
    rev=(rev*10)+i%10
    i=i//10
if (x==rev):
    print ("palindrome num")  
else:
    print ("not palindrome")  
    

#using while loop
i=int(input("enter num:"))  
rev=0

while (i>0):
    rev=(rev*10)+i%10
    i=i//10
print("reverse=",rev)   


#using while loop
num=int(input("enter a num:"))
sum=0
while (num>0):
    sum+=num
    num-=1
    print (" the result is", sum)
    
# using for loop
num=int(input("enter num:"))  
fact=1
for i in range(1,num+1) :
    fact=fact* i
print ("factorial num is :",fact)  



#if else and for loop
a=int(input("enter a num:")) 
a1,a2=0,1
sum=0
if a<=0:
    print ("please enter number greater than 0:")
else:
    for i in range (0,a) :
        print ( sum ,end=" ")
        a1=a2
        a2=sum
        sum=a1+a2


#names
names =["Esha", "Ayesha","Areeba","Rubab","saba:"]   
for i in range (3,4):
    print ( names[i])
    
    
#grades assigning 
marks=int(input("enter a marks:"))
if marks>=180:
    print ("A grade")
elif marks>=100:
    print ("B grade")   
elif marks>=80:
    print("C grade")   
elif marks>=50:
    print ("D grade")    
else:
    print ("F grade")   
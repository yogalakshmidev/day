#print 2 table using for loop
#for i in range(1,11):
#   print(i,"x 2  = ",i*2)

# print 3 table using for loop
#for i in range(1,11):
#   print(i, "x2=" , i*3)


#Get input for num 8 and 15, print the number between 8 and 15
#a = int(input("Enter the first number for range"))
#b = int(input("Enter the second number for range"))
#for i in range(a,b):
#    print(i+1)


#Print the even number between 1 to 10 and count the total number of even no within that
#print the odd number between 1 to 10 and count the tot no of odd no in it
#Count the number which are divisible by 3 and 5. Range 1 to 100
count = 0;
oddCount = 0;
totalCount = 0;
a= int(input())
b= int(input())
if(a==1 and b == 100):
    c=b+1;
    for i in range(a,c):
        if(i%3 ==0 and i%5 == 0):
            totalCount=totalCount +1;
    print("Total number of counts for the no divide by 3 and 5 is",totalCount);
else:
    for i in range(1,11):
    
        if (i%2== 0 ):
            print (i)
            count = count +1;
    print("Even number between ",a, "and",b ,"is",count)


    for j in range(1,11):
         if(j%2 != 0):
            print(j)
            oddCount = oddCount + 1;
    print("Odd number between ",a ,"and",b ,"is",oddCount)


#Print the number  1 to 5 using while loop

##i=1
##while(i<6):
##    print(i)
##    i+=1


#Write the looping stmt to print 10,20,30,40,50,60,......200

##i=10
##j=210
##while(i<j):
##    print(i);#to print in the next line
##    print(i,end=",")#to print in the same line seperated by comma
##    i=i+10

#write the program to print the first 10 natual numbers in reverse order

##i = 10
##while(i>0):
##      print(i, end=",")
##      i=i-1


#Write the program to find the factorial of the n number

##i=int(input("Enter the number to find the factorial : "))
##fact=1
##while(i>0):
##    fact *=i
##    i -= 1#i=i-1
##print(fact)



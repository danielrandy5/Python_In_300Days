#Day 1: setting up python, python on cli #!/bin/env phython 3.7
#completion Date: May 7th 2021

print (" randy" + str(4) )
print(" this\n\t is \n ot")

print(22 // 8) #remender
print (2 ** 3) #exponent

#print( "you can add a string with a number:" + 42) Unless you add str()
print("you can add a string to a number: " + str(42))
print("this is also {}  and + {}".format("zizi","sisi"))
print("this is good {} \n\t but will only {} work here" .format("okay","didi5")) #tab with formating
## fomarting with {} {} .format("1st","2") will work. you cam also use

print(" this will work if i make this ")
print("{1} {0}".format(3,4)) # this will call in an array form

print("\"this is a qoute \"")
print( """ this is 
 a block""" ) ## this ia block text

print("my name is randy\n" * 5) #Using * to repeat a line
print(r"my name is randy") #Using r to print raw string
print (1==1) # return a true or false Boolean
print (1==2) #equal to
print (1!=2) #not equal to
print (1 > 2)
print ( 1< 2)
print (1 <= 2)
print (1 >= 2)

print( "yes" or "No")
print("Why" and "Okay\n")


##Day 1 Assginment
#Ask for your name,count and print out

print("\"Hello Welcome\"""\nPlease enter your name:")
myName=input()

print("\nThank you {}".format(myName))
print("this lent of your name is:")
print(len(myName)) ## len counts the number of aphabets
print("how old are you " + myName)
Age=input()
print ("you'll be " + str(int(Age) + 5) + " in  in 5 yrs time")
print ( len("my day is are numbered")) # len
print ( str(10)) # str change an integer into a string
print(round(10.5)) #rounds to the nearing number
print(float(10.10)) #print the same number
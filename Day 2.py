#Day 2: String formatting
#completion Date:

cheers = "where everybody knows YOUR  name "
print(cheers.capitalize()) #Capitalizes what need to be capitalzed
print(cheers.title()) #Capitalizes the first leter of a word
print(cheers.lower()) #changes everything to a lowercase
print(cheers.upper()) #changes every word to upercase
print("this CAN also Work".upper()) #this can also work with everything

## Precision and format
i = 13
print('{0:2} square is {1:20}.'.format(i, i ** 2)) ## the 2 and 20 is for Width i.e /
#  {position:width}

### < for the left position and > for the right ^ middle
print ('{0:1} squared is {1:<4}.'.format(i,i ** 2))
print ('{0:1} squared is {1:>4}.'.format(i,i ** 2))
print ('{0:1} squared is {1:^4}.'.format(i,i ** 2))


msg = "END OF CODE"
print("{:=^50}".format(msg)) ## prints out end of line

print ("{:.6}".format(cheers.capitalize()))

lines = [1,2,3,5]
write = []
write.append(" this is the first line")
write.append("this is th 2nd line")
write.append("this is the third line")
print(write)
print(lines.index(5))

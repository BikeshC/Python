print "Program to reverse a number"
input = input("Enter an integer: ")
if type(input) != int:
	exit("You did not enter an integer!!!")
input = str(input)
l = len(input)
output=""
for i in range(1,l+1):
	output += input[-i]
print int(output)
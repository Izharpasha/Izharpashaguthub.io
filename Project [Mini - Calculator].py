First = input("Enter Your Number :")
operator = input("Choose Your Operator ( +,-,*,/,%) :")
Second = input("Enter Your Number :")

First = int(First)
Second = int(Second)

if operator == "+" :
		print(First + Second)
elif operator == "-" :
		print(First - Second)
elif operator == "*" :
		print(First * Second)
elif operator == "/" :
		print(First / Second)
elif operator == "%" :
		print(First % Second)

else:
		print("Invalid Syntax")
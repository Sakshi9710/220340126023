try: 
	num = int(input("Enter the number: "))
	print(num**2)
except EOFError as e:
    print(end="")

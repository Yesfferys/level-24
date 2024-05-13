import os

"""
This program creates a matrix with the data you input: rows, columns, and values for each element.
"""

def prompt_option_number():
	"""
	It doesn't take any arguments, prompts the user for an option among three previously given options, 
	and returns the chosen option in INTEGER format.
	"""
	option = input("Choose an option (1 , 2 o 3): ")
	while option not in ("1","2","3"):
	   	option = input("Please, Choose an option again (1 , 2 o 3): ")
	return int(option)

def prompt_option():
	"""
	it doesn't take any arguments,promts the user one option among ´Yes´ or ´no´ previusly given options,
	and returns the shosen option
	"""
	while True:
		option = input("Please, input 'yes' o 'no': ").lower()
		if option == "yes" or option == "no":
			return option
		else:
			print("invalid option. Please, input 'yes' o 'no'.")

def continue_program():
	"""
	Reduce the code when interacting with the user, without accepting any parameters as arguments."
	"""
	continue_program=input("Press ENTER to continue")
	os.system("cls")

def presentation():
	"""
	Show the program's presentation, it does not take any parameters, returns the options for the user to choose from
	"""
	print("--------------------------------------------------------------------------------------")
	print("----------------------------- let's built a matriz   ---------------------------------")
	print("--------------------------------------------------------------------------------------")
	print("----------------------------- 1. Built matriz        ---------------------------------")
	print("----------------------------- 2. show matriz         ---------------------------------")
	print("----------------------------- 3. exit of systems     ---------------------------------")
	print("--------------------------------------------------------------------------------------")


def built_matriz():
	try:
		rows=int(input("Please, ENTER any number of ROWS to built the matriz: "))
		columns=int(input("please, ENTER any number of COLUMNS to built the matriz: "))
	except ValueError:
		print("You have not enter an integer number")
	else:
		matriz=[]
		for i in range(rows):
			matriz.append([])
			for j in range(columns):
				matriz[i].append(0)

		for row in range(len(matriz)):
			for element in range(len(matriz[row])):
				print(f'input value to rows number:',row+1,'column:',element+1)
				value=int(input("Input value: "))
				matriz[row][element]=value
		return matriz

def show_matriz(matriz):
	for row in range(len(matriz)):
		print("[", end= " ")
		for column in range(len(matriz[row])):
			print(matriz[row][column], end= " ")
		print("]")


################################################   program  flow  #########################################################

matriz=None
while True:
	presentation()
	print()
	option=prompt_option_number()
	
	
	if matriz==None and option==1:
		print("let's go built a matriz")
		matriz=built_matriz()
		continue_program()
		continue
	elif matriz!=None and option==1:
		print("You already have a matriz built, You want to rewrite the existing one?")
		rewrite=prompt_option()

		if rewrite=="yes":
			matriz=built_matriz()
			continue_program()
			continue
		elif rewrite=="no":
			os.system("cls")
			continue

	elif option==2 and matriz==None:
	 	print("you must create a matriz")
	 	continue_program()
	 	continue

	elif option==2 and matriz!=None:
		print("The matriz is: ")
		show_matriz(matriz)
		continue_program()
		continue

	elif option==3:
		print("End of program")
		break



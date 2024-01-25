# We are going to create cypher text using ASCII values
user_input = input("Enter a message to encrypt: ")

# we are going to create a class called Cypher so we can use it to encrypt
class Cypher:
	
	# This function will take the user input and convert it to ASCII values
	def convert_to_ascii(user_input):
		ascii_list = [] # We are going to use this to store the values in the ASCII 
		for i in user_input:# We are going to use a for loop to go throught each letter the user input 
			ascii_list.append(ord(i))# we are going to use this to add the value to the list and what the number is going to be 
		return ascii_list# This is going to return the acsii list when we call it 

	# This function will take the ASCII values and convert them to characters
	def convert_to_char(ascii_list):
		char_list = []# we are going to make a list to save our progress inside 
		for i in ascii_list:# we are going to create a list for every letter in the code 
			char_list.append(chr(i))# this code we are going to add(.append) the chracter to the list that we created to stay organized 
		return char_list# this will return the list we created and saved the values in

	# This function will take the ASCII values and shift them by 10 places to the right
	def shift(ascii_list): # we are to use this function to be able to shift the values by 10 places
		shift_list = []# Here we are gonna save it in a list so we can use it later
		for i in ascii_list: # we are going to use a loop here to go through each character in the code 
			shift_list.append(i + 10) # as soon as we get a letter then we are going to add a 10 to it 
		return shift_list # this will return the list we created and saved the values in

# In this code we are going to call the function we created and additionally we are going to print the encrypted message
# The cypher text comes from the class we created so in order to use the class we are going to call it everytime we want to use what is inside the class
# the reason why we are going to add a . after the class is because we are going to use the function inside the class
# the reason why also is added everythign together instead of having it seperate it to make the code more cleaner and more organized
print(Cypher.convert_to_char(Cypher.shift(Cypher.convert_to_ascii(user_input)))) 


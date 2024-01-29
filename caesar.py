# We are going to create cypher text using ASCII values
# We are also going to create a text to be decrypted
user_input = input("Enter a message to encrypt: ")
user_decrypt = input("Enter a message to decrypt: ")


#We are going to create a class called Cypher so we can use it to encrypt
class Cypher:
	
#This function will take the user input and convert it to ASCII values
	def convert_to_ascii(user_input):
		ascii_list = [] 
		for i in user_input:
			ascii_list.append(ord(i))
		return ascii_list

#This function will take the ASCII values and convert them to characters
	def convert_to_char(ascii_list):
		char_list = ""
		for i in ascii_list:
			char_list += (chr(i))
		return char_list

#This function will take the ASCII values and shift them by 10 places to the right
	def shift(ascii_list):
		shift_list = []
		for i in ascii_list:
			if i == 32:
				shift_list.append(i)
				continue # The reason for this is to make sure the code does not shift the space
			shifted = i + 10
			if shifted > 122:  #This will loop around for lowercase letters
				shifted -= 26
			elif shifted > 90 and i < 91:  #This will loop around for uppercase letters
				shifted -= 26
			shift_list.append(shifted)
		return shift_list 
	
# This Function will take the ASCII values and shift them by 10 places to the left(back to normal) Just copy and paste from
# The code above and just remove the shift + 10 
	def unshift(ascii_list):
		unshift_list = []
		for i in ascii_list:
			if i == 32:
				unshift_list.append(i)
				continue
			unshifted = i - 10
			if unshifted < 97 and i > 96:  #This will loop around for lowercase letters
				unshifted += 26
			elif unshifted < 65:  #This will loop around for uppercase letters
				unshifted += 26
			unshift_list.append(unshifted)
		return unshift_list
	

# In this code we are going to call the function we created and additionally we are going to print the encrypted message
# The Cypher text comes from the class we created so in order to use the class we are going to call it everytime we want to use what is inside the class
# reason why we are going to add a . after the class is because we are going to use the function inside the class
# the reason why also is added everythign together instead of having it seperate it to make the code more cleaner and more organized
# We are also going to ask the user to input a message to decrypt
	
#In this code we are going to call the function we created. This will help use stay organize and clean 
# We call that chaining functions.(We are calling the class(Cypher)within a function by using a .)
	
encrypted_message = Cypher.convert_to_char(Cypher.shift(Cypher.convert_to_ascii(user_input)))
print(f"Encrypted message: {encrypted_message}")

# We are going to call the function we created to decrypt the message
#we are also chaining so we do not make a mess of the code.

decryption =Cypher.convert_to_char(Cypher.unshift(Cypher.convert_to_ascii(user_decrypt)))
print(f"Decrypted message: {decryption}")
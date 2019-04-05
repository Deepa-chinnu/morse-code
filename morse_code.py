def encode(message):
# Function that encodes your string

	morse_code = {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--..",
	"0": "-----",
	"1": ".----",
	"2": "..---",
	"3": "...--",
	"4": "....-",
	"5": ".....",
	"6": "-....",
	"7": "--...",
	"8": "---..",
	"9": "----.",
	" ": "(space)"
	}
# Dictonary with all caracters/numbers to morse code

	message = message.upper()
	encoded_msg = ""
# Makes you massage in all CAPS, and creates an empy string

	for x in message:
		encoded_msg = encoded_msg + morse_code[x] + " "
# Takes your message imput and turns it into morse code

	return encoded_msg
# Returns the morse code

def decode(secret):
# Function that decodes your string

	morse_code_decode = {
	".-": "A",
	"-...": "B",
	"-.-.": "C",
	"-..": "D",
	".": "E",
	"..-.": "F",
	"--.": "G",
	"....": "H",
	"..": "I",
	".---": "J",
	"-.-": "K",
	".-..": "L",
	"--": "M",
	"-.": "N",
	"---": "O",
	".--.": "P",
	"--.-": "Q",
	".-.": "R",
	"...": "S",
	"-": "T",
	"..-": "U",
	"...-": "V",
	".--": "W",
	"-..-": "X",
	"-.--": "Y",
	"--..": "Z",
	"-----": "0",
	".----": "1",
	"..---": "2",
	"...--": "3",
	"....-": "4",
	".....": "5",
	"-....": "6",
	"--...": "7",
	"---..": "8",
	"----.": "9",
	"(space)": " "
	}
# Dictonary for decoding morse code

	secret = secret.split(" ")
# Splites the morse code at every space

	decoded_msg = ""
# Creates a empy string

	try:
		for x in secret:
			decoded_msg = decoded_msg + morse_code_decode[x]
	except KeyError:
		pass
# Takes the morse code from the dir and turns it into caracters or numbers

	decoded_msg = decoded_msg.title()
# Makes the decoded word display in title

	return decoded_msg
# Returns a decoded message

if __name__ == "__main__":
# Execute test-program if started from original file

	secret = encode("Hello World")
	nosecret = decode(secret)
# Defines secret as the string with the morse code

	print("Hello World = " + secret + "\n")
	print(secret + "= " + nosecret)
	print('\nTo import this to your own python project do "from morse_code import *"')
# Prints the morse code and instructions

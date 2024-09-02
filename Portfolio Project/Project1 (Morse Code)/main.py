#Storing the Morse code values for particular letters
storage = {
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9': '----.',
    '0' : '-----'
}

# taking user input
sentence = input("Enter the sentence: ")

# converting it to upper case and then accessing each letter
sentence = sentence.upper()
answer = ""

for letter in sentence:
    if (letter in storage):
        answer += storage.get(letter)
        answer += " "
    else:
        answer += "       "

print(f"Your Morse Code for the string is: {answer}")
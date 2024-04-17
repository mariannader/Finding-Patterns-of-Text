#Finding Patterns of Text Without Regular Expression
# from Automate the Boring Stuff with Python Book
# check if the string is a phone number
# US format 415-555-4242
def isPhoneNumber(text):
    # if the string len is not == 12 so it is not a number
    if len(text) != 12:
        return False
    
    # for loop for the first 3 digits (0.1.2)
    for i in range(0,3):
        #check if any is not a decimal
        if not text[i].isdecimal():
            return False
        
    # in US every 3 numbers saperated by - (hyphen)
    if text[3] and text[7] != '-':
        return False
    
    # check for the other numbers
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    # if the string pass all cases so it ture
    return True

print("Test the US Phone Number Format Function")
print(isPhoneNumber("415-555-4242 is a phone numbe?")) #False
print(isPhoneNumber('415-555-4242')) #True
print(isPhoneNumber('Moshi moshi')) # False
print("\n")

#---------------------------------
def isEGPhoneNumber(text):
    textNoSpace = []
    for i in range(len(text)):
        if text[i] == ' ':
            continue
        textNoSpace.append(text[i])

    # if the string len is not == 13 so it is not a number
    if len(textNoSpace)!= 11:
        return False
    #check for the company code
    if (textNoSpace[0] == '0' and textNoSpace[1] == '1' and (textNoSpace[2] == '0' or textNoSpace[2] == '1' or textNoSpace[2] == '2' or textNoSpace[2] == '5')):
        # for loop for check all is decimals
        for i in range(3, 11):
            if not textNoSpace[i].isdigit():
                return False
        return True
    else:
        return False


print("Test the EG Phone Number Format Function")
print(isEGPhoneNumber('01209003899')) #True
print(isEGPhoneNumber('01551234567')) #True
print(isEGPhoneNumber('is the a number 01203066936')) #False
print("\n")

#----------------------------------------

# Enter a massage and extract the phone number from 

message = "Call me at 01209003899 tomorrow. 01551234567 is my office."

for i in range(len(message)):
     chunk = message[i:i+11]
     if isEGPhoneNumber(chunk):
         print('EG Phone number found: ' + chunk)
print('Done Finding')

# While the string in message is short in this example, it could be millions 
# of characters long and the program would still run in less than a second. A 
# similar program that finds phone numbers using regular expressions would 
# also run in less than a second, but regular expressions make it quicker to 
# write these programs.


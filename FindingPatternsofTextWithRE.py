#Finding Patterns of Text With Regular Expression
# Remember \d is a digit character, \d\d\d-\d\d\d-\d\d\d\d is the regular expression for a phone number pattern  415-555-4242.
import re

massage = '415-555-4242 is my number.'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
result=phoneNumRegex.search(massage)
print("number found : " + result.group())


# Matching Multiple Groups with the Pipe Symbol |
massage = '0102 456 2345 is my number.'
EGphoneNumRegex = re.compile(r'\d\d\d\d \d\d\d \d\d\d\d')
result=EGphoneNumRegex.search(massage)
print("EG number found : " + result.group())


#  Writing mo.group() inside our print 
# statement displays the whole match, 415-555-4242.

#  phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#  >>> mo = phoneNumRegex.search('My number is 415-555-4242.')
# >>> mo.group(1)
#  '415'
#  >>> mo.group(2)
#  '555-4242'
#  >>> mo.group(0)
#  '415-555-4242'
#  >>> mo.group()
#  '415-555-4242'
# >>> mo.groups()
#  ('415', '555-4242')
#  >>> areaCode, mainNumber = mo.groups()
#  >>> print(areaCode)
#  415
#  >>> print(mainNumber)
#  555-4242
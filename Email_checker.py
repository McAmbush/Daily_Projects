print(20*'=')
print('Welcome to email checker!!')
print(20*'=')
import re
str = input('Enter your email: ')
pattern = r'([\w\.-]+)@([\w\.-]+)([\w\.]+)'
match = re.search(pattern,str)
if match:
    print('Your email is correct!\nYour email is:'+match.group())
else:
    print('Invalid Email!!')

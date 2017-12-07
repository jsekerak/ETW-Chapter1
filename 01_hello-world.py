Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> hello
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> 1+1
2
>>> 3**2
9
>>> print (Hello World)
SyntaxError: invalid syntax
>>> 

>>> Print ('Hello World')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    Print ('Hello World')
NameError: name 'Print' is not defined
>>> num = 2
>>> type (num)
<class 'int'>
>>> num = 'now I am a string'
>>> type (num)
<class 'str'>
>>> 

>>> type(98)
<class 'int'>
>>> type (98.0)
<class 'float'>
>>> type (True)
<class 'bool'>
>>> type (true)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    type (true)
NameError: name 'true' is not defined
>>> type (True)
<class 'bool'>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> 1>2
False
>>> 1!=1
False
>>> 1>=1
True
>>> 1==1
True
>>> x=3
>>> x*5
15
>>> "Cisco"*x
'CiscoCiscoCisco'
>>> str1="Cisco"
>>> str2"Networking"
SyntaxError: invalid syntax
>>> str2="Networking"
>>> str3="Academy"
>>> space = " "
>>> print (str1 + space + str2 + space + str3)
Cisco Networking Academy
>>> cls
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> clr
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    clr
NameError: name 'clr' is not defined
>>> "cls"
'cls'
>>> ?
SyntaxError: invalid syntax
>>> type "str1)
SyntaxError: EOL while scanning string literal
>>> print (str(str1) + space +str2)
Cisco Networking
>>> str1 = 1.0
>>> hostnames = ["R1", "R2", "R3", "R4"]
>>> type (hostnames)
<class 'list'>
>>> len(hostnames)
4
>>> hostnames
['R1', 'R2', 'R3', 'R4']
>>> hostnames[0]
'R1'
>>> hostnames[-1]
'R4'
>>> hostnames[0] = "rtr1
SyntaxError: EOL while scanning string literal
>>> hostnames
['R1', 'R2', 'R3', 'R4']
>>> hostnames[2]
'R3'
>>> hostnames[3]
'R4'
>>> ipAddress = {"R1":"10.1.1.1", "R2":"10.2.2.2", "R3":"10.3.3.3"}
>>> ipaddress
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    ipaddress
NameError: name 'ipaddress' is not defined
>>> ip
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    ip
NameError: name 'ip' is not defined
>>> ipAddress
{'R1': '10.1.1.1', 'R2': '10.2.2.2', 'R3': '10.3.3.3'}
>>> ipAddress['R1']
'10.1.1.1'
>>> ipAddress ['R1'] = '10.1.1.3'
>>> ipAddress
{'R1': '10.1.1.3', 'R2': '10.2.2.2', 'R3': '10.3.3.3'}
>>> ipaddress
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    ipaddress
NameError: name 'ipaddress' is not defined
>>> 'R3' in ipAddress
True
>>> 'R4' in ipAddress
False
>>> 
====== RESTART: C:\Users\attc-249-20\emerging-tech-ch1\02_list-dicts.py ======
country
capitals
Traceback (most recent call last):
  File "C:\Users\attc-249-20\emerging-tech-ch1\02_list-dicts.py", line 20, in <module>
    print(capitals["South Africa"[1]])
KeyError: 'o'
>>> print (country)
['Brazil', 'Russia', 'India', 'China', 'South Africa']
>>> print (capitals)
{'Brazil': 'Brasilia', 'Russia': 'Moscow', 'India': 'New Delhi', 'China': 'Beijing', 'South Africa': ['Pretoria', 'Cape Town', 'Bloemfontein']}
>>> 
====== RESTART: C:\Users\attc-249-20\emerging-tech-ch1\02_list-dicts.py ======
country
capitals
Traceback (most recent call last):
  File "C:\Users\attc-249-20\emerging-tech-ch1\02_list-dicts.py", line 20, in <module>
    print(capitals["South Africa"[1]])
KeyError: 'o'
>>> firstname = input("What is your first name?")
What is your first name? Jeff
>>> print (Hello " + firstName + "1")
       
SyntaxError: invalid syntax
>>> 
== RESTART: C:\Users\attc-249-20\emerging-tech-ch1\03_personal-info_sol.py ==
What is your first name? Jeff
What is your last name? S
What is your location? Cleveland
What is your age? 50
Hi Jeff S! Your location is Cleveland and you are 50 years old.
>>> 
>>> 
====== RESTART: C:/Users/attc-249-20/emerging-tech-ch1/05_if-ACL_sol.py ======
What is the IPv4 ACL Number?2000
This is not a standard or extended IPv4 ACL.
>>> devices = ["R1", "R2", "R3", "R4"]
>>> 
====== RESTART: C:/Users/attc-249-20/emerging-tech-ch1/05_if-ACL_sol.py ======
What is the IPv4 ACL Number?
Traceback (most recent call last):
  File "C:/Users/attc-249-20/emerging-tech-ch1/05_if-ACL_sol.py", line 1, in <module>
    aclNum = int(input("What is the IPv4 ACL Number?"))
ValueError: invalid literal for int() with base 10: ''
>>> for item in devices:
	print(item)
	

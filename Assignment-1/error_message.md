# Error message

## Script 1
```
SyntaxError: '(' was never closed
```
##### Syntax error as one of the open parantheses '(' is not closed with ')'
##### *Code fix :*
```
print("This is a simple test")
print("Oha, it does not work.")
```
## Script 2
```
NameError: name 'gravitational_acceleration' is not defined
```
##### There is an undeclared variable 'gravitational_acceleration' that we are trying to use. Define the variable to fix the error.
##### *Code fix :*
```
mass_in_kg = 10
gravitational_acceleration = 2

force = mass_in_kg * gravitational_acceleration

print(f"{mass_in_kg} get's accelerated with a force of {force} on earth.")
```
## Script 3
```
ModuleNotFoundError: No module named 'Math'
```
##### The name of the library imported is incorrect. Correct module name 'math'
##### *Code fix :*
```
from math import sqrt

a = 9
print(f"The square root of {a} is {sqrt(a)}.")
```
## Script 4
```
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```
##### The parameters to print() functions must be passed within the parantheses.
##### *Code fix :*
```
print ("Let's run some legacy code...")
```
## Script 5
```
TypeError: can't multiply sequence by non-int of type 'float'
```
##### A statement can be print N number of time, where N is an integer and not a float. 
##### *Code fix :*
```
print("Let's repeat this" * 3)
```
## Script 6
```
IndentationError: unindent does not match any outer indentation level
```
##### Code indentation is not correct for if-else statement
##### *Code fix :*
```
age = int(input("Your age: "))

if age < 18:
  print("Sorry, we don't serve minors here")
else:
  print("What can i serve you?")
```
## Script 7
```
SyntaxError: expected ':'
```
##### Syntax is not correct for while statement. While statement must end with a ':'
##### *Code fix :*
```
while input("What can I server you? ") != "Gin":
    print("Awful choice, try again.")
print("Good choice.")
```
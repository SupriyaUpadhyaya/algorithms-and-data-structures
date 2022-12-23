from cgitb import reset


print("Hello World!")

name = input("what is your name?")
print("Hello, " + name)

if name == "Supriya":
    print("Hello, " + name)
else:
    print("Not correct user!!")

x: int = 11
y: int = 2

result = 11//2, 11%2

print(result)

x: int = 0
while x <= 100:
    if x % 2 == 0:
        print(x)
    x = x + 1

for x in range(201):
    if x % 2 == 0:
        print(x)

x: int = 495
for x in range(500, 5, 525):
    print(x)
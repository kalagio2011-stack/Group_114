#2) მომხმარებელს შემოაყვანინეთ რიცხვი n და ტერმინალში
# გამოიტანეთ რიცხვები 1-იდან n-ის ჩათვლით.
# ეს დავალება შეასრულეთ როგორც for, ასევე მოიძიეთ ინფორმაცია 
# while ციკლზე და while loop-ითაც შეარსრულეთ ეს დავალება.

n = int(input("please enter your number: "))

for i in range(1, n + 1):
    print(i)

# for გამოიყენება ბრძანების რამდენჯერმე გასამეორებლად
#while იმეორებს ბრძანებას სანამ პირობა ჭეშმარიტია

#3) მომხმარებელს შემოაყვანინეთ რიცხვი n და დათვალეთ, 
# რამდენი რიცხვია 1-იდან n-ის ჩათვლით,
# რომელიც 3-ის ჯერადია. საბოლოოდ გამოიტანეთ ამ რიცხვების რაოდენობა.
# ეს დავალება შეასრულეთ როგორც for, ასევე while ციკლით.

aiter = int(input("please enter your number: "))

for i in range(1, aiter + 1):
    if i %  3 == 0:
        print(i)

b = int(input("please neter your number: "))

i = 1
while i <= b:
    if i % 3 == 0:print(i)
    i += 1
    
#4) მომხმარებელს შემოაყვანინეთ რიცხვი n და გამოთვალეთ 0-იდან n-ის
# ჩათვლით არსებული ყველა ლუწი რიცხვის ჯამი. საბოლოოდ გ
# ამოიტანეთ მიღებული ჯამი
# . ეს დავალება შეასრულეთ როგორც for, ასევე while ციკლით.

number = int(input("enter any number: "))
total = 0

for i in range(0, number+1, 2):
    total = total + i
    print(total)
    
number1 = int(input("enter any number: "))

abc = 0
total1 = 0

while abc <=number1:
    total1 = total + abc
    abc = abc + 2
    print(total1)
    
# 6)

number2 = int(input("Enter any number: "))
total2 = 0

while number2 > 0:
    total2 = total2 + (number2%10)
    number2 = number2//10

print(total2)

number3 =input("enter any number: ")
total3 = 0

for i in number3:
    total3 = total3 + int(i)
    
print(total3)

# 7)
number4 = int(input("Enter any number: "))
total4 = 2
count = 0

while total4 <=number4:
    total4 = total4 +2
    count = count +1
print(total4)
print(count)


number5 = int(input("Enter any number: "))
total5 = 2
count2 = 0

for i in range(1):
    if total5 > number5:
        break

    total5= total5+2
    count2 = count2 +1

print(total5)
print(count2)

# 8) მომხმარებელს შემოაყვანინეთ რიცხვი n და გამოიტანეთ
# 0-იდან n-ის ჩათვლით ყველა რიცხვი, რომელიც 5-ის ჯერადია.
# ეს დავალება შეასრულეთ როგორც for, ასევე while ციკლით.

number6 = int(input("enter any number: "))

adc = 0

while adc <= number6:
    print(adc)
    adc = adc + 5
    
for i in range(0, number6+1, 5):
    print(i)


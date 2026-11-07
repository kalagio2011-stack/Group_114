#მომხმარებელს შემოაყვანინეთ მთელი რიცხვი n და for ციკლის დახმარებიუთ
# შეკრიბეთ ყვცელა ის რიცხვი 1-დან n-ის ჩავლით რომელიც
# 3-ზე უნაშთოდ იყოფა. საბოლოოდ გამოიტანეთ მიღებული ჯამი

n = int(input("please enter your number: "))

i = 0 

for i  in range(1, n  + 1):
    if i % 3 == 0:
        i = i + 1

print(i)

#მომხმარებელს შემოაყვანინეთ რიცხვი და შეამოწმეთ არის თუ არა
# მარტივი რიცხვი. მარტივი რიცხვი იყოფა მხოლოდ ერთზე და საკუთარ თავზე

number = int(input("please enter your number: "))

if n < 2:
    print("არ არის მარტივი")
else:
    მარტივია = True
    
    for i in range(2, n):
        if n % i == 0:
            მარტივია = True
        
    if მარტივია:
        print("მარტივი რიცხვია")
    else:
        print("არ არის მარტივი")
        

#მომხმარებელს შემოაყვანინეთ ორი დადებითი რიცხვი იპოვეთ მათი უდიდესი საერთო გამყოფი

number2 = int(input("please enter your number: "))
number3 = int(input("please enter your second number: "))



#მომხმარებელს შემოაყვანინეთ დადებითი მთელი რიცხვი.
# while ციკლის გამოყენებით გამოთცავეთ მხოლოდ კენთი ციფრების ჯამი


n2 = int(input("please enter your number: "))

jami = 0

while n2 > 0:
    cifri = n % 10
    
    if cifri % 2 == 1 :
        jami = jami + cifri
        
    n = n // 10
    
print(jami)
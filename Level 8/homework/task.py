#2) მომხმარებელს შემოაყვანინეთ მთელი რიცხვი n. შემდეგ while 
# ციკლის გამოყენებით გამოიტანეთ რიცხვები 1-იდან n-ის ჩათვლით.
#მოიძიეთ ინფორმაცია და გამოიყენეთ if და else, რათა:
#თუ რიცხვი ლუწია, ტერმინალში გამოიტანოთ "Even";
#სხვა შემთხვევაში გამოიტანოთ "Odd".

n = int(input("please enter your number: "))

i = 1

while i <= n:
    print(i)
    
    if i % 2 == 0:
        print("even")
    else:
        print("Odd")
        
    i = i + 1
    
#3) მომხმარებელს შემოაყვანინეთ რიცხვი n. while ციკლის
# გამოყენებით გამოიტანეთ რიცხვები 0-იდან n-ის ჩათვლით.
#გამოიყენეთ if და else:
#თუ რიცხვი 5-ის ჯერადია, გამოიტანეთ "Divisible by 5".
#სხვა შემთხვევაში გამოიტანეთ თავად რიცხვი

n2 = int(input("please enter your number: "))

i = 0

while i <= n2:
    if i % 5 == 0:
        print(i, "Divisible by 5")
    else:
        print(i)
    
    i = i + 1 
    
#4) შექმენით ცვლადი correct_password და შეინახეთ მასში პაროლი "python123".
#მომხმარებელს შეაყვანინეთ პაროლი და while ციკლის გამოყენებით ხელახლა მოსთხოვეთ შეყვანა, სანამ სწორ პაროლს არ შეიყვანს.
#გამოიყენეთ if და else:
#თუ პაროლი სწორია, გამოიტანეთ "Access Granted!".
#სხვა შემთხვევაში გამოიტანეთ "Wrong password!".

correct_password = "python123"

password = input("enter your password: ")

while password != correct_password:
    print("wrong password!")
    password = input("try again: ")
    
if password == correct_password:
        print("Accses granted!")
    
# 5) მომხმარებელს შემოაყვანინეთ რიცხვი n. for ციკლის გამოყენებით გამოიტანეთ რიცხვები 1-იდან n-ის ჩათვლით.
#გამოიყენეთ if და else:
#თუ რიცხვი 2-ის ჯერადია, გამოიტანეთ "Even number".
#სხვა შემთხვევაში გამოიტანეთ "Odd number".


n3 = int(input("please enter your number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
         print(i, "Even number")
    else:
        print(i, "Odd number")
        
#6) მომხმარებელს შემოაყვანინეთ რიცხვი n. for ციკლის 
# გამოყენებით გადაუარეთ რიცხვებს 1-იდან n-ის ჩათვლით.
#გამოიყენეთ if და else:
#თუ რიცხვი 3-ის ჯერადია, გამოიტანეთ ეს რიცხვი.
#სხვა შემთხვევაში გამოიტანეთ "Not divisible by 3".

n4 = int(input("please enter your number: "))

for i in range(1, n4 + 1):
    if i % 3 == 0:
        print(i)
    else:
        print("Not divisible by 3")
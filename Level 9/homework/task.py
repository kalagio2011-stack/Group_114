#2) მომხმარებელს შეაყვანინეთ ასაკი. თუ ასაკი 0-ზე ნაკლებია, გამოიტანეთ "Invalid age".
# თუ ასაკი 18 ან მეტია, გამოიტანეთ "Adult", სხვა შემთხვევაში — "Minor".

age = int(input("please enter your age: "))

if age < 0:
    print("Invalid age")
elif age >= 18:
    print("Adult")
else:
    print("minor")
    
#3) მომხმარებელს შეაყვანინეთ რიცხვი. თუ რიცხვი 
# დადებითია და ლუწია, გამოიტანეთ "Positive Even".
# თუ დადებითია და კენტია, გამოიტანეთ "Positive Odd".
# თუ უარყოფითია, გამოიტანეთ "Negative", სხვა შემთხვევაში — "Zero".

number = int(input("please enter your number: "))

if number > 0 and number % 2 == 0:
    print("Positive Even")
elif number > 0 and number % 2 != 0:
    print("Positive Odd")
elif age < 0:
    print("Negative")
else:
    print("Zero")
    
#4) შექმენით ორი ცვლადი: correct_username = "gio" და correct_password = "12345".მომხმარებელს შეაყვანინეთ სახელი და პაროლი.
# თუ ორივე სწორია, გამოიტანეთ "Login successful!", სხვა შემთხვევაში — "Wrong username or password!". გამოიყენეთ and.

correct_username = "gio"
correct_password = "12345"

username = input("please enter your username: ")
password = input("please enter your password: ")

if username == correct_username and password == correct_password:
    print("Loggin successful!")
else:
    print("Wrong username or password")
    
#5) უნდა შექმნა პროგრამა რომელშიც მომხარებლის დავალება იქნება,
# რომ გამოიცნოს შენს მიერ ჩაფიქრებული რიცხვი
#წინასწარ შექმენი რაიმე ცვლადი სადაც გექნება შენახული რაიმე რიცხვი,
# შემდგომ მომხმარებელს მოსთხოვე ამ რიცხვის გამოცნობა იქამდე,
#სანამ არ გამოიცნობს ამ რიცხვს, ასევე მიეცი მინიშნებებიც, თუ მომხმარებლის 
# ვარაუდი მეტია შენს რიცხვზე - "თქვენი რიცხვი მეტია ჩაფიქრებულზე"
#თუ რიცხვი ნაკლებია შენს რიცხვზე - "თქვენი რიცხვი ნაკლებია ჩაფიქრებულ 
# რიცხვზე" და თუ მომხმარებელი გამოიცნობს ჩაფიქრებულ რიცხვს
#რომ უთხარი "თქვენ წარმატებით გამოიცანით რიცხვი!".

number2 = 10

guess = int(input("guess a number: "))

while guess != number:
    if guess > number:
        print("your number is higher than the guess")
    else:
        print("your number is lower than the guess")
        
    guess = int(input("guess again: "))
    
print("you guessed the number")


#6) მომხმარებელს შეაყვანინეთ რიცხვი n. for ციკლის გამოყენებით 
# გამოიტანეთ ყველა რიცხვი 1-დან n-ის ჩათვლით.
#თუ რიცხვი ლუწია, გამოიტანეთ "Even", სხვა შემთხვევაში — "Odd".

n = int(input("please enter your number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")
        
#7) შექმენით ცვლადი correct_password = "python123".
# while ციკლის გამოყენებით მომხმარებელს პაროლი 
# შეაყვანინეთ მანამ,სანამ სწორ პაროლს არ შეიყვანს.
# არასწორი პაროლის შემთხვევაში გამოიტანეთ "Wrong password!",
# სწორი პაროლის შემთხვევაში — "Access Granted!".

correct_password2 = "python123"

password = input("enter your password: ")

while password != correct_password2:
    print("wrong password!")
    password = input("try again: ")
    
if password == correct_password2:
        print("Accses granted!")
        
#8) მომხმარებელს შეაყვანინეთ ორი რიცხვი: start და end.
# while ციკლის გამოყენებით გამოიტანეთ ყველა რიცხვი start-დან end-ის ჩათვლით.
#თუ რიცხვი დადებითია და ლუწია, გამოიტანეთ "Positive Even", სხვა შემთხვევაში გამოიტანეთ თავად რიცხვი.


start = int(input("please enter your number: "))
end = int(input("please enter your number: "))

while start <= end:
    if start % 2 == 0:
        print(start, "Positive even")
    else:
        print(start)
    
    start = start + 1
    
    
#9) მომხმარებელს შეაყვანინეთ ასაკი და გამოცდის ქულა.
# თუ ასაკი 18 ან მეტია და ქულა 70 ან მეტია,
# გამოიტანეთ "You passed!". თუ ასაკი 18-ზე ნაკლებია და ქულა 70 ან მეტია, 
# გამოიტანეთ "Good result, but you are under 18!".
# თუ ქულა 70-ზე ნაკლებია, გამოიტანეთ "You failed!".

user_age = int(input("please enter your age: "))
point = int(input("please enter your point: "))

if user_age >= 18 and point >= 70:
    print("You passed!")
elif user_age < 18 and point >= 70:
    print("Good result, but you are under 18")
elif point < 70:
    print("you failed")
    
#10) მომხმარებელს შეაყვანინეთ რიცხვი n. while ციკლის გამოყენებით
# გამოიტანეთ რიცხვები 1-დან n-ის ჩათვლით. თუ რიცხვი იყოფა 2-ზეც
# და 3-ზეც, გამოიტანეთ "Special Number"..
# თუ მხოლოდ 2-ზე იყოფა — "Even". თუ მხოლოდ 3-ზე იყოფა —
# "Divisible by 3". სხვა შემთხვევაში გამოიტანეთ თავად რიცხვი.

n2 = int(input("please enter you number: "))
 
i = 1

while i <= n2:
    if i % 2 == 0 and i % 3 == 0:
        print("special number")
    elif i % 2 == 0:
        print("Even")
    elif i % 3 == 0:
        print("Divisible by 3")
    else:
        print(i)
        
    i = i + 1
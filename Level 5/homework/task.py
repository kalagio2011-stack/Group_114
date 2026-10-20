# 2) მომხმარებელს შეაყვანინეთ ასაკი input() ფუნქციის გამოყენებით. გარდაქმენით 
# მიღებული მნიშვნელობა int() ფუნქციით და შეინახეთ ცვლადში. შეამოწმეთ შედარების ოპერატორების გამოყენებით,
# არის თუ არა მომხმარებელი 18 წლის ან მეტი. დაბეჭდეთ შესაბამისი შედეგი.

age=int(input("please enter your age: "))

print(age >= 18)

#3) მომხმარებელს შეაყვანინეთ ორი რიცხვი. პირველი გარდაქმენით int() ფუნქციით, ხოლო მეორე - float() ფუნქციით. 
# შეადარეთ ისინი ერთმანეთთან და დაბეჭდეთ, რომელი რიცხვია მეტი, ან ტოლია თუ არა ისინი.

number1=int(input("please enter your number: "))
number2=float(input("please enter your secong number: "))

print(number1 > number2)
print(number1 < number2)
print(number1 >= number2)
print(number1 <= number2)
print(number1 != number2)
print(number1 == number2)

# 4) მომხმარებელს შეაყვანინეთ სახელი, ასაკი და სიმაღლე. სახელი შეინახეთ str() ფუნქციის გამოყენებით,
# ასაკი გარდაქმენით int() ფუნქციით, ხოლო სიმაღლე - float() ფუნქციით.
# გამოიყენეთ bool() ფუნქცია სახელის შესამოწმებლად და შედარების ოპერატორებით განსაზღვრეთ,
# არის თუ არა მომხმარებელი 16 წლის ან მეტი და მისი სიმაღლე 1.70 მეტრზე მეტი. დაბეჭდეთ მიღებული შედეგები.

name=str(input("please enter your name: "))
age=int(input("please enter your age: "))
hight=float(input("please enter your hight: "))

print(bool(name))
print(age >= 16)
print(hight >= 1.70)

# 5) მომხმარებელს შემოაყვანინეთ სამი რიცხვი input() ფუნქციის დახმარებით,
# შემდგომ თითოეული მათგანი გარდაქმენით int() ფუნქციის დახმარებით ინტეჯერად,
# საბოლოოდ მომხმარებელს გამოუტანეთ ყველა შედარების ოპერატორის შედეგები ამ სამ რიცხვს შორის.

number1=int(input("please enter your number: "))
number2=int(input("please enter your second number:"))
number3=int(input("please enter your third number: "))

print(number1 > number3)
print(number2 < number1)
print(number3 >= number1)
print(number2 <= number1)
print(number1 != number2)
print(number2 == number3)
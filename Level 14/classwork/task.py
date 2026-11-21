#1) თქვენი დავალებაა შექმნათ 4 ფუნქცია: add, subtruct,
# multiply და divide, თითოეულ მათგანს უნდა გადაეცემოდეს
# არგუმენტად ორი რიცხვი და თითოეულმა ფუნქციამ უნდა ჩაატაროს შესაბამისი მათემატიკური ოპერაცია
# (დამატება, გამოკლება, გამრავლება და გაყოფა),
# თითოეული ფუნქცია უნდა აბრუნებდეს მიღებულ შედეგს, 
# საბოლოოდ გამოიყენეთ ოთხივე ფუნქცია და 
# ტერმინალში გამოიტანეთ მათემატიკური ოპერაციების შედეგები.


def add(a, b):
    return a + b

def substract(a, b):
    return(a + b)

def multiply(a, b):
    return(a * b)

def divide(a,b):
    return(a // b)

num1 = int(input("enter your number: "))
num2 = int(input("enter your second number: "))

print(add(num1, num2))
print(substract(num1, num2))
print(multiply(num1, num2))
print(divide(num1, num2))
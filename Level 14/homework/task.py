#2) შექმენით ფუნქცია greet(), რომელსაც გადაეცემა 
# მომხმარებლის სახელი. ფუნქციამ უნდა დაბეჭდოს მისალმების ტექსტი,
# რომელშიც გამოყენებული იქნება მომხმარებლის
# სახელი. გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა სახელით.


def greet(name):
    print("Hello", name)
    
greet("Gio")
greet("Nika")
greet("Luka")


#3) შექმენით ფუნქცია calculator(), რომელსაც გადაეცემა
# ორი რიცხვი და მათემატიკური ოპერატორი (+, -, *, /). ფუნქციამ
#if-elif-else კონსტრუქციის გამოყენებით უნდა შეასრულოს 
# შესაბამისი მათემატიკური მოქმედება და დაბეჭდოს მიღებული შედეგი.


def caculator(num1 , num2, caculation):
    if caculation == "+":
        print(num1 + num2)
        
    elif caculation == "-":
        print(num1 - num2)
        
    elif caculation == "*":
        print(num1 * num2)
        
    elif caculation == "/":
        print(num1 / num2)
    
caculator(10, 5, "+")
caculator(10, 5, "-")
caculator(10, 5, "*")
caculator(10, 5, "/")

#4) შექმენით ფუნქცია check_even(), რომელსაც
# გადაეცემა ერთი რიცხვი. ფუნქციამ შეამოწმოს,
#არის თუ არა რიცხვი ლუწი. თუ ლუწია, დააბრუნოს 
# ტექსტი „ლუწი რიცხვია“, ხოლო სხვა შემთხვევაში — „კენტი რიცხვია“.

def check_even(num3):
    if num3 % 2 == 0:
        print("ლუწი რიცხვი")
    else:
        print("კენტი რიცხვია")
        
check_even(10)
check_even(23)
check_even(9)

#5) შექმენით ფუნქცია print_numbers(),
# რომელსაც გადაეცემა ერთი რიცხვი. 
# ფუნქციამ for ციკლის გამოყენებით 
# დაბეჭდოს ყველა რიცხვი 1-იდან გადაცემულ რიცხვამდე.


def print_numbers(num4):
    for i in range(1, num4 + 1):
        print(i)
        
print_numbers(10)
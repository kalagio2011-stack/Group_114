#1) შექმენით პროგრამა, რომელიც მომხმარებელს 
# შეაყვანინებს 10 რიცხვს. თითოეული რიცხვის შეყვანის შემდეგ 
# პროგრამამ უნდა შეამოწმოს, არის თუ არა ის დადებითი,
# უარყოფითი თუ ნული და ასევე დაადგინოს, ლუწია თუ კენტი.
# საბოლოოდ გამოიტანეთ რამდენი დადებითი, 
# უარყოფითი, ლუწი და კენტი რიცხვი შეიყვანა მომხმარებელმა.

dadebiti = 0 
uaryopiti = 0
luwi = 0
kenti = 0
i = 0

while i < 10:
    number = int(input("please enter your nunmber: "))
    
    if number > 0:
        dadebiti = dadebiti + 1
    elif number < 0:
        uaryopiti = uaryopiti + 1
    
    if number % 2 == 0:
        luwi = luwi + 1
    else:
        kenti = kenti = 1
        
    i = i + 1
    
print("Dadebiti", dadebiti)
print("Uaryoiti", uaryopiti)
print("Luwi", luwi)
print("Kenti", kenti)

#2) შექმენით პროგრამა, რომელიც მომხმარებელს შეაყვანინებს პროდუქტების რაოდენობას,
# შემდეგ კი for ციკლის გამოყენებით თითოეული პროდუქტის ფასს. 
# პროგრამამ უნდა დაითვალოს ყველა პროდუქტის საერთო ღირებულება.
# თუ თანხა 200 ლარზე მეტია, მომხმარებელს მიეცით 15%-იანი ფასდაკლება,
# თუ 100-დან 200 ლარამდეა - 10%, ხოლო სხვა შემთხვევაში ფასდაკლება 
# არ მოქმედებს. საბოლოოდ გამოიტანეთ გადასახდელი თანხა.

n = int(input("how many products? "))
total = 0

for i in range(n):
    price = float(input("please enter products price: "))
    total = total + price
    
if total > 200:
    total = total * 0.85
elif total >= 100:
    total = total * 0.90
else:
    total = total
    
print("Final price: ", total)


#3) შექმენით პროგრამა, რომელშიც მომხმარებელმა უნდა გამოიცნოს
# წინასწარ განსაზღვრული რიცხვი (მაგალითად, 42). გამოიყენეთ while
# ციკლი, რათა მომხმარებელს ჰქონდეს გამოცნობის რამდენიმე მცდელობა.
# თუ შეყვანილი რიცხვი საიდუმლო რიცხვზე მეტია ან ნაკლებია, გამოიტანეთ
# შესაბამისი შეტყობინება. სწორი პასუხის შემთხვევაში გამოიტანეთ გამარჯვების
# შეტყობინება და მცდელობების რაოდენობა.


secret = 42
attempts = 0

guess = int(input("Guess the number: "))

while guess != secret:
    attempts = attempts + 1
    
    if guess > secret:
        print("Too high")
    else:
        print("Too low")
        
    guess = int(input("try again: "))
    
attempts = attempts + 1

print("you won!")
print("Number of attempts:", attempts)



#4) შექმენით პროგრამა, რომელიც მომხმარებელს შეაყვანინებს 5
# სტუდენტის სახელსა და ქულას. თითოეული სტუდენტის ქულის 
# მიხედვით განსაზღვრეთ მისი შედეგი: თუ ქულა 90 ან 
# მეტია - "შესანიშნავი", თუ 70-დან 89-მდეა - "კარგი", თუ 50-დან 69-მდეა - "დამაკმაყოფილებელი", 
# ხოლო 50-ზე ნაკლები ქულის შემთხვევაში - "ჩაჭრილი".
# საბოლოოდ გამოიტანეთ ყველა სტუდენტის სახელი და შესაბამისი შედეგი.


i = 0 

while i < 5:
    name = input("Enter student name: ")
    
    grade = int(input("Enter student grade: "))
    
    if grade >+ 90:
        result = "exelent"
    elif grade >= 70:
        result = "good"
    elif grade >= 50:
        result = "satisfactory"
    else:
        result = "failed"
        
    print(name, "-", result)
    
    i = i + 1
    

#5) შექმენით პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს
# რიცხვები მანამ, სანამ 0-ს არ შეიყვანს. გამოიყენეთ while ციკლი
# რიცხვების მისაღებად და თითოეული რიცხვისთვის განსაზღვრეთ, 
# დადებითია თუ უარყოფითი და ლუწია თუ კენტი. 
# როდესაც მომხმარებელი 0-ს შეიყვანს, პროგრამამ უნდა
# შეწყვიტოს რიცხვების მიღება და გამოიტანოს შეყვანილი რიცხვების
# ჯამი, მათი რაოდენობა და დადებითი რიცხვების რაოდენობა.


total = 0
count = 0
positive = 0

num = int(input("Enter a number: "))

while num != 0:
    total = total + num
    count = count + 1

    if num > 0:
        print("Positive")
        positive = positive + 1
    else:
        print("Negative")

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

    num = int(input("Enter a number: "))

print("Sum:", total)
print("Count:", count)
print("Positive numbers:", positive)
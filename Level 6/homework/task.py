#2) შექმენით ორი ცვლადი: age და has_ticket. age-ში შეინახეთ მომხმარებლის ასაკი, ხოლო has_ticket-ში — True ან False.
# გამოიყენეთ and ოპერატორი და შეამოწმეთ, შეუძლია თუ არა მომხმარებელს კინოში შესვლა.
# შესვლა შესაძლებელი უნდა იყოს მხოლოდ იმ შემთხვევაში, თუ მომხმარებელი მინიმუმ 12 წლისაა და ბილეთი აქვს. 
# (მონაცემები, ანუ age-იც და has_ticket-იც უნდა შემოაყვანინოთ მომხმარებელს.)

age = int(input("please enter your age: "))
has_ticket=input("please if you have ticket: ")
 
print(has_ticket == "yes" and age >= 12)

#3) მომხმარებელს input()-ის საშუალებით შეაყვანინეთ ორი რიცხვი და შეინახეთ ისინი int()-ის გამოყენებით ცვლადებში.
# გამოიყენეთ or ოპერატორი და შეამოწმეთ,
# არის თუ არა ერთ-ერთი რიცხვი 100-ის ტოლი. შედეგი გამოიტანეთ ტერმინალში (True ან False)

number1=int(input("please enter you number: "))
number2=int(input("please enter your second number: "))

print(number1 == 100 or number2 == 100)

#4) მომხმარებელს შეაყვანინეთ მისი სახელი და ასაკი. შექმენით ცვლადი is_student,
# რომლის მნიშვნელობაც იქნება True ან False. გამოიყენეთ and ოპერატორი და შეამოწმეთ,
# არის თუ არა მომხმარებელი სტუდენტი და ამავე დროს 18 წლის ან უფროსი. შედეგი გამოიტანეთ ტერმინალში.

user_name=input("please enter your name: ")
user_age=int(input("please enter your age: "))

is_student=bool(input("if you are student enter true if your not enter false: "))

print(is_student == True and user_age >= 18)

#5) შექმენით ორი ცვლადი: is_sunny და is_warm. ორივე ცვლადში შეინახეთ ლოგიკური მნიშვნელობები (True ან False).
# გამოიყენეთ not ოპერატორი, რათა შეამოწმოთ,
# არის თუ არა ამინდი მზიანი და ამავე დროს არ არის თუ არა თბილი.
# მიღებული შედეგი გამოიტანეთ ტერმინალში print()-ის საშუალებით.

is_sunny=True
is_warm=False

print(is_sunny and not is_warm)
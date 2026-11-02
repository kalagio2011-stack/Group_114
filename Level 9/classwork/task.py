# 1) მომხმარებელს შემოაყვანინეთ თავისი ასაკი,
# შემდგომ შეამოწმეთ არის თუ არა მომხმარებელი ბავშვი,
# მოზარდი, სრულწლოვანი თუ ხანდაზმული:

#თუ ასაკი მეტია 0-ზე და ნაკლებია 12-ზე - მომხმარებელი არის ბავშვი
#თუ ასაკი მეტია 12-ზე და ნაკლებია 18-ზე - მომხმარებელი არის მოზარდი
#თუ ასაკი მეტია 18-ზე და ნაკლებია 60-ზე - მომხმარებელი არის სრულწლოვანი
#თუ ასაკი მეტია 60-ზე და ნაკლებია 100-ზე - მომხმარებელი არის ხანდაზმული.

user_age = int(input("please enter your age: "))

if user_age > 0 and user_age < 12:
    print("user is a child")
elif user_age > 12 and user_age < 18:
    print("user is teenager")
elif user_age > 18 and user_age < 60:
    print("user is adult")
elif user_age >= 60 and user_age < 100:
    print("user is old")
    
#2) მომხმარებელს შემოაყვანინეთ თავისი ქულა რომელიც მიიღო შემაჯამებელზე, შემდგომ შეამოწმეთ:

#ქულა მეტია 90-ზე და ნაკლებია 100-ზე - შეფასება "A"
#ქულა მეტია 80-ზე და ნაკლებია 90-ზე - შეფასება "B"
#ქულა მეტია 70-ზე და ნაკლებია 80-ზე - შეფასება "C"
#ქულა მეტია 50-ზე და ნაკლებია 70-ზე - შეფასება "E"
#ქულა მეტია 0-ზე და ნაკლებია 50-ზე - შფასება "F"

#და ყველა სხვა შემთხვევაში "Wrong Score! Try again!".

point = int(input("please enter your point: "))

if point > 90 and point < 100:
    print("A")
elif point > 80 and point < 90:
    print("B")
elif point < 70 and point > 80:
    print("C")
elif point > 50 and point < 70:
    print("E")
elif point < 0 and point < 50:
    print("F")
else:
    print("Wrong score! Try again!")
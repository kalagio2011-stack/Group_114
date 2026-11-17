#1) კომენტარების სახით ახსენით რა არის ფუნქცია, მეთოდი და 
# რა განსხვავებაა მათ შორის, ასევე ახსენით რა არის ფუნქციის არგუმენტი

# პითონში გვაქვს რამოდენიმე ტოპის ფუნქციები.ჩაშენებული როგორიცაა print და range
# იწერება წერტილით რომელიც გამოყენება კონკრეტულ ფუნქციაზე სამუშაოდ
# არგუმებტი პითონში არის მონაცემი რომელსაც უნქციას ვაწვდიტ სამუშაოდ


#2) მოიყვანეთ თითოეული სტრინგის ფუნქციის 2-2 გამოყენების
# მაგალითი (.upper(), .lower(), capitalize() და .find()), 
# ასევე მოიძიეთ კიდევ 3 სტრინგის მეთოდის შესახებ და
# მათზეც მოიყვანეთ 2-2 მაგალითი, ასევე დეტალურად ახსენით 
# თითოეული მეთოდი რაზეც მოიძიებთ ინფორმაციას კომენტარების სახით.

num = " grade"
normal = "phone  "

print(num.upper())
print(normal.upper())

print(num.lower())
print(normal.lower())

print(num.capitalize())
print(normal.capitalize())

print(num.find("d"))
print(normal.find("k"))

print(num.strip())
print(normal.strip())

print(num.replace("grade", "hello"))
print(normal.replace("phone", "TV"))
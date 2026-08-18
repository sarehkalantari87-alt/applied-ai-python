#گرفتن نام و سن از ورودی
# name = input("enter your name: ")
# age = int(input("enter your age: "))
# print("hi", name,age)
# //////////////////////////////////
#یک عددی را از ورودی بگیرد اگه بزرگتر از صفر است بگوید مثبت وگرنه بگوید منفی
# a=int(input('enter a number'))
# if a>0 :
#     print('enter number +')
# else:
#     print('enter number -')
# /////////////////////////////////////
# سن را بگیرد اگه کوچکتر از 18 بود بگوید نوجوان در غیر این صورت بگوید جوان
# age=int(input('enter a age'))
# if age<=18 :
#     print('enter tringer')
# else:
#     print('enter javan')
# ///////////////////////////////////////
#بررسی زوج یا فرد بودن عدد
# number = int(input("enter a number: "))
# if number % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")
# ///////////////////////////////////////////
#بررسی رمز عبور
# password = input("enter your password: ")
# if password == "12345":
#     print("your welcome!")
# else:
#     print("password is wrong")
#OR
# pas='12345'
# password = input("enter your password: ")
# if password == pas:
#     print("your welcome!")
# else:
#     print("password is wrong")
# //////////////////////////////////
# گرفتن نمره از ورودی و مقایسه کردن
# number=int(input('enter a number:'))
# if (80 < number <=100) :
#     print('very good',number)
# elif (60 < number <=80) :
#     print('good',number)
# elif (60 < number <=40) :
#     print('ok',number)
# else:
#     print('bad',number)
# ////////////////////////////////
#بررسی وضعیت آب و هوا بر اساس دما
# temp = float(input('enter a air: '))
# if temp < 0:
#     print('air is  very cold')
# elif temp < 10:
#     print('air is  cold')
# elif temp < 20:
#     print('air is  ok')
# elif temp < 30:
#     print('air is  hot')
# else:
#     print('air is very hot')
# ////////////////////////////////
# تعیین فصل بر اساس شماره ماه
month = int(input('enter a month (for between 1 to 12): '))
if month == 1 or month == 2 or month == 3:
    print('spring season')
elif month == 4 or month == 5 or month == 6:
    print('summer season')
elif month == 7 or month == 8 or month == 9:
    print('Autumn Season')
elif month == 10 or month == 11 or month == 12:
    print('Winter Season')
else:
    print('enter a valid month')
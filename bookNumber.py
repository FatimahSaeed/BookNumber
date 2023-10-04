book_numbers = {"Amal": 1111111111,
                "Mohammed": 2222222222,
                "Khadijah": 3333333333,
                "Abdullah": 4444444444,
                "Rawan": 5555555555,
                "Faisal": 6666666666,
                "Layla": 7777777777}

number = input("enter the number to search")
newname = input("Enter new name")
newnum = input("Enter new number")

if newnum and newname is not None:
    book_numbers.update({newname: newnum})
    print(book_numbers)


def numfun(number):
    num = int(number)
    for k, v in book_numbers.items():
        if num == v:
           return k


if number == str:
    print("This is invalid number")
elif len(number) == 10:
    result = numfun(number)
    print(result)
else:
    print("Sorry, the number is not found ")



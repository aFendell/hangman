# User input v3 - validating input

let1 = input("guess a letter: ")
# if input contains more then 1 char and non-alphabet character
if len(let1) > 1 and not let1.isalpha():
    print("E3")
# if input is not alphabet
elif not let1.isalpha():
    print("E2")
# if input is more then 1 char
elif len(let1) > 1:
    print("E1")
# if input is OK - 1 alphabet char
elif len(let1) == 1 and let1.isalpha():
    print(let1.lower())



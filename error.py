# error handling
try:
    age_input = input('enter your age')
    age_input = age_input / 0
    print(age_input)
except TypeError:
    print('invakid data type')
except ZeroDivisionError:
    print('you cant divide by zero')
# encloses one or multiple line of code

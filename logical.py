name_lenght =input('enter your name: ')
if len(name_lenght) < 3:
    print('name must be at lest 3 characters')
elif len(name_lenght) > 50:
    print('name can be maximum of 50 characters')
else:
    print('name looks good')
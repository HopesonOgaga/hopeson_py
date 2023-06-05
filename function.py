
def greet ():
    print('hello world')
greet()

def outer():
    print('outer function')
    def inner():
        print('inner function')
    inner()
outer()
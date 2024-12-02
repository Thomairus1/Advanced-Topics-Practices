def cough(func):
    
    def func_wrappper():
        #stuff that happens before the function
        print("*cough*")
        func()
        #stuff that happens after the function
        print("*cough*")
    
    return func_wrappper


@cough
def awkward():
    print("Can I get a discount?")


@cough
def answer():
    print("This is a dollar tree. . .")

awkward()
answer()
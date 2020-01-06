def greet2(name):
    print("How are you, " + name + "?")

def bye():
    print("Ok, bye!")

def greet(name):
    print("Hey " + name + "!")
    greet2(name)
    print("Preparing to say goodbye...")
    bye()

greet("Marta")

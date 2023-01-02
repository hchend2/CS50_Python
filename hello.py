# Ask user for their name ...

def main():
    name = input("What is your name ? ").strip().title()
    #name = name.strip().title()
    #name = name.capitalize()
    # Say hello to user ...
    hello(name)
    #print(name)
    print("Welcom to our python bootcamp")

def hello(to):
    print ("hello", to)

main()
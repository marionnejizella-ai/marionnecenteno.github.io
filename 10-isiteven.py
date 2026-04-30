#Exercise 10: Is it even?
#Marionne Jizella E. Centeno

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an even number."
    
def main ():
    user_input = input("Enter a number to check:")
    num = int(user_input)
    
    result_message = check_even_odd(num)

    print(result_message)

if __name__== "__main__": main ()
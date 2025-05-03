import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range (length))
    return password

length = int(input("Enter a Desired password Length: "))

if __name__ =="__main__":
    print("generate_password: ", generate_password(length))
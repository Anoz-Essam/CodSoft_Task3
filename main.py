import string
import secrets

letters_nums = string.ascii_letters + string.digits
passwd_container = []

def generate_passwd(length):
    passwd = ''.join(secrets.choice(letters_nums) for i in range(length))
    passwd_container.append(passwd)
    return passwd

def view_passwd():
    for i in range(0 , len(passwd_container)):
        print(f"Password {i+1}:{passwd_container[i]}")

def main():
    print("1.Generate")
    print("2.View generated passwords")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            length = int(input("Enter length of password: "))
            print(f"Generated password: {generate_passwd(length)}")
        case 2:
            view_passwd()

if __name__ == '__main__':
    print("-----Password Generator----")
    while True:
        main()

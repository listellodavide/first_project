import re

def main():
    greet_employee()
    parse_emails()
    parse_text()

def greet_employee():
    print("Hello World")

def parse_emails():
    email_log = """ Received email on 20.09.2024 from davide.lindo12@gmail.com, 
                    Received email on 21.09.2024 from mantra9483@amazon.co.uk,
                    Received email on 21.09.2024 from ch23annel@tutto.bello.it."""

    print(re.findall("\w+@\w+\.[a-z]{2,12}\.?[a-z]{0,12}", email_log))

def parse_text():
    with open("login_attempts.txt", "r") as file:
        file_text = file.read()
    print(file_text.split())

if __name__ == "__main__":
    main()
def emailProcess(email):
    email_username = email[0:email.index("@")]
    # print(f"User name is : {email_username}")
    email_domain = email[email.index("@")+1:]
    return [email_username, email_domain]

def printMsg(email_username, email_domain):
    print(f"User name is : {email_username}; Email domain is {email_domain}")

def main():
    email = input("Please enter your email: ").strip()
    email_username, email_domain = emailProcess(email)
    printMsg(email_username, email_domain)

# When this file is main file
# main()
if __name__ == "__main__":
    main()

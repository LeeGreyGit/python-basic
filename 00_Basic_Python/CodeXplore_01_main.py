from CodeXplore_01_sub import emailProcess, printMsg

def main():
    emails = ['per001@gmail.com','per002@gmail.com','per003@gmail.com']
    for email in emails:
        username, email_domain = emailProcess(email)
        printMsg(username, email_domain)

if __name__ == "__main__":
    main()

def numUniqueEmails(emails):
    unqiueEmails = set()

    for email in emails:
        name, domain = email.split('@')
        local = name.split('+')[0].replace('.', '')
        unqiueEmails.add(local + '@' + domain)
    
    return len(unqiueEmails)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
count = numUniqueEmails(emails)
print("Number of Unqiue Emails is:", count)
import os

print(os.getcwd())

f = open('community_emails.txt', 'r')
for line in f:
    print(line)

f.close()

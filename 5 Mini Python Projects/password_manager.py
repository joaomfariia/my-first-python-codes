from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open('keys.key', 'wb') as key_file:
        key_file.write(key)

write_key()
'''

def retrieve_key():
    file = open('keys.key', 'rb')
    key = file.read()
    file.close()
    return key

master_password = input("What is the master password? ")
key = retrieve_key() + master_password.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        # read the file line by line
        for line in f.readlines():
            #print(line.rstrip())
            print(str(fer.decrypt(password.encode())))

def create():
    username = input("Username: ")
    password = input("Password: ")

    with open('passwords.txt', 'a') as f:
    # 'a' = append  'w' = write/overwrite   'r' = read
        f.write(username + "|" + str(fer.encrypt(password.encode())) + '\n')

while True:

    mode = input("Would you like to create a new password, view existing ones or quit? (view | create | quit) ").lower()
    
    if mode == 'quit':
        quit()

    if mode == 'view':
        view()
    elif mode == 'create':
        create()
    else:
        print("Invalid mode!")
        continue
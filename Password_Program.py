'''
Created on May 11, 2020

@author: noizebot
'''

URL=""
email=""
username=""
password=""


Credentials_List=list([email,username,password])
Password_DB = {URL: Credentials_List}

# PasswordFile= open(,'w')

# with open('passwordFile.txt','w') as data:
#     data.write(str(Password_DB))
# PasswordFile.write("stuff")


while True:
    action = int(input("1. Add a password:\n2. Get password:\n"))

    if action == 1:
        
        # 1.  Prompt user for data
        URL = input("Enter Website: ")
        email = input("Enter email: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
    
        # 2. Create List
        Credentials_List=list([email,username,password])
        
        
        # 3. UPDATE Dictionary 
        Password_DB.update({URL:Credentials_List})
        with open('passwordFile.txt','w') as data:
            data.write(str(Password_DB))
    
    if action == 2:
        
        html = input("What website are you looking for: ")
        for key in Password_DB.keys():
            if html == key:
                x,y,z=Password_DB[key]
                print("Email: ",x)
                print("Username: ", y)
                print("Password: ", z)
    
    






















# 
# print("Nested dictionary 1-") 
# print(Password_DB) 
#   
# # Nested dictionary having same keys 
# Password_DB = { 'Dict1': {'Site': search, 'age': '19'}, 
#          'Dict2': {'Site': search, 'age': '25'}} 
# print("\nNested dictionary 2-") 
# print(Password_DB) 
#   
# # Nested dictionary of mixed dictionary keys 
# Password_DB = { 'Dict1': {1: 'G', 2: 'F', 3: 'G'},  
#          'Dict2': {'Name': 'Geeks', 1: [1, 2]} } 
# print("\nNested dictionary 3-") 
# print(Password_DB)
# 
# print("Search: :" + search)
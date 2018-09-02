'''    
    Program that checks if name exist in list
'''

# capture List of string 

ordinary_list = []
f = open('ordinary_list.txt','r')
ordinary = f.readlines()      # Using .readlines()
f.close()
for name in ordinary:
    ordinary_list.append((name.title()).rstrip('\n')) 
# print(ordinary_list)

vip_list = []
f = open('vip_list.txt','r')
vip = f.readlines()      # Using .readlines()
f.close()
for name in vip:
    vip_list.append((name.title()).rstrip('\n')) 
# print(vip_list)

User_Name = (input("Please Enter your Name:\n > ")).title()
# Ask a user to enter one of their names and check through the lists to see
# if any(User_Name in mystring for mystring in vip_list) == True:
#     print ("\n".join(names for names in vip_list if User_Name.title() in names))

def registration_checker(User_Name):
    if any(User_Name in mystring for mystring in vip_list) == True:
        print ("\n".join(names for names in vip_list if User_Name.title() in names) + ", VIP")
    elif any(User_Name in mystring for mystring in ordinary_list) == True:
        print ("\n" .join(names for names in ordinary_list if User_Name.title() in names) + ", Ordinary")
    else:
        print("Sorry, The name {} entered is not registed in any list!".format(User_Name))
    

registration_checker(User_Name)
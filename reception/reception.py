'''    
    Program that checks if name exist in list
'''
print("\n\tRegistration Checker \n")

def read_file(file_to_read):
    # read from file
    names_list = []
    f = open(file_to_read,'r')
    NamesList = f.readlines()      # Using .readlines()
    f.close()
    for name in NamesList:
        names_list.append((name.title()).rstrip('\n'))

    return names_list

# print(read_file('ordinary_list.txt'))
# print(read_file('vip_list.txt'))

def registration_checker():
    User_Name = (input("Please Enter your Name:\n > ")).title()
    # Ask a user to enter one of their names and check through the lists to see
    ordinary_list = read_file('ordinary_list.txt')
    vip_list = read_file('vip_list.txt')
    if any(User_Name in mystring for mystring in vip_list) == any(User_Name in mystring for mystring in ordinary_list):
        print ("\n".join(names for names in vip_list if User_Name.title() in names) + ", VIP")
        print ("\n" .join(names for names in ordinary_list if User_Name.title() in names) + ", Ordinary")
    elif any(User_Name in mystring for mystring in vip_list) == True:
        print ("\n".join(names for names in vip_list if User_Name.title() in names) + ", VIP")
    elif any(User_Name in mystring for mystring in ordinary_list) == True:
        print ("\n" .join(names for names in ordinary_list if User_Name.title() in names) + ", Ordinary")
    else:
        print("Sorry, The name {} entered is not registed in any list!".format(User_Name))

registration_checker()
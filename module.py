class Person:

    def __init__(self, name, phone_number, email_address, professional):
        self.name = name #enscapulation
        self.phone = phone_number
        self.email = email_address
        self.professional = professional
    
    def description(self):
        return "I am {},{} by professional and my contact is {} and email is {}" \
        .format(self.name,self.professional, self.phone, self.email)


class User(Person):
    # pass
    def __init__(self, name, phone, email, professional, gender, age):
        super().__init__(name, phone, email, professional) #constract of super class
        self.gender = gender
        self.age = age


class GuestList:

    def __init__(self):
        self.dict_of_users = {}

    def add_user(self, users):
        if (self.user_exist(users.Id)):
            pass
        
        self.dict_of_users[users.Id] = users

    def find_user_by_email(self, Id):
        if(self.user_exist(1)):
            return self.dict_of_users[Id]
        
        return None

    def delete_user(self,Id):
        pass
    
    def user_exist(self,Id):
        return self.dict_of_users.__contains__(Id)
    

class AppUsers:
    def __init__(self, Id, username, email_address):
        self.Id = Id
        self.name = username
        self.email = email_address

class SignUp():
    def __init__(self):
        self.first_name = dict()
        self.last_name = dict()
        self.email_address = dict()
        self.user_password = dict()
    
    def firstName(self,name,firstname):
        self.first_name[name] = firstname
        if not isinstance(self.first_name[name], str):
            raise TypeError("Value should be a string")
            # continue
        if len(self.first_name[name]) < 3:
            raise ValueError("name should have more than 3 characters" )  
    
    def lastName(self,name,lastname):
        self.last_name[name] = lastname
        if not isinstance(self.last_name[name], str):
            raise TypeError("value should be a string") 
        if len(self.last_name[name]) < 3:
            raise ValueError("few character inputs" ) 
    
    def emailAddress(self,email,e_address):
        self.email_address[email] = e_address
        if not isinstance(self.email_address[email], str):
            raise TypeError("email should be in string format")
            # raise ValueError("Email should have more than 14 characters " ) 
        if len(self.email_address[email]) < 14:
            raise ValueError("Email should have more than 14 characters")
        
    def add(self, email_Address, password):
        # pass
        self.user_password[email_Address] = password

    def getPassword(self, email_Address):
        return self.user_password[email_Address]
'''    
    Program that checks if name exist in list
'''

Ordinary_list = ["Lule Herman","Edmond Musiitwa","Eric Ebulu","Douglas Kato",\
"Kayabula Alex Joseph","Jolly Karungi","Christopher Kaggwa","Katusiime Joel"\
"Manzede Benard","Orone Faith","Rubarema Sam","kyakulumbye Ahmad","Mutesasira Moses",\
"Kica Ronald Okello","Michael Robert Wali","Mulondo Moses"]

Vip_list = ["Hakeem Matovu","kasule Joseph","Phiona Mary Kigai","Ivan Kivumbi",\
"Romin Kayira","Nabulo Vivian","Haruna Kiwooma","Soko Paul","Sekabira Yasin",\
"Ntale Shadik","Kabareebe Treasure","Maria Nanfuka","Kafuuma Henry","Albert Abaasa"]

# List of string #
def registration_checker(User_Name):

    if User_Name in Vip_list:
        print("Congratulations, {} is found in VIP List ".format(User_Name))
    elif User_Name in Ordinary_list:
        print("Congratulations, {} is found in Ordinary List ".format(User_Name))
    else:
        print("Sorry, The name {} entered is not registed in any list".format(User_Name))
    




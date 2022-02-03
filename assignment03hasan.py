dict0 = {1: {'First Name': 'Saiful','Last Name': 'Islam', 'Email': 'islam@gmail.com', 'password': 'a12345'},
         2: {'First Name': 'Mahmudul','Last Name': 'Hasan', 'Email': 'hasan@gmail.com', 'password': 'b12345'},
         3: {'First Name': 'Mominul','Last Name': 'Hasan', 'Email': 'mominul@gmail.com', 'password': 'c12345'} }

while True:
    email = input("Please enter your email: ")
    password =input("Please enter your password: ")
    checker=0

    for id in dict0:

        for k in dict0[id]:
            comp=(dict0[id][k])
            if email == comp:
                p=(dict0[id]['password'])
                if password == p:
                    print("Hello, "+dict0[id]['First Name']+" "+dict0[id]['Last Name']+" You have successfully logged in")
                    quit()
                else:
                    print("You have enterd incorrect password, You need to try again")
                    checker=1
                    break
    if checker==0:        
        print("You have entered incorrect email")
 
     

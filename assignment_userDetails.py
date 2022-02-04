while True:
    n=input('Enter any key to continue or Enter 0 to exit: ')
    checker=0
    if(n=='0'):
        break

    UserName=input('Enter user name: ')

    UserNameList=['hasan', 'mominul','mahmudul','sathi']

    FullNameList=['Hasan Minhaj','Mominul Hasan','Mohammed Mahmudul Hasan','Afroza Akhter Sathi']
    AgeList=['20','30','25','22']
    GernderList=['Male','Male','Male','Female']

    for name in UserNameList:
        if(name == UserName):
            print('')
            print("       User exists")
            print("    User name is ",UserName)
            
            if(UserName=='hasan'):
                print("    Full Name : "+FullNameList[0])
                print("    Age : "+AgeList[0])
                print("    Gender : "+GernderList[0])
            if(UserName == 'mominul'):
                print("    Full Name : "+FullNameList[1])
                print("    Age : "+AgeList[1])
                print("    Gender : "+GernderList[1])
            if(UserName == 'mahmudul'):
                print("    Full Name : "+FullNameList[2])
                print("    Age : "+AgeList[2])
                print("    Gender : "+GernderList[2])
            if(UserName == 'sathi'):
                print("    Full Name : "+FullNameList[3])
                print("    Age : "+AgeList[3])
                print("    Gender : "+GernderList[3])
            checker=5
            break
    if(checker != 5):
        print("User doesn't exist")   

    

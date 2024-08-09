"""PhoneNumber"""
def main() :
    """main"""

    phoneNumber = input()
    inCountry = input()

    if inCountry == "Domestic" :
        if len(phoneNumber) <= 9 :
            print(phoneNumber[:1] , phoneNumber[1:5] , phoneNumber[5:])
        else :
            print(phoneNumber[:2] , phoneNumber[2:6] , phoneNumber[6:])
    elif inCountry == "International" :
        if len(phoneNumber) <= 9 :
            print("+66" , phoneNumber[1:5] , phoneNumber[5:])
        else :
            print("+66"+phoneNumber[1:2] , phoneNumber[2:6] , phoneNumber[6:])
main()

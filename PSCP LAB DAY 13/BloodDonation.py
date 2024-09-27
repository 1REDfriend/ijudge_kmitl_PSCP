'''BloodDonation'''
def main():
    '''Smth'''
    age = int(input())
    weight = int(input())
    fq = int(input())
    cer1 = True
    cer2 = True
    result = "Yes"
    if age < 17 or age > 70:
        result = "No"
    if weight < 45 :
        result = "No"
    if not fq and age > 55 :
        result = "No"
    if age == 17 :
        cer1 = input()
        if cer1 == "False" :
            cer1 = False
    if 60 <= age <= 70 :
        cer2 = input()
        if cer2 == "False" :
            cer2 = False
    if not cer1 :
        result = "No"
    if not cer2 :
        result = "No"
    print(result)
main()

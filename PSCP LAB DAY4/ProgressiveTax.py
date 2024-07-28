"""ProgressiveTax"""
def main() :
    """taxttaxtax"""
    income = int(input())
    tax = 0
    if income > 4000000 :
        tax += ((income - 4000000) * 0.35)
        income = 4000000
    if income > 2000000 :
        tax += ((income - 2000000) * 0.3)
        income = 2000000
    if income > 1000000 :
        tax += ((income - 1000000) * 0.25)
        income = 1000000
    if income > 750000 :
        tax += ((income - 750000) * 0.2)
        income = 750000
    if income > 500000 :
        tax += ((income - 500000) * 0.15)
        income = 500000
    if income > 300000 :
        tax += ((income - 300000) * 0.1)
        income = 300000
    if income > 150000 :
        tax += ((income - 150000) * 0.05)
        income = 150000
    print(int(tax))
main()

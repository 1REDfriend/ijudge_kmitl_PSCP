"""MyMath"""
import math
def main() :
    """MyMath"""
    num1 = math.sin(math.radians(90)) + (math.sin(math.radians(60))**2)
    num1 = num1 / (math.cos(math.radians(245**2)) + math.cos(math.radians(45 + 135)))

    num2 = (math.factorial(16) * math.factorial(4))
    num2 = num2 / math.factorial(8)

    num3 = ((13**2) + (3**2))**0.5
    num3 = 40 / num3

    num4 = math.log10(1234**4)

    num5 = math.log(4234,5) + math.log2(8191) + (71 * math.log10(156154))
    num5 = num5 / (math.log(777,7) - math.log(888,8) - math.log(999,9))

    print(num1)
    print(num2)
    print(num3)
    print(num4)
    print(num5)
main()

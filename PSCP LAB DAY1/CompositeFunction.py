"""CompositeFunction"""
def main() :
    """CompositeFunction"""
    x = int(input())
    def f(x) :
        """def"""
        return 2 * x
    def g(x) :
        """def"""
        return x/2 + 1
    print(f"{f(g(x)):.2f}")
    print(f"{g(f(x)):.2f}")
main()

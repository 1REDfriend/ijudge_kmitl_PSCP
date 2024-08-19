"""1"""
def main():
    """1"""
    m1 =input("").strip()
    m2 =input("").strip()
    m3 =input("").strip()
    m4 =input("").strip()
    m5 =input("").strip()

    resulf = max(len(m1),len(m2),len(m3),len(m4),len(m5))
    print("*"*(resulf+4))
    print(f"* {m1:<{resulf}} *")
    print(f"* {m2:<{resulf}} *")
    print(f"* {m3:<{resulf}} *")
    print(f"* {m4:<{resulf}} *")
    print(f"* {m5:<{resulf}} *")
    print("*"*(resulf+4))

main()

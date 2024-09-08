"""counting star"""
def main() :
    """main void"""
    star = input() + " "
    st_star = ''
    constellation = 0
    comet = 0
    shooting_star = 0
    for v in star :
        if len(st_star) >= 2 :
            if st_star in ("~*" , "*~") :
                comet += 1
                st_star = ''
            elif st_star in "*/" :
                shooting_star += 1
                st_star = ''
            elif st_star in "**" :
                constellation += 1
                st_star = ''
            else :
                st_star = st_star[1]
        st_star += v

    if shooting_star or comet or constellation :
        print(f'constellation: {constellation}')
        print(f'comet: {comet}')
        print(f'shooting star: {shooting_star}')
    else :
        print("Tonight is a quiet night.")
main()

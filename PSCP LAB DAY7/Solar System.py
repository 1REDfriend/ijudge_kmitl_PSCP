"""Solar System"""
def sunsu(solar_ss) :
    """sunLnwza"""
    sun = 0
    if solar_ss.find("Sun ") != -1 :
        sun = solar_ss.find("Sun ")
    elif solar_ss.find(" Sun") != -1:
        sun = solar_ss.find(" Sun") +1
    return sun

def main() :
    """Solar System main"""
    solar_ss = input().strip()
    sun = sunsu(solar_ss)
    hot = ''
    cool = ''

    if solar_ss[:sun].count(" ") == solar_ss[sun:].count(" ") :
        hot += solar_ss[solar_ss.rfind(" ", 0, sun-1)+1:sun].strip()
        hot += " " + solar_ss[sun+4:solar_ss.find(" ", sun+4)].strip()

        cool += solar_ss[:solar_ss.find(" ")].strip()
        cool += " " + solar_ss[solar_ss.rfind(" "):].strip()

        print(f'Hot: {hot}')
        print(f'Cool: {cool}')
    elif solar_ss[:sun].count(" ") and solar_ss[sun:].count(" ") :
        hot += solar_ss[solar_ss.rfind(" ", 0, sun-1)+1:sun].strip()
        end_index = solar_ss.find(" ", sun+4)
        if end_index == -1:
            end_index = None
        hot += " " + solar_ss[sun+4:end_index].strip()

        if solar_ss[:sun].count(" ") > solar_ss[sun:].count(" ") :
            cool = solar_ss[:solar_ss.find(" ")].strip()
        else :
            cool = solar_ss[solar_ss.rfind(" "):].strip()

        print(f'Hot: {hot}')
        print(f'Cool: {cool}')
    elif not solar_ss[:sun].count(" ") :
        hot = solar_ss[solar_ss.find(" "):solar_ss.find(" " , 4)].strip()

        cool = solar_ss[solar_ss.rfind(" "):].strip()

        print(f'Hot: {hot}')
        print(f'Cool: {cool}')
    else :
        hot = solar_ss[solar_ss.rfind(" ",None,sun-1):solar_ss.rfind(" ")].strip()

        cool = solar_ss[:solar_ss.find(" ")].strip()

        print(f'Hot: {hot}')
        print(f'Cool: {cool}')
main()

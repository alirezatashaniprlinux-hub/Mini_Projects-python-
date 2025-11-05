def get_order(string , endnum):
   
    while True:
        try:
            num = int(input(string))
            if endnum < num:
                raise Exception()
            return num
        except:
            print('this order not a number or out of range')
            
def get_num(string):
    while True:
        try:
            num = float(input(string))
            return num
        except:
            print('please enter a number ...')
def main():
    print('hi\nwelcome to calculator')
    while True:
        print('1. sum')
        print('2. min')
        print('3. mul')
        print('4. dev')
        print('5. exit')
        
        choose = get_order('enter order :',5)
        if choose == 5 :
            break
        num1 = get_num('enter num 1: ')
        num2 = get_num('enter num 2: ')
        match choose:
            case 1:
                print(f'{num1}+{num2} = {num1+num2}')
            case 2:
                print(f'{num1}-{num2} = {num1-num2}')

            case 3 :
                print(f'{num1}x{num2} = {num1*num2}')

            case 4 :
                if num2 != 0 :
                    print(f'{num1}/{num2} = {num1/num2}')
                else:
                    print('cant calculate it becuse num2 is 0')

          

if __name__ == "__main__":
    main()
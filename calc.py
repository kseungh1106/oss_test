# get two integer parameters
# return sum
def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

def multi(x, y):
    return x*y

def div(x, y):
    return x/y


# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while True:        
        print("0: exit, 1: plus, 2: minus, 3: multiply, 4: divide")
        check = input()
        if check == '1':
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", plus(x,y))
            
        elif check == '2':
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", minus(x,y))
            
        elif check == '3':
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", multi(x,y))
            
        elif check == '4':
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            if y == 0:
                print("0으로 나눌 수 없습니다.")    
            else:
                print("answer : ", div(x,y))
            
        elif check > '4':
            print("0~4사이의 숫자를 입력하세요")
            
        else:
            print("Thank you")
            break
        
if __name__ == "__main__":
    main()

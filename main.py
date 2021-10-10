

def sigma(upper_point,down_point,power):
    sum = 0
    while(down_point <= upper_point):
        sum += down_point**power
        down_point+=1
        #print(sum)
    return sum

def main():
    upper_point=6
    down_point = 3
    power = 2
    print(sigma(upper_point,down_point,power))



if __name__ == '__main__':
    main()

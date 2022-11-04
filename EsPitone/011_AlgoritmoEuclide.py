def MCD(num_1,num_2):
    if num_1 < num_2 :
        num_1,num_2 = num_2,num_1

    while(num_1 % num_2 != 0): 
        num_2,num_1  = num_1 % num_2,num_2

    return num_2

def mcm(num_1,num_2):
    return (num_1*num_2)/MCD(num_1,num_2)

def main():
    print(f"MCD : {MCD(300,45)}\nmcm : {mcm(2,9)}")

if __name__ == "__main__":
    main()
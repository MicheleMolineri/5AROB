from cmath import sqrt


def ePrimo(num):
    
    div, p = 2 , True

    while(p and div <= int(num**0.5)+1):
        if (num%div) == 0:
            p = False 
        div += 1
        
    return  p    

print(ePrimo(int(input("inserisci un numero primo : "))))
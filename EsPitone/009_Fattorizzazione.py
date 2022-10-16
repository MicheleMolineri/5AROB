#991847

def scriviFile():
    f=open("./nPrimi.csv","w")
    for n in range(2,100000) :
        if ePrimo(n):
            f.write(str(n)+"\n")

def ePrimo(num):
    
    div, p = 2 , True

    while(p and div <= int(num**0.5)+1):
        if (num%div) == 0:
            p = False 
        
        div += 1
        
    return  p  

def fattori(num):
    f=open("./nPrimi.csv","r")
    testo = f.readlines()
    numPrimi  = [int(n) for n in testo]
    f.close()
    return  [ n for n in numPrimi if num%n == 0] 

def main():
    scriviFile()
    print("Scritto")
    print(fattori(int(input("inserisci un numero : "))))

if __name__ == "__main__":
    main()
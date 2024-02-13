while True:
    print ("0-Quitter")
    print ("1-addition")
    print ("2-sustraction")
    print ("3-multiplication")
    print ("4-division")
    print ("5-Mod")
    x=int(input("choisir une operation: "))
    if (x==0):
        print ("GoodBye")
        break
    elif (x==1):
        n1=float(input("saisir nombre 1: "))
        n2=float(input("saisir nombre 2: "))
        som = n1 + n2
        print("la somme de ",n1," et ",n2," est: ", som)
    elif (x==2):
        n1=float(input("saisir nombre 1: "))
        n2=float(input("saisir nombre 2: "))
        diff = n1 - n2
        print("la difference de ",n1," et ",n2," est: ", diff)
    elif (x==3):
        n1=float(input("saisir nombre 1: "))
        n2=float(input("saisir nombre 2: "))
        fois = n1 * n2
        print("la multipliquation de ",n1," et ",n2," est: ", fois)
    elif (x==4):
        n1=float(input("saisir nombre 1: "))
        n2=float(input("saisir nombre 2: "))
        while n2==0:
            n2=float(input('saisir un nombre non nulle\nTry Again: '))
        div = n1 / n2
        print("la division de ",n1," et ",n2," est: ", div)
    elif (x==5):
        n1=float(input("saisir nombre 1: "))
        n2=float(input("saisir nombre 2: "))
        while n2==0:
            n2=float(input('saisir un nombre non nulle\nTry Again: '))
        mod = n1 % n2
        print("le module de ",n1," et ",n2," est: ", mod)

#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.
def codi(a):
    cod=['a','b','u','e','l','i','t','o'] 
    cod1=["A","B","U","E","L","I","T","O"]
    print("Referencia",'abuelito')
    print("Referencia",'01234567')
    sad=''
    for i in range(len(a)):
        if a[i] in cod:
            sad+=str(cod.index(a[i]))
        elif a[i] in cod1:
            sad+=str(cod1.index(a[i]))
        else:
            sad+=a[i]
    print(sad)
    print("Palabra escogida",a)            
x=input('ingrese palabra a encriptar:')
codi(x)   
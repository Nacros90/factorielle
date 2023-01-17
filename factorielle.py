n=int(input("Entrez un entier naturel n : "))
f=1
for i in range(n):
    f=f*(i+1)
print("La factorielle de",n,"est",f)
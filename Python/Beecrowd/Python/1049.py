# TAG : Animal

variavel_1 = str(input()) .upper()  .strip()
variavel_2 = str(input()) .upper()  .strip()
variavel_3 = str(input()) .upper()  .strip()

if variavel_1 == "VERTEBRADO" :	
    
    if variavel_2 == "AVE" :
        
        if variavel_3 == "CARNIVORO" :
            especime = "aguia"

        elif variavel_3 == "ONIVORO" :
            especime = "pomba"


    elif variavel_2 == "MAMIFERO" :
        
        if variavel_3 == "ONIVORO" :
            especime = "homem"

        elif variavel_3 == "HERBIVORO" :
            especime = "vaca"
        
elif variavel_1 == "INVERTEBRADO" :
    
    if variavel_2 == "INSETO" :

        if variavel_3 == "HEMATOFAGO" :
            especime = "pulga"

        elif variavel_3 == "HERBIVORO" :
            especime = "lagarta"
        
    elif variavel_2 == "ANELIDEO" :

        if variavel_3 == "ONIVORO" :
            especime = "minhoca"
        
        elif variavel_3 == "HEMATOFAGO" :
            especime = "sanguessuga"

print(especime)
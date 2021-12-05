import re

# Cadena entrada
s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'

print(re.search("@robot3!",s))


cadena = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 5, number of retweets: 7"

print(re.search("User_mentions:9", cadena))
print(re.search("likes: 5", cadena))
print(re.search("number of retweets: 4", cadena))

#PROBLEMA 2 

if __name__ == "__main__":
    numero_tarjeta= [input() for _ in range(int(input())) ]

    pattern_1= "^[456]\d{16}$"
    pattern_2= "^[0123456789]\{4}-[0123456789]{4}-[0123456789]{4}-[0123456789]{4}"
    validator = re.compile(pattern_1,pattern_2)
    for p in numero_tarjeta:
        print("Valido" if validator.search(p) else "No valido")
           
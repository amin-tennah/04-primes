"""fonction calcule"""
#### Fonction secondaire


def isprime(p):
    """fonction calcule"""
    # votre code ici
    if p in (0,1):
        return False
    for d in range(2, int(p**0.581) + 1):
        if p % d == 0:
            return False
    return True

#### Fonction principale
def main():
    """fonction calcule"""
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()

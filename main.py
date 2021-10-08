def get_base_2(b):
    while b != 0:
        rest = b % 2
        rez = rez + rest * peter
        peter = peter * 10
        nr = nr / 2
    print(rez)


def test_get_base_2():
    assert get_base_2(10) == 1010
    assert get_base_2(5) == 101


def este_antipalindrom(b):
    copie = b
    nr = 0
    ok = True
    while copie > 0:
        nr = nr * 10 + copie % 10
        copie = copie // 10
    if b == nr:
        ok = False
    return ok


def test_este_antipalindrom():
    assert este_antipalindrom(101) == False
    assert este_antipalindrom(205) == True
    assert este_antipalindrom(306) == True
    assert este_antipalindrom(44) == False


def isPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def get_largest_prime_below(n):
    gasit = False
    n = n - 1
    while gasit == False:
        if isPrime(n) == True:
            return n
            gasit == True
        else:
            n = n - 1


def test_get_largest_prime_below():
    assert get_largest_prime_below(18) == 17
    assert get_largest_prime_below(15) == 13
    assert get_largest_prime_below(9) == 7


def main():
    test_get_base_2()
    test_este_antipalindrom()
    test_get_largest_prime_below()
    shouldRun = True
    while shouldRun:
        print("1. Transformati un numar din baza 10 in baza 2")
        print("2. Determinati daca un numar este antipalindrom")
        print("3. Determinati cel mai mare numar prim mai mic decat n")
        print("x. Oprire program")

        optiune = input("Alegeti optiunea ")
        if optiune == "3":
            n = int(input("Introduceti numarul "))
            if n > 2:
                print(get_largest_prime_below(n))
            else:
                print("Nu exista")
        elif optiune == "2":
            b = input("Introduceti numarul ")
            print(este_antipalindrom(b))
        elif optiune == "1":
            b = input("Introduceti numarul ")
            print(get_base_2(b))
        elif optiune == "x":
            shouldRun = False
        else:
            print("Optiune inexistenta. Reincercati!")

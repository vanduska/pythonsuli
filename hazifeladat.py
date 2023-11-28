import random

def random_homerseklet_generalas(varos, ido):
    homerseklet = [random.randint(1, 40) for _ in range(ido)]
    return {varos: homerseklet}

def main():
    varosok = ["Budapest", "Kaposvár", "Kecskemét", "Pécs", "Győr"]
    ido = 24

    homerseklet_adat = {}

    for varos in varosok:
        homerseklet_adat.update(random_homerseklet_generalas(varos, ido))

    for varos, homerseklet in homerseklet_adat.items():
        print(f"{varos} hőmérsékleti adatai:")
        for ora, homerseklet in enumerate(homerseklet, start=1):
            print(f"{ora}. óra: {homerseklet} °C")
        print()

if __name__ == "__main__":
    main()

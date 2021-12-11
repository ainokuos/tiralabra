from labyrintti import Labyrintti
from dead_end_filling import DeadEndFilling
#from wall_follower import WallFollower

def main():
    while True:
        print("1: Dead-end filling")
        print("2: Wall follower")
        print("0: Sulje")
        
        toiminto = int(input("Valitse toiminto: "))

        if toiminto == 1:
            koko = int(input("Anna labyrintin koko(n x n): "))
            labyrintti = Labyrintti(koko)
            DEF = DeadEndFilling(labyrintti.palauta())
            DEF.palauta()

        #if toiminto == 2:
            #WF = WallFollower(labyrintti)

        if toiminto == 0:
            break

if __name__=="__main__":
    main()

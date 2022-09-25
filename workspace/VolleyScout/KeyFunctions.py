class Key_Func():
    def __init__(self):
        self.data = []

    def abwehr6(self, liste):
        for player in liste:
            if player[1] == "Aussen" and (player[2] == '1' or player[2] == '5' or player[2] == '6'):
                print("Nr: " + player[0] + " hat abgewehr")

    def zuspiel(self, liste):

        for i in liste:
            if 'Zuspiel' in i:
                print(liste[liste.index(i)][0] + 'spielt zu')

    def liberoZuspiel(self, liste):
        for i in liste:
            if 'Libero' in i:
                print(liste[liste.index(i)][0] + 'spielt zu')

    def annahme(self, liste, a, b, c, d, e, f):
        print("hier")
        for i in liste:
            if 'Zuspiel' in i:
                print(i.index('Zuspiel'))

                zpos = liste[(i.index('Zuspiel') - 1)][2]

        print('pos : ' + zpos)

        if zpos == '1':
            for k in liste:
                if k[2] == a:
                    print(k[0] + "nimmt an")
        elif zpos == '6':
            for k in liste:
                if k[2] == b:
                    print(k[0] + "nimmt an")
        elif zpos == '5':
            for k in liste:
                if k[2] == c:
                    print(k[0] + "nimmt an")
        elif zpos == '4':
            for k in liste:
                if k[2] == d:
                    print(k[0] + "nimmt an")
        elif zpos == '3':
            for k in liste:
                if k[2] == e:
                    print(k[0] + "nimmt an")
        elif zpos == '2':
            for k in liste:
                if k[2] == f:
                    print(k[0] + "nimmt an")
        else:
            None
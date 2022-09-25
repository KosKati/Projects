from XMLFunctions import *


class keyFunktionen():
    def __init__(self, filename, label1, label2, label3):
        self.filename = filename
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        dir = os.path.dirname(__file__)
        dir = dir + "/Games/" + filename
        self.ist_Laufer_Eins = False


    def last_three_actions(self, new_text):
        self.label3.setText(self.label2.text())
        self.label2.setText(self.label1.text())
        self.label1.setText(new_text)

    def liberodrin(self, listen):
        for i in listen:
            if (i[1] == 'Libero') and (i[2] != '0'):
                return True
        return False

    def aufschlag(self, liste, time,  id_counter):
        self.ist_Laufer_Eins = False
        for i in liste:
            if (i[2] == '1') and (i[1] != 'Libero'):

                add_node(self.filename, i[0], 'Aufschlag', time, id_counter)
                #self.label1.setText('Aufschlag: ' + i[0] + '\t Zeit: ' + time)
                self.last_three_actions('Aufschlag: ' + i[0] + '\t Zeit: ' + time)


    def zuspiel(self, liste, time, id_counter):

        for i in liste:
            if 'Zuspiel' == i[1]:
                add_node(self.filename , i[0], 'Zuspiel', time, id_counter)
                self.last_three_actions('Zuspiel: ' + i[0] + '\t Zeit: ' + time)


    def liberoZuspiel(self, liste, time, id_counter):

        for i in liste:
            if ('Libero' == i[1]) and (i[2] != '0'):
                add_node(self.filename, i[0], 'Zuspiel', time, id_counter)
                self.last_three_actions('Zuspiel: ' + i[0] + '\t Zeit: ' + time)

    def abwehr1(self, liste, time, id_counter):
        for player in liste:
            if player[1] == "Zuspieler" and (player[2] == '5' or player[2] == '6' or player[2] == '1'):
                add_node(self.filename, player[0], 'Abwehr', time, id_counter)
                self.last_three_actions('Abwehr: ' + player[0] + '\t Zeit: ' + time)
            else:
                if player[1] == "Diagonal" and (player[2] == '5' or player[2] == '6' or player[2] == '1'):
                    add_node(self.filename, player[0], 'Abwehr', time, id_counter)
                    self.last_three_actions('Abwehr: ' + player[0] + '\t Zeit: ' + time)

    def abwehr2(self, liste, time, id_counter):
        for i in liste:

            if 'Zuspiel' in i:
                zpos = liste[liste.index(i)][2]


        if self.ist_Laufer_Eins:
            if self.liberodrin(liste):
                for k in liste:
                    if ((k[1] == "Aussen") and (k[2] == '2')):
                        add_node(self.filename, k[0], 'Abwehr', time, id_counter)
                        self.last_three_actions('Abwehr: ' + k[0] + '\t Zeit: ' + time)


        else:
            for player in liste:
                if (player[1] == "Diagonal") and ((player[2] == '2') or (player[2] == '3') or (player[2] == '4')) or (
                        (player[1] == "Zuspiel") and ((player[2] == '2') or (player[2] == '3') or (player[2] == '4'))):
                    add_node(self.filename, player[0], 'Abwehr', time, id_counter)
                    self.last_three_actions('Abwehr: ' + player[0] + '\t Zeit: ' + time)

    def abwehr3(self, liste, time, id_counter):

        for player in liste:
            if (player[1] == "Mitte") and ((player[2] == '2') or (player[2] == '3') or (player[2] == '4')):
                add_node(self.filename, player[0], 'Abwehr', time, id_counter)
                self.last_three_actions('Abwehr: ' + player[0] + '\t Zeit: ' + time)

    def abwehr4(self, liste, time, id_counter):
        for i in liste:

            if 'Zuspiel' in i:
                zpos = liste[liste.index(i)][2]


        if self.ist_Laufer_Eins:

            if self.liberodrin(liste):
                for k in liste:
                    if ((k[1] == "Diagonal") and (k[2] == '4')):
                        add_node(self.filename, k[0], 'Abwehr', time, id_counter)
                        self.last_three_actions('Abwehr: ' + k[0] + '\t Zeit: ' + time)


        else:
            for player in liste:
                if (player[1] == "Aussen") and ((player[2] == '2') or (player[2] == '3') or (player[2] == '4')) :
                    add_node(self.filename, player[0], 'Abwehr', time, id_counter)
                    self.last_three_actions('Abwehr: ' + player[0] + '\t Zeit: ' + time)

    def abwehr6(self, liste, time, id_counter):

        for player in liste:
            if (player[1] == "Aussen") and ((player[2] == '5') or (player[2] == '6') or (player[2] == '1')):
                add_node(self.filename, player[0], 'Abwehr', time, id_counter)
                self.last_three_actions('Abwehr: ' + player[0] + '\t Zeit: ' + time)

    def abwehr1(self, liste, time, id_counter):

        for player in liste:
            if ((player[1] == "Zuspiel") or (player[1] == "Diagonal")) and ((player[2] == '5') or (player[2] == '6') or (player[2] == '1')):
                add_node(self.filename, player[0], 'Abwehr', time, id_counter)
                self.last_three_actions('Abwehr: ' + player[0] + '\t Zeit: ' + time)

    def abwehr5(self, liste, time, id_counter):

        for player in liste:
            if (player[1] == "Libero") and ((player[2] == '5') or (player[2] == '6') or (player[2] == '1')):
                add_node(self.filename, player[0], 'Abwehr', time, id_counter)
                self.last_three_actions('Abwehr: ' + player[0] + '\t Zeit: ' + time)
            else:
                if player[1] == "Mitte" and ((player[2] == '5') or (player[2] == '6') or (player[2] == '1')):
                    add_node(self.filename, player[0], 'Abwehr', time, id_counter)
                    self.last_three_actions('Abwehr: ' + player[0] + '\t Zeit: ' + time)

    def einblock4(self, liste, time, id_counter):
        for i in liste:

            if 'Zuspiel' in i:
                zpos = liste[liste.index(i)][2]


        if zpos == '1':

            if self.liberodrin(liste):
                for k in liste:
                    if ((k[1] == "Diagonal") and (k[2] == '4')):
                        add_node(self.filename, k[0], 'Block', time, id_counter)
                        self.last_three_actions('Block: ' + k[0] + '\t Zeit: ' + time)
            else:
                for z in liste:
                    if (z[1] == 'Aussen') and (z[2] == '4'):
                        add_node(self.filename, z[0], 'Block', time, id_counter)
                        self.last_three_actions('Block: ' + z[0] + '\t Zeit: ' + time)

        else:
            for player in liste:
                if (player[1] == "Aussen") and ((player[2] == '2') or (player[2] == '3') or (player[2] == '4')) :
                    add_node(self.filename, player[0], 'Block', time, id_counter)
                    self.last_three_actions('Block: ' + player[0] + '\t Zeit: ' + time)

    def einervblock2(self, liste, time, id_counter):
        for i in liste:

            if 'Zuspiel' in i:
                zpos = liste[liste.index(i)][2]

        if zpos == '1':

            if self.liberodrin(liste):
                for k in liste:
                    if ((k[1] == "Aussen") and (k[2] == '2')):
                        add_node(self.filename, k[0], 'Block', time, id_counter)
                        self.last_three_actions('Block: ' + k[0] + '\t Zeit: ' + time)
            else:
                for z in liste:
                    if (z[1] == 'Diagonal'):
                        add_node(self.filename, z[0], 'Block', time, id_counter)
                        self.last_three_actions('Block: ' + z[0] + '\t Zeit: ' + time)


        else:
            for player in liste:
                if (player[1] == "Diagonal" and ((player[2] == '2') or (player[2] == '3') or (player[2] == '4')) or (
                        (player[1] == "Zuspiel") and ((player[2] == '2') or (player[2] == '3') or (player[2] == '4')))):
                    add_node(self.filename, player[0], 'Block', time, id_counter)
                    self.last_three_actions('Block: ' + player[0] + '\t Zeit: ' + time)


    def doppelblock2(self, liste, time, id_counter):
        for i in liste:
            if (i[1] == 'Mitte') and ((i[2] == '2') or (i[2] == '3') or (i[2] == '4')) :
                mitteVorne = i[0]

            if 'Zuspiel' in i:
                zpos = liste[liste.index(i)][2]


        if zpos == '1':

            if self.liberodrin(liste):
                for k in liste:
                    if ((k[1] == "Aussen") and (k[2] == '2')):
                        add_two_node(self.filename, k[0], mitteVorne, 'Block', time, id_counter)
                        self.last_three_actions('Block: ' + k[0] + ' und '+ mitteVorne + '\t Zeit: ' + time)
                        #print(k[0] + mitteVorne + ' blocken')
            else:
                for z in liste:
                    if (z[1] == 'Diagonal'):
                        add_two_node(self.filename, z[0], mitteVorne, 'Block', time, id_counter)
                        self.last_three_actions('Block: ' + z[0] + ' und ' + mitteVorne + '\t Zeit: ' + time)
                        #print(z[0] + mitteVorne +' blockt')


        else:
            for player in liste:
                if (player[1] == "Diagonal" and ((player[2] == '2') or (player[2] == '3') or (player[2] == '4')) or (
                        (player[1] == "Zuspiel") and ((player[2] == '2') or (player[2] == '3') or (player[2] == '4')))):
                    add_two_node(self.filename, player[0], mitteVorne, 'Block', time, id_counter)
                    self.last_three_actions('Block: ' + player[0] + ' und ' + mitteVorne + '\t Zeit: ' + time)
                    #print("Nr: " + player[0] + mitteVorne +" blockt")

    def doppelblock4(self, liste, time, id_counter):
        for i in liste:
            if (i[1] == 'Mitte') and ((i[2] == '2') or (i[2] == '3') or (i[2] == '4')) :
                mitteVorne = i[0]

            if 'Zuspiel' in i:
                zpos = liste[liste.index(i)][2]

        print('pos : ' + zpos)

        if zpos == '1':

            if self.liberodrin(liste):
                for k in liste:
                    if ((k[1] == "Diagonal") and (k[2] == '4')):
                        add_two_node(self.filename, k[0], mitteVorne, 'Block', time, id_counter)
                        self.last_three_actions('Block: ' + k[0] + ' und ' + mitteVorne + '\t Zeit: ' + time)
                        #print(k[0] + " " + mitteVorne + ' blockt')
            else:
                for z in liste:
                    if (z[1] == 'Aussen') and (z[2] == '2'):
                        add_two_node(self.filename, z[0], mitteVorne, 'Block', time, id_counter)
                        self.last_three_actions('Block: ' + z[0] + ' und ' + mitteVorne + '\t Zeit: ' + time)
                        #print(z[0] +  " " + mitteVorne + ' blockt')

        else:
            for player in liste:
                if (player[1] == "Aussen") and ((player[2] == '2') or (player[2] == '3') or (player[2] == '4')) :
                    add_two_node(self.filename, player[0], mitteVorne, 'Block', time, id_counter)
                    #add_node('Test.xml', mitteVorne, 'Block', time, id_counter)
                    self.last_three_actions('Block: ' + player[0] + ' und '+ mitteVorne + '\t Zeit: ' + time)

    def einerblock3(self, liste, time, id_counter):
        for player in liste:
            if (player[1] == "Mitte" and ((player[2] == '2') or (player[2] == '3') or (player[2] == '4'))):
                add_node(self.filename, player[0], 'Block', time, id_counter)
                self.last_three_actions('Block: ' + player[0] +  '\t Zeit: ' + time)
                    #print(player[0] + ' hat geblockt')

    def dreierblock(self, liste, time, id_counter):
        players = []
        for player in liste:
            if (player[2] == '3') or (player[2] == '4') or (player[2] == '2'):
                players.append(player[0])

        add_three_node(self.filename, players[0], players[1], players[2], 'Block', time, id_counter)
        self.last_three_actions('Block: ' + player[0] + ' und ' + player[1] + ' und ' + player[2] + ' und '+ '\t Zeit: ' + time)
                   # print(player[0] + ' hat geblockt')


    def annahme(self, liste, a, b, c, d, e, f, time, id_counter):
        for i in liste:
            if 'Zuspiel' in i:
                zpos = liste[liste.index(i)][2]


        if zpos == '1':
            self.ist_Laufer_Eins = True
            for k in liste:
                if k[2] == a:
                    add_node(self.filename, k[0], 'Annahme', time, id_counter)
                    self.last_three_actions('Annahme: ' + k[0] + '\t Zeit: ' + time)
        elif zpos == '6':
            for k in liste:
                if k[2] == b:
                    add_node(self.filename, k[0], 'Annahme', time, id_counter)
                    self.last_three_actions('Annahme: ' + k[0] + '\t Zeit: ' + time)
        elif zpos == '5':
            for k in liste:
                if k[2] == c:
                    add_node(self.filename, k[0], 'Annahme', time, id_counter)
                    self.last_three_actions('Annahme: ' + k[0] + '\t Zeit: ' + time)
        elif zpos == '4':
            for k in liste:
                if k[2] == d:
                    add_node(self.filename, k[0], 'Annahme', time, id_counter)
                    self.last_three_actions('Annahme: ' + k[0] + '\t Zeit: ' + time)
        elif zpos == '3':
            for k in liste:
                if k[2] == e:
                    add_node(self.filename, k[0], 'Annahme', time, id_counter)
                    self.last_three_actions('Annahme: ' + k[0] + '\t Zeit: ' + time)
        elif zpos == '2':
            for k in liste:
                if k[2] == f:
                    add_node(self.filename, k[0], 'Annahme', time, id_counter)
                    self.last_three_actions('Annahme: ' + k[0] + '\t Zeit: ' + time)
        else:
            None

    def angriff2(self, liste, time, id_counter):
        for i in liste:

            if 'Zuspiel' in i:
                zpos = liste[liste.index(i)][2]


        if zpos == '1':

            if self.liberodrin(liste):
                print(" Libero und Läufer 1")
                for k in liste:
                    if ((k[1] == "Aussen") and (k[2] == '2')):
                        add_node(self.filename, k[0], 'Angriff', time, id_counter)
                        self.last_three_actions('Angriff: ' + k[0] + '\t Zeit: ' + time)
            else:
                print(" Kein Libero und Läufer 1")
                for z in liste:
                    if (z[1] == 'Diagonal'):
                        add_node(self.filename, z[0], 'Angriff', time, id_counter)
                        self.last_three_actions('Angriff: ' + z[0] + '\t Zeit: ' + time)



        else:
            for player in liste:
                if (player[1] == "Diagonal" and ((player[2] == '2') or (player[2] == '3') or (player[2] == '4')) or (
                        (player[1] == "Zuspiel") and ((player[2] == '2') or (player[2] == '3') or (player[2] == '4')))):
                    add_node(self.filename, player[0], 'Angriff', time, id_counter)
                    self.last_three_actions('Angriff: ' + player[0] + '\t Zeit: ' + time)


    def angriff6(self, liste, time, id_counter):

        for player in liste:
            if player[1] == "Aussen" and (player[2] == '5' or player[2] == '6' or player[2] == '1'):
                add_node(self.filename, player[0], 'Angriff', time, id_counter)
                self.last_three_actions('Angriff: ' + player[0] + '\t Zeit: ' + time)

    def angriff1(self, liste, time, id_counter):

        for player in liste:
            if player[1] == "Diagonal" and (player[2] == '5' or player[2] == '6' or player[2] == '1'):
                add_node(self.filename, player[0], 'Angriff', time, id_counter)
                self.last_three_actions('Angriff: ' + player[0] + '\t Zeit: ' + time)

    def angriff3(self, liste, time, id_counter):

        for player in liste:
            if player[1] == "Mitte" and (player[2] == '2' or player[2] == '3' or player[2] == '4'):
                add_node(self.filename, player[0], 'Angriff', time, id_counter)
                self.last_three_actions('Angriff: ' + player[0] + '\t Zeit: ' + time)

    def angriff4(self, liste, time, id_counter):
        for i in liste:

            if 'Zuspiel' in i:
                zpos = liste[liste.index(i)][2]


        if zpos == '1':

            if self.liberodrin(liste):
                for k in liste:
                    if ((k[1] == "Diagonal") and (k[2] == '4')):
                        add_node(self.filename, k[0], 'Angriff', time, id_counter)
                        self.last_three_actions('Angriff: ' + k[0] + '\t Zeit: ' + time)
            else:
                for z in liste:
                    if (z[1] == 'Aussen') and (z[2] == '4'):
                        add_node(self.filename, z[0], 'Angriff', time, id_counter)
                        self.last_three_actions('Angriff: ' + z[0] + '\t Zeit: ' + time)


        else:
            for player in liste:
                if (player[1] == "Aussen") and (player[2] == '2' or player[2] == '3' or player[2] == '4') :
                    add_node(self.filename, player[0], 'Angriff', time, id_counter)
                    self.last_three_actions('Angriff: ' + player[0] + '\t Zeit: ' + time)

    def angriff1(self, liste, time, id_counter):
        for player in liste:
            if player[1] == "Zuspieler" and (player[2] == '5' or player[2] == '6' or player[2] == '1'):
                add_node(self.filename, player[0], 'Angriff', time, id_counter)
                self.last_three_actions('Angriff: ' + player[0] + '\t Zeit: ' + time)
            else:
                if player[1] == "Diagonal" and (player[2] == '5' or player[2] == '6' or player[2] == '1'):
                    add_node(self.filename, player[0], 'Angriff', time, id_counter)
                    self.last_three_actions('Angriff: ' + player[0] + '\t Zeit: ' + time)

    def angriff5(self, liste):

        for player in liste:
            if (player[1] == "Libero") and ((player[2] == '5') or (player[2] == '6') or (player[2] == '1')):
                print("Nr: " + player[0] + " hat angegriffen")
            else:
                if player[1] == "Mitte" and ((player[2] == '5') or (player[2] == '6') or (player[2] == '1')):
                    print("Nr: " + player[0] + " hat angegriffen")
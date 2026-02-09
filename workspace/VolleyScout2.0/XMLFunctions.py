from pathlib import Path
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class XMLFuctions():
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.root = None


    def create_new_Team(self,team_name: str, player_numbers):
        self.root = ET.Element('root')
        players_child = ET.SubElement(self.root,'Players')
        tree = ET.ElementTree(self.root)
        ET.indent(tree, space="\t", level=0)
        tree.write("./Teams/"+team_name+".xml", encoding="utf-8")
        for player_number in player_numbers:
            self.add_player_without_attributes(players_child,"number_"+player_number, team_name)

    def add_player_without_attributes(self,parent,number_player, game_name):
        player_node = ET.SubElement(parent,number_player)
        tree = ET.ElementTree(self.root)
        ET.indent(tree, space="\t", level=0)
        tree.write("./Teams/" + game_name + ".xml", encoding="utf-8")


    def create_new_game(self,game_name: str, player_numbers):

        self.root = ET.Element('root')
        players_child = ET.SubElement(self.root,'Players')
        tree = ET.ElementTree(self.root)
        ET.indent(tree, space="\t", level=0)
        tree.write("./Games/"+game_name+".xml", encoding="utf-8")
        for player_number in player_numbers:
            self.add_player(players_child,"number_"+player_number, game_name)

    def add_player(self,parent,number_player, game_name):
        player_node = ET.SubElement(parent,number_player)
        tree = ET.ElementTree(self.root)
        ET.indent(tree, space="\t", level=0)
        tree.write("./Games/" + game_name + ".xml", encoding="utf-8")
        self.add_player_attributes(player_node,game_name)

    def add_player_attributes(self, parent,  game_name):
        player_attribute = {"Service", "Reception", "Set", "Attack", "Block", "Defense"}

        for attribute in player_attribute:
            tmp_child = ET.SubElement(parent,attribute)
            tmp_child.text ="0/0/0/0/0/0"
            tree = ET.ElementTree(self.root)
            ET.indent(tree, space="\t", level=0)
            tree.write("./Games/"+game_name+".xml", encoding="utf-8")



    def read_value_player(self, player_number, action):
        player_number = "number_" + str(player_number)

        xml_file = Path(self.path)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        players = root.find("players")
        player = players.find(player_number)
        value = player.find(action).text

        return value


    def write_value_player(self, player_number, action, value):
        player_number = "number_" + str(player_number)

        xml_file = Path(self.path)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        players = root.find("players")
        player = players.find(player_number)
        player.find(action).text = value
        tree.write("./Games/testgame.xml")

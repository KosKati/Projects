import os
import xml
import xml.etree.ElementTree as ET
from datetime import datetime
from xml.dom import minidom
from xml.dom.minidom import parseString

from pathlib import Path

from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout
from lxml import etree
from lxml.builder import E



"""
def createRoot(nameFile):
    dir = os.path.dirname(__file__)
    dir = dir + "/Games/" + nameFile
    data = ET.Element('Raben')
    xmlstr = minidom.parseString(ET.tostring(data)).toprettyxml(indent="   ", newl='\r', encoding="utf-8")
    myfile = open(dir, 'wb')
    myfile.write(xmlstr)
    myfile.close()


def addNode(nameFile, player, action, time):
    dir = os.path.dirname(__file__)
    dir = dir + "/Games/" + nameFile
    tree = ET.parse(dir)
    root = tree.getroot()

    playerNode = ET.SubElement(root, 'player')
    playerNode.set("time", time)
    actionNode = ET.SubElement(playerNode, player)
    actionNode.text = action
    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ", newl='\r', encoding="utf-8")
    prettify(root)
    myfile = open(dir, 'wb')
    myfile.write(xmlstr)
    myfile.close()

createRoot('Test.xml')
addNode('Test.xml', 'Jenny', 'Aufschlag', '7878')
addNode('Test.xml', 'Bobby', 'Annahme', '98766')
addNode('Test.xml', 'Bobby', 'Block', '98754566')


"""

# !/usr/bin/env python3


GAMES_FOLDER_PATH = Path(__file__).absolute().parent / "Games"


def save_xml_document(path, root):
    #with open(path, 'w') as file:
     #   file.write(root)
    f = open(path, 'wb')
    f.write(etree.tostring(root, encoding="utf-8", pretty_print=True))
    f.close()

    #path.write_bytes(etree.tostring(root, encoding="utf-8", pretty_print=True))

    #with open(path, 'w') as file:
     #   file.write('')


def create_root(filename, root_name):
    save_xml_document(GAMES_FOLDER_PATH / filename, etree.Element(root_name))


def add_node(filename, player, action, time, c, rat):
    dir = os.path.dirname(__file__)
    dir = dir + "/Games/" + filename
    file_path = GAMES_FOLDER_PATH / filename
    root = etree.parse(dir).getroot()
    node = E('Timestamp', time=time, id=c)
    node.append(E(action, player, rating = rat))
    root.append(node)
    prettify(root)
    save_xml_document(file_path, root)

def add_node_laufer(filename, player, action, time, c, rat, lauf):
    dir = os.path.dirname(__file__)
    dir = dir + "/Games/" + filename
    file_path = GAMES_FOLDER_PATH / filename
    root = etree.parse(dir).getroot()
    node = E('Timestamp', time=time, id=c)
    node.append(E(action, player, rating = rat, Laufer = lauf))
    root.append(node)
    prettify(root)
    save_xml_document(file_path, root)



def add_two_node(filename, player1, player2, action, time, c, rat):
    dir = os.path.dirname(__file__)
    dir = dir + "/Games/" + filename
    file_path = GAMES_FOLDER_PATH / filename

    root = etree.parse(dir).getroot()
    node = E('Timestamp', time=time, id=c)

    node.append(E(action, player1, rating = rat))
    node.append(E(action, player2, rating = rat))
    root.append(node)
    prettify(root)
    save_xml_document(file_path, root)


def add_three_node(filename, player1, player2, player3, action, time, c, rat):
    dir = os.path.dirname(__file__)
    dir = dir + "/Games/" + filename
    file_path = GAMES_FOLDER_PATH / filename

    root = etree.parse(dir).getroot()
    root1 = E('Raben')

    node = E('Timestamp', time=time, id=c)

    node.append(E(action, player1, rating = rat))
    node.append(E(action, player2, rating = rat))
    node.append(E(action, player3, rating = rat))
    root.append(node)
    prettify(root)
    save_xml_document(file_path, root)


def print_root(filename):
    dir = os.path.dirname(__file__)
    dir = dir + "/Games/" + filename
    root = etree.parse(dir).getroot()
    print(root)


def prettify(element, indent='  '):
    queue = [(0, element)]  # (level, element)
    while queue:
        level, element = queue.pop(0)
        children = [(level + 1, child) for child in list(element)]
        if children:
            element.text = '\n' + indent * (level + 1)  # for child open
        if queue:
            element.tail = '\n' + indent * queue[0][0]  # for sibling open
        else:
            element.tail = '\n' + indent * (level - 1)  # for parent close
        queue[0:0] = children  # prepend so children come before siblings


def hhmmss(ms):
    # s = 1000
    # m = 60000
    # h = 3600000
    m, s = divmod(ms, 60)
    h, m = divmod(m, 60)
    return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))


def tree_to_labels(filename):
    com_line = QHBoxLayout()
    all_lines = QVBoxLayout()

    dir = os.path.dirname(__file__)
    dir = dir + "/Games/" + filename + ".xml"
    # tree = ET.parse(dir)
    # root = tree.getroot()
    mydoc = minidom.parse(dir)

    items = mydoc.getElementsByTagName('Timestamp')

    label_string = ''
    for elem in items:
        label_left = QLabel('')
        label_actions = QLabel('')
        label_right = QLabel('')
        label_left.setMinimumHeight(20)
        label_actions.setMinimumHeight(20)
        label_right.setMinimumHeight(20)
        com_line = QHBoxLayout()

        var = int(float(elem.attributes['time'].value))
        cur_time = hhmmss(var)
        label_string = 'id : ' + elem.attributes['id'].value + ' Zeit : ' + cur_time
        print('gefüllt' + label_string)
        label_left.setText(label_string + '\n')
        for sub_elem in elem.childNodes:
            if sub_elem.nodeType == sub_elem.ELEMENT_NODE:
                label_actions.setText(str(sub_elem.nodeName) + '\n')
                label_right.setText(str(sub_elem.firstChild.nodeValue) + '\n')

        com_line.addWidget(label_left)
        com_line.addWidget(label_actions)
        com_line.addWidget(label_right)
        all_lines.addLayout(com_line)
    return all_lines

def delete_node(id, file):
    #print('Treffer von id:' + id)
    tree = ET.parse(file)
    xml = tree.getroot()
    iterator = xml.findall("Timestamp")
    for item in iterator:
        f = item
        text = item.attrib["id"]
        if text == id.text():
            print('Treffer von id:' + id.text())
            xml.remove(f)
            tree.write(file)


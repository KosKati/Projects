from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import DBFunctions

filename = "dokument3"
c = canvas.Canvas(f"./Reports/{filename}.pdf")


c.drawString(100, 750, f"Spielbericht von EW gegen BS")

player_data = DBFunctions.select_report_player_data("game_data_ewd1_bs_01")
player_data.insert(0,["Nr.","Name","Punkte\nGes./BP/G-V", "Aufschlag\nGes./Fhl./Pkt.", "Annahme\nGes./Fhl./Pos.%/(Prf%)", "Angriff\nGes./Fhl./Blo/Pkt./(Pkt%)", "Block\nPkt."])
print(player_data)


# 3. Tabelle erstellen und Formatieren
table = Table(player_data)
style = TableStyle([
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#00FFFFFF')),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    #('GRID', (0, 0), (-1, 0), 1, colors.black),
    ('LINEAFTER', (0, 0), (-1, -1), 0.25, colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Horizontal center
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')  # Vertical center

])
table.setStyle(style)
table.wrapOn(c, 100, 10)
table.drawOn(c, 0, 450)

set_points_data = DBFunctions.select_report_set_points_data("game_data_ewd1_bs_01")
set_points_data.insert(0,[ "Satz","Punkte\nAuf./Ang./Bk./GgGhl.", "Aufschlag\nGes./Fhl./Pkt.", "Annahme\nGes./Fhl./Pos.%/(Prf%)", "Angriff\nGes./Fhl./Blo/Pkt./(Pkt%)", "Block\nPkt."])

table = Table(set_points_data)
style = TableStyle([
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#00FFFFFF')),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    #('GRID', (0, 0), (-1, 0), 1, colors.black),
    ('LINEAFTER', (0, 0), (-1, -1), 0.25, colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Horizontal center
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')  # Vertical center

])
table.setStyle(style)
table.wrapOn(c, 100, 10)
table.drawOn(c, 0, 300)


rotations_points_data = DBFunctions.get_rotation_difference_value("game_data_ewd1_bs_01")
rotations_points_data.insert(0,[ "Läufer:", "Punkte\n in Diff. :"])

table = Table(rotations_points_data)
style = TableStyle([
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#00FFFFFF')),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    #('GRID', (0, 0), (-1, 0), 1, colors.black),
    ('LINEAFTER', (0, 0), (-1, -1), 0.25, colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Horizontal center
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')  # Vertical center

])
table.setStyle(style)
table.wrapOn(c, 100, 10)
table.drawOn(c, 500, 283)


situation_points_data = DBFunctions.get_situations_points_value("game_data_ewd1_bs_01", "good_reception")
print("da")
print(situation_points_data)
situation_points_data.insert(0,[ "Dir. Angriffe n. guter Annahme\nFhl/Blo/Pkt%/Ges"])
print("da")
print(situation_points_data)
table = Table(situation_points_data)
style = TableStyle([
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#00FFFFFF')),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    #('GRID', (0, 0), (-1, 0), 1, colors.black),
    ('LINEAFTER', (0, 0), (-1, -1), 0.25, colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Horizontal center
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')  # Vertical center

])
table.setStyle(style)
table.wrapOn(c, 100, 10)
table.drawOn(c, 0, 150)

situation_points_data = DBFunctions.get_situations_points_value("game_data_ewd1_bs_01", "bad_reception")
print("da")
print(situation_points_data)
situation_points_data.insert(0,[ "Dir. Angriffe n. schlechter Annahme\nFhl/Blo/Pkt%/Ges"])
print("da")
print(situation_points_data)
table = Table(situation_points_data)
style = TableStyle([
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#00FFFFFF')),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    #('GRID', (0, 0), (-1, 0), 1, colors.black),
    ('LINEAFTER', (0, 0), (-1, -1), 0.25, colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Horizontal center
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')  # Vertical center

])
table.setStyle(style)
table.wrapOn(c, 100, 10)
table.drawOn(c, 200, 150)

situation_points_data = DBFunctions.get_situations_points_value("game_data_ewd1_bs_01", "defense")
print("da")
print(situation_points_data)
situation_points_data.insert(0,[ "Dir. Angriffe n. Abwehr\nFhl/Blo/Pkt%/Ges"])
print("da")
print(situation_points_data)
table = Table(situation_points_data)
style = TableStyle([
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#00FFFFFF')),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    #('GRID', (0, 0), (-1, 0), 1, colors.black),
    ('LINEAFTER', (0, 0), (-1, -1), 0.25, colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Horizontal center
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')  # Vertical center

])
table.setStyle(style)
table.wrapOn(c, 100, 10)
table.drawOn(c, 430, 150)


c.save()

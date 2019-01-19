import pip
import svgwrite
import XJ_Convertor
import requests
import xml_validation
import xml_extraction

if XJ_Convertor.inputType == '-f':
    JsonData = XJ_Convertor.parseJSON(XJ_Convertor.myfile)
elif XJ_Convertor.inputType == '-h':
    reponse = requests.get(url = XJ_Convertor.url)
    JsonData = reponse.json()
    
LEntites = []
# Recuperation de la liste des entités
for i in range(len(JsonData)):
    keys = JsonData[i].keys()
    key = next(iter(keys))
    LEntites.append(key)
    print(key)


# Initiation du fichier SVG
document_svg = svgwrite.Drawing(filename = XJ_Convertor.svgFile,
                                debug = True)

entityCoordsList = []
# Recuperation des noms des entités que l'on enregistre dans la variable "listEntites"
print('Liste des entites et leurs attributs: ')
for i in range(len(LEntites)):
    LAttributs = []
    LAssocs = []

    print('\t' + LEntites[i])

    # Recuperation des noms des attributs que l'on enregistre dans la variable "listAttributs"
    nbAttributs = len(JsonData[i][LEntites[i]][0].keys())
    
    for key in JsonData[i][LEntites[i]][0].keys():
        LAttributs.append(key)
        print('\t\t' + key)

    
    if (i % 2 == 0):
        # Creation du rectangle contenant les infos de l'entité
        document_svg.add(document_svg.rect(insert = (10, i*150 + 10),
                                           size = ("150px", "130px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(251, 131, 107)"))
        entityCoords = {
            "nomEntite": LEntites[i],
            "coordX": 10,
            "coordY": i*150 + 10
        }
        entityCoordsList.append(entityCoords)          

        document_svg.add(document_svg.rect(insert = (10, i*150 + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(251, 131, 107)"))
        

        # Affichage du nom de l'entité
        document_svg.add(document_svg.text(LEntites[i],
            insert=(20, i*150 + 30),
            stroke='none',
            fill="rgb(255, 255, 255)",
            font_size='15px',
            font_weight="bold")
        )

        # Affichage de la liste des attributs
        for k in range(len(LAttributs)):
            document_svg.add(document_svg.text(LAttributs[k],
                insert=(20, i*150 + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )
    else:
        # Creation du rectangle contenant les infos de l'entité
        document_svg.add(document_svg.rect(insert = (500, (i - 1)*150 + 10),
                                           size = ("150px", "130px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(251, 131, 107)"))

        entityCoords = {
            "nomEntite": LEntites[i],
            "coordX": 500,
            "coordY": (i - 1)*150 + 10
        }
        entityCoordsList.append(entityCoords)

        document_svg.add(document_svg.rect(insert = (500, (i - 1)*150 + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(251, 131, 107)"))

        

        # Affichage du nom de l'entité
        document_svg.add(document_svg.text(LEntites[i],
            insert=(510, (i - 1)*150 + 30),
            stroke='none',
            fill="rgb(255, 255, 255)",
            font_size='15px',
            font_weight="bold")
        )

        # Affichage de la liste des attributs
        for k in range(len(LAttributs)):
            document_svg.add(document_svg.text(LAttributs[k],
                insert=(510, (i - 1)*150 + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )

for i in range(len(LEntites)):
    # Recuperations des differentes associations
    nbAssocs = len(JsonData[i]['relations']['associations'])
    
    for j in range(nbAssocs):
            nomAutreEntite = JsonData[i]['relations']['associations'][j]["nomAutreEntite"]
            nomAssoc = JsonData[i]['relations']['associations'][j]["nomAssoc"]
            cardDeb = JsonData[i]['relations']['associations'][j]["cardDeb"]
            cardFin = JsonData[i]['relations']['associations'][j]["cardFin"]

            for k in range(len(entityCoordsList)):
                if entityCoordsList[k]['nomEntite'] == LEntites[i]:
                    for p in range(len(entityCoordsList)):
                        if entityCoordsList[p]['nomEntite'] == nomAutreEntite:
                            if entityCoordsList[i]['coordX'] == entityCoordsList[p]['coordX']:
                                debutLigneX = entityCoordsList[k]['coordX'] + 75
                                debutLigneY = entityCoordsList[k]['coordY'] + 130
                            elif entityCoordsList[i]['coordY'] == entityCoordsList[p]['coordY']:
                                debutLigneX = entityCoordsList[k]['coordX'] + 150
                                debutLigneY = entityCoordsList[k]['coordY'] + 65


                if entityCoordsList[k]['nomEntite'] == nomAutreEntite:
                    for p in range(len(entityCoordsList)):
                        if entityCoordsList[p]['nomEntite'] == nomAutreEntite:
                            if entityCoordsList[i]['coordX'] == entityCoordsList[p]['coordX']:
                                finLigneX = entityCoordsList[k]['coordX'] + 65
                                finLigneY = entityCoordsList[k]['coordY']
                            elif entityCoordsList[i]['coordY'] == entityCoordsList[p]['coordY']:
                                finLigneX = entityCoordsList[k]['coordX']
                                finLigneY = entityCoordsList[k]['coordY'] + 65

                    document_svg.add(document_svg.line(
                        (debutLigneX, debutLigneY),
                        (finLigneX, finLigneY),
                        stroke_width = "2",
                        stroke="rgb(15, 15, 15)"))
                    
                    #  Affichage de la cardinalité depart
                    document_svg.add(document_svg.text(cardDeb,
                        insert=(debutLigneX + 10, debutLigneY + 20),
                        stroke='none',  
                        fill="rgb(15, 15, 15)",
                        font_size='15px',
                        font_weight="bold")
                    )

                    # Affichage de la cardinalité arrivée
                    document_svg.add(document_svg.text(cardFin,
                        insert=(finLigneX - 40, finLigneY + 20),
                        stroke='none',  
                        fill="rgb(15, 15, 15)",
                        font_size='15px',
                        font_weight="bold")
                    )

                    # Affichage du nom de l'association
                    document_svg.add(document_svg.text(nomAssoc,
                        insert=((finLigneX - debutLigneX) / 2 + debutLigneX - 30, (finLigneY - debutLigneY)/2 + debutLigneY + 20),
                        stroke='none',  
                        fill="rgb(15, 15, 15)",
                        font_size='15px',
                        font_weight="bold")
                    )

document_svg.save()
import pip
import svgwrite
import XJ_Convertor
import requests

if XJ_Convertor.inputType == '-f':
    JsonData = XJ_Convertor.parseJSON(XJ_Convertor.myfile)
elif XJ_Convertor.inputType == '-h':
    reponse = requests.get(url = XJ_Convertor.url)
    JsonData = reponse.json()
    
LEntites = []
# Recuperation de la liste des entités
for i in range(len(JsonData)):
    keys = JsonData[i].keys()
    key = next(iter(keys))
    LEntites.append(key)
    print(key)


# Initiation du fichier SVG
document_svg = svgwrite.Drawing(filename = XJ_Convertor.svgFile,
                                debug = True)

entityCoordsList = []
# Recuperation des noms des entités que l'on enregistre dans la variable "listEntites"
print('Liste des entites et leurs attributs: ')
for i in range(len(LEntites)):
    LAttributs = []
    LAssocs = []

    print('\t' + LEntites[i])

    # Recuperation des noms des attributs que l'on enregistre dans la variable "listAttributs"
    nbAttributs = len(JsonData[i][LEntites[i]][0].keys())
    
    for key in JsonData[i][LEntites[i]][0].keys():
        LAttributs.append(key)
        print('\t\t' + key)

    
    if (i % 2 == 0):
        # Creation du rectangle contenant les infos de l'entité
        document_svg.add(document_svg.rect(insert = (10, i*150 + 10),
                                           size = ("150px", "130px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(251, 131, 107)"))
        entityCoords = {
            "nomEntite": LEntites[i],
            "coordX": 10,
            "coordY": i*150 + 10
        }
        entityCoordsList.append(entityCoords)          

        document_svg.add(document_svg.rect(insert = (10, i*150 + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(251, 131, 107)"))
        

        # Affichage du nom de l'entité
        document_svg.add(document_svg.text(LEntites[i],
            insert=(20, i*150 + 30),
            stroke='none',
            fill="rgb(255, 255, 255)",
            font_size='15px',
            font_weight="bold")
        )

        # Affichage de la liste des attributs
        for k in range(len(LAttributs)):
            document_svg.add(document_svg.text(LAttributs[k],
                insert=(20, i*150 + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )
    else:
        # Creation du rectangle contenant les infos de l'entité
        document_svg.add(document_svg.rect(insert = (500, (i - 1)*150 + 10),
                                           size = ("150px", "130px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(251, 131, 107)"))

        entityCoords = {
            "nomEntite": LEntites[i],
            "coordX": 500,
            "coordY": (i - 1)*150 + 10
        }
        entityCoordsList.append(entityCoords)

        document_svg.add(document_svg.rect(insert = (500, (i - 1)*150 + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(251, 131, 107)"))

        

        # Affichage du nom de l'entité
        document_svg.add(document_svg.text(LEntites[i],
            insert=(510, (i - 1)*150 + 30),
            stroke='none',
            fill="rgb(255, 255, 255)",
            font_size='15px',
            font_weight="bold")
        )

        # Affichage de la liste des attributs
        for k in range(len(LAttributs)):
            document_svg.add(document_svg.text(LAttributs[k],
                insert=(510, (i - 1)*150 + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )

for i in range(len(LEntites)):
    # Recuperations des differentes associations
    nbAssocs = len(JsonData[i]['relations']['associations'])
    
    for j in range(nbAssocs):
            nomAutreEntite = JsonData[i]['relations']['associations'][j]["nomAutreEntite"]
            nomAssoc = JsonData[i]['relations']['associations'][j]["nomAssoc"]
            cardDeb = JsonData[i]['relations']['associations'][j]["cardDeb"]
            cardFin = JsonData[i]['relations']['associations'][j]["cardFin"]

            for k in range(len(entityCoordsList)):
                if entityCoordsList[k]['nomEntite'] == LEntites[i]:
                    for p in range(len(entityCoordsList)):
                        if entityCoordsList[p]['nomEntite'] == nomAutreEntite:
                            if entityCoordsList[i]['coordX'] == entityCoordsList[p]['coordX']:
                                debutLigneX = entityCoordsList[k]['coordX'] + 75
                                debutLigneY = entityCoordsList[k]['coordY'] + 130
                            elif entityCoordsList[i]['coordY'] == entityCoordsList[p]['coordY']:
                                debutLigneX = entityCoordsList[k]['coordX'] + 150
                                debutLigneY = entityCoordsList[k]['coordY'] + 65


                if entityCoordsList[k]['nomEntite'] == nomAutreEntite:
                    for p in range(len(entityCoordsList)):
                        if entityCoordsList[p]['nomEntite'] == nomAutreEntite:
                            if entityCoordsList[i]['coordX'] == entityCoordsList[p]['coordX']:
                                finLigneX = entityCoordsList[k]['coordX'] + 65
                                finLigneY = entityCoordsList[k]['coordY']
                            elif entityCoordsList[i]['coordY'] == entityCoordsList[p]['coordY']:
                                finLigneX = entityCoordsList[k]['coordX']
                                finLigneY = entityCoordsList[k]['coordY'] + 65

                    document_svg.add(document_svg.line(
                        (debutLigneX, debutLigneY),
                        (finLigneX, finLigneY),
                        stroke_width = "2",
                        stroke="rgb(15, 15, 15)"))
                    
                    #  Affichage de la cardinalité depart
                    document_svg.add(document_svg.text(cardDeb,
                        insert=(debutLigneX + 10, debutLigneY + 20),
                        stroke='none',  
                        fill="rgb(15, 15, 15)",
                        font_size='15px',
                        font_weight="bold")
                    )

                    # Affichage de la cardinalité arrivée
                    document_svg.add(document_svg.text(cardFin,
                        insert=(finLigneX - 40, finLigneY + 20),
                        stroke='none',  
                        fill="rgb(15, 15, 15)",
                        font_size='15px',
                        font_weight="bold")
                    )

                    # Affichage du nom de l'association
                    document_svg.add(document_svg.text(nomAssoc,
                        insert=((finLigneX - debutLigneX) / 2 + debutLigneX - 30, (finLigneY - debutLigneY)/2 + debutLigneY + 20),
                        stroke='none',  
                        fill="rgb(15, 15, 15)",
                        font_size='15px',
                        font_weight="bold")
                    )

document_svg.save()


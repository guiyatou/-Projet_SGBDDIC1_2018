
import requests
import json

def getExtractedData(myJsondata,fjson):
        extractedData = dict()
        listEntites = []
        #Récuperation de la liste des entités

        for i in range(len(myJsondata)):
                keys = myJsondata[i].keys()
                key = next(iter(keys))
                listEntites.append(key)

        extractedData["allEntities"] = listEntites
        # Recuperation des noms des entités que l'on enregistre dans la variable "listEntites"

        #print('Liste des entites et leurs attributs: ')
        for i in range(len(listEntites)):
                listAttributs = []
                listAssocs = []

                # Recuperation des noms des attributs que l'on enregistre dans la variable "listAttributs"
                nbAttributs = len(myJsondata[i][listEntites[i]][0].keys())
                extractedData[listEntites[i]] = dict()
                for key in fjson[i][listEntites[i]][0].keys():
                        listAttributs.append(key)
                extractedData[listEntites[i]]["attributes"] = listAttributs
        for i in range(len(listEntites)):
        # Recuperations des differentes associations
                nbAssocs = len(myJsondata[i]['relations']['associations'])
        #print(nbAssocs)
        for j in range(nbAssocs):
                # for key in fichierjson[i][listEntites[i]]['relations']['associations'][j].keys():
                #     listAssocs.append(key)
                #     print(key)
                nomAutreEntite = fjson[i]['relations']['associations'][j]["nomAutreEntite"]
                # cardDeb = fichierjson[i][listEntites[i]]['relations']['associations'][j]["cardDeb"]
                # cardFin = fichierjson[i][listEntites[i]]['relations']['associations'][j]["cardFin"]
                nomAssoc = myJsondata[i]['relations']['associations'][j]["nomAssoc"]
                #print(nomAssoc)
        #print(extractedData)
        return extractedData
        #Recuperation des attributs d'une entitée
def getAttributesEntity(data,entityName):
        return data[entityName]["attributes"]


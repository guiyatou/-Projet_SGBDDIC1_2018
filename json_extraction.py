import requests
import json

def ExtraireDonnee(Jsondata,f1):
        extractionDonnee = dict()
        LEntites = []
        #Récuperation de la liste des entités

        for i in range(len(Jsondata)):
                keys = Jsondata[i].keys()
                key = next(iter(keys))
                LEntites.append(key)

        extractionDonnee["allEntities"] = LEntites
        # Recuperation des noms des entités que l'on enregistre dans la variable "listEntites

        for i in range(len(LEntites)):
                LAttributs = []
                LAssocs = []

                # Recuperation des noms des attributs que l'on enregistre dans la variable "listAttributs"
                nbAttributs = len(Jsondata[i][LEntites[i]][0].keys())
                extractionDonnee[LEntites[i]] = dict()
                for key in f1[i][LEntites[i]][0].keys():
                        LAttributs.append(key)
                extractionDonnee[LEntites[i]]["attributes"] = LAttributs
        for i in range(len(LEntites)):
        # Recuperations des differentes associations
                nbAssocs = len(Jsondata[i]['relations']['associations'])
        for j in range(nbAssocs):
                nomAutreEntite = f1[i]['relations']['associations'][j]["nomAutreEntite"]
                nomAssoc = Jsondata[i]['relations']['associations'][j]["nomAssoc"]
        return extractionDonnee
        #Recuperation des attributs d'une entitée
def getAttributesEntity(data,entityName):
        return data[entityName]["attributes"]


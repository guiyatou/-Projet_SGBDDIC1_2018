import xJ_Convertor

def extractXmlFile(myXmlFIle):
    diagramme= myXmlFIle.getchildren()
    allEntitiesName = list()
    allAssocName = list()
    extractedXmlFile = dict()
    extractedXmlFile["entities"] = dict()
    extractedXmlFile["assoc"] = dict()
    for entite in diagramme:
        entite_children = entite.getchildren()
        thisElementAttributes = list()
        for entite_child in entite_children:
            thisElementType = entite.tag
            thisElementName = entite_child.text
            
            print("\t{} {}".format(entite_child.tag,thisElementName))
            for attributes in entite_child:
                print("\t\t%s" % (attributes.tag))
                thisElementAttributes.append(attributes.tag)
                #Recuperation des noms d'entitees et d'associations
                if thisElementType=="entite":
                    allEntitiesName.append(thisElementName)
                else:
                    if thisElementType=="association":
                        allAssocName.append(entite_child.text)
            if thisElementType=="entite":
                print("Okkkkk")
                extractedXmlFile["entities"][thisElementName] = {"entityName":thisElementName,"attributes":thisElementAttributes}
            else:
                if thisElementType=="association":
                    extractedXmlFile["assoc"][thisElementName] = {"assocName":thisElementName,"attributes":thisElementAttributes}
    return {"entities":extractedXmlFile["entities"],"associations":extractedXmlFile["assoc"]}
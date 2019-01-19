import xml_extraction
import xml.etree.ElementTree as ET
#Projet_SGBD/XJ_Convertor.py


# analyse du fichier xml
def parsefile(file):
  return ET.parse(file)

#validation du fichier xml
def xml_validator(file):
  try:
    parsedFile = parsefile(file)
    return parsedFile.getroot()
  except Exception as e:
    print("---Erreur: le fichier xml %s n'a pas une bonne syntaxe" % file)
    print(" voila c'est ca l'erreur %s" %e)
    return False

if __name__ == "__main__":
  myXmlFile = xml_validator("fichier.xml")
  if myXmlFile!=False:
    extractedXmlFile = xml_extraction.extractXmlFile(myXmlFile)
    print(extractedXmlFile)

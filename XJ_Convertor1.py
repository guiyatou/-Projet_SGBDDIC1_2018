
importation os
système d' importation
importer json
importer json_validation

# DEBUT Fonctionnalité d'extrait des données du fichier json en respectant le format
def  parseJSON ( filePath ):
    file  =  open (filePath)
    data =  fichier .read ()
    j = json.loads (data)
    retour j
# FIN Function of l'extraire the data of file json in respectant le format

si  len (sys.argv) ==  7 :

    type de fichier = sys.argv [ 2 ]
    type d'entrée = sys.argv [ 3 ]
    
    si inputType ==  ' -h ' :
        url = sys.argv [ 4 ]
    elif inputType ==  ' -f ' :
        monfichier = sys.argv [ 4 ]
        nomFichier, fichierExt = os.path.splitext (myfile)
        fileExt = fileExt.lower ()

    svgFile = sys.argv [ 6 ]

    si  __name__  ==  " __main__ " :
        si inputType ==  ' -f ' :
            # Vérification si le fichier en entrée existe
            si  non (os.path.exists (monfichier)):
                print ( ' --- Erreur: Ce fichier n \' existe pas! ' )
            sinon :
                si fileType ==  ' json ' :
                    # Vérification de l'extention du fichier en entrée
                    si (fileExt ! =  ' .json ' ):
                        print ( ' --- Erreur: Veuillez entrer un fichier JSON ' )
                    sinon :
                        si json_validation.json_validator (myfile):
                            importer generation_svg
                        sinon :
                            print (myJsondata)

                elif fileType ==  " xml " :
                    if (fileExt ! =  ' .xml ' ):
                        print ( ' --- Erreur: Veuillez entrer un fichier XML ' )
                    sinon :
                        si validation.xml_validator (myfile):
                            print ( ' Traitement du fichier XML ' )
                        sinon :
                            validation.xml_validator (myfile)
                sinon :  
                    print ( " --- Erreur: Veuillez spécifier un type de fichier correct. " )
                    print ( " --- Votre choix: " + fileType)
                
        elif inputType ==  ' -h ' :
                    url = sys.argv [ 4 ]
                    print (url)
                    si fileType ==  ' json ' :
                        importer rouguisvg     
        sinon :
                    print ( " --- Erreur: Veuillez spécifier un type d'acquisition de fichier correct. " )
                    print ( " --- Votre choix: " + inputType)
sinon :
 print ( ' Erreur: Nombre d'arguments incorrects. ' )

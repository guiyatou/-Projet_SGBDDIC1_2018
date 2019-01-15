import sys
import xml.etree.ElementTree as ET
#verifier si l'option -i
if  sys.argv[1]=="-i":
	if sys.argv[3]=="xml" :
		if sys.argv[5]=="-t" :
			fichier = open("fichier.xml","w")
			fichier.write(r.text)
			fichier.close()
			tree = ET.parse("fichier.xml")
		pass
		tree = ET.parse(sys.argv[])
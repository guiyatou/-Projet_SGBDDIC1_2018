import sys
import xml.etree.ElementTree as ET
import svgwrite
import requests

#verification du fichier d'entree(l'option-i)
if  sys.argv[2]=="-i":
	if sys.argv[3]=="xml" :
		if sys.argv[5]=="-h" :
			r = requests.get("http://sgbdproject.000webhostapp.com/files/qtDTO.html")
			fichier = open("docXml.xml","w")
			fichier.write(r.text)
			fichier.close()
			tree = ET.parse("docXml.xml")
		pass
		tree = ET.parse(sys.argv[1])
root = tree.getroot()
#PARCOURIR LE FICHIER XML RECUPERE LES ENTITES ET LES ASSOCIATIONS ET LEURS ATTRIBUTS
for entite1 in root.findall('entite1'):
     
    # name = entite.get('id')
    nomEntite = entite1.find('nomEntite').text
    for attribut in entite1.findall('attribut'):
     	ide = attribut.find('id').text
     	nom = attribut.find('nom').text
    	prenom = attribut.find('prenom').text
    card1 = entite1.find('cardinalite').text


for entite2 in root.findall('entite2'):
     
    # name = entite.get('id')
    nomEntite2 = entite2.find('nomEntite').text
    for attribut in entite2.findall('attribut'):
     	ide2 = attribut.find('id').text
     	intitule = attribut.find('intitule').text
    card2 = entite2.find('cardinalite').text

for association in root.findall('association'):
     
    # name = entite.get('id')
     nomAssos = association.find('nomAssos').text
     for attribut in association.findall('attribut'):
     	date = attribut.find('date').text

#trace du fichier xml
#if sys.argv[4] in globals():
  	print nomEntite
	print ide
	print nom
	print prenom
	print card1
	
	print nomEntite2
	print ide2
	print intitule
	print card2

	print nomAssos
	print date
	#CREATION DU FICHIER SVG
dwg = svgwrite.Drawing('projet.svg')

# CREATION D'UNE ENTITE
dwg.add(dwg.rect((10, 10), (200, 100),
    stroke=svgwrite.rgb(0,0, 0, '%'),

    fill='white')
)

# ASSOCIER LA CARDINALITE A L'ENTITE
dwg.add(dwg.text(card1,
    insert=(65,125),
    stroke='none',
    fill=svgwrite.rgb(15, 15, 15, '%'),
    font_size='15px',
    font_weight="bold")
)
# LINE RELIANT DEUX CLASSE
dwg.add(dwg.line((210, 40), (8, 40), 
	stroke=svgwrite.rgb(0,0,0, '%'))
)

# NOM DE L'ENTITE
dwg.add(dwg.text(nomEntite,
    insert=(65,25),
    stroke='none',
    fill='black',
    font_size='15px',
    font_weight="bold",
    font_family="Arial")
)


# 
dwg.add(dwg.rect((10, 400), (200, 100),
    stroke=svgwrite.rgb(0, 0, 0, '%'),
    fill='white')
)

# 
dwg.add(dwg.text(nomEntite2,
    insert=(70, 420),
    fill='black',
    font_size='15px',
    font_weight="bold",
    font_family="Arial")
)


# 
dwg.add(dwg.text(card2,
    insert=(65,395),
    stroke='none',
    fill=svgwrite.rgb(15, 15, 15, '%'),
    font_size='15px',
    font_weight="bold")
)

dwg.add(dwg.line((100, 110), (100, 400), 
	stroke=svgwrite.rgb(0,0,0, '%'))
)


#l'association
dwg.add(dwg.line((210, 430), (8, 430), 
	stroke=svgwrite.rgb(0,0,0, '%'))
)
dwg.add(dwg.circle(center=(100,250),
    r=60, 
    stroke=svgwrite.rgb(15, 15, 15, '%'),
    fill='white')
)

dwg.add(dwg.text(nomAssos,
    insert=(70, 250),
    fill='black',
    font_size='15px',
    font_weight="bold",
    font_family="Arial")
)





# output our svg image as raw xml
print(dwg.tostring())

# SAUVEGARDER LE FICHIER SVG
#dwg.save()zimport sys
import xml.etree.ElementTree as ET
import svgwrite
import requests

#verifier si l'option -i
if  sys.argv[2]=="-i":
	if sys.argv[3]=="xml" :
		if sys.argv[5]=="-t" :
			r = requests.get("http://sgbdproject.000webhostapp.com/files/qtDTO.html")
			fichier = open("fluxXml.xml","w")
			fichier.write(r.text)
			fichier.close()
			tree = ET.parse("fluxXml.xml")
		pass
		tree = ET.parse(sys.argv[1])
root = tree.getroot()
#PARCOURIR LE FICHIER XML AFIN DE RECUPERER LES ENTITES ET LES ASSOCIATIONS ET LEURS ATTRIBUTS
for entite1 in root.findall('entite1'):
     
    # name = entite.get('id')
    nomEntite = entite1.find('nomEntite').text
    for attribut in entite1.findall('attribut'):
     	ide = attribut.find('id').text
     	nom = attribut.find('nom').text
    	prenom = attribut.find('prenom').text
    card1 = entite1.find('cardinalite').text


for entite2 in root.findall('entite2'):
     
    # name = entite.get('id')
    nomEntite2 = entite2.find('nomEntite').text
    for attribut in entite2.findall('attribut'):
     	ide2 = attribut.find('id').text
     	intitule = attribut.find('intitule').text
    card2 = entite2.find('cardinalite').text

for association in root.findall('association'):
     
    # name = entite.get('id')
     nomAssos = association.find('nomAssos').text
     for attribut in association.findall('attribut'):
     	date = attribut.find('date').text

#trace du fichier xml
#if sys.argv[4] in globals():
  	print nomEntite
	print ide
	print nom
	print prenom
	print card1
	
	print nomEntite2
	print ide2
	print intitule
	print card2

	print nomAssos
	print date
	#CREATION DU FICHIER SVG
dwg = svgwrite.Drawing('projet.svg')

# CREATION D'UNE ENTITE
dwg.add(dwg.rect((10, 10), (200, 100),
    stroke=svgwrite.rgb(0,0, 0, '%'),

    fill='white')
)

# ASSOCIER LA CARDINALITE A L'ENTITE
dwg.add(dwg.text(card1,
    insert=(65,125),
    stroke='none',
    fill=svgwrite.rgb(15, 15, 15, '%'),
    font_size='15px',
    font_weight="bold")
)
# LINE RELIANT DEUX CLASSE
dwg.add(dwg.line((210, 40), (8, 40), 
	stroke=svgwrite.rgb(0,0,0, '%'))
)

# NOM DE L'ENTITE
dwg.add(dwg.text(nomEntite,
    insert=(65,25),
    stroke='none',
    fill='black',
    font_size='15px',
    font_weight="bold",
    font_family="Arial")
)


# 
dwg.add(dwg.rect((10, 400), (200, 100),
    stroke=svgwrite.rgb(0, 0, 0, '%'),
    fill='white')
)

# 
dwg.add(dwg.text(nomEntite2,
    insert=(70, 420),
    fill='black',
    font_size='15px',
    font_weight="bold",
    font_family="Arial")
)


# 
dwg.add(dwg.text(card2,
    insert=(65,395),
    stroke='none',
    fill=svgwrite.rgb(15, 15, 15, '%'),
    font_size='15px',
    font_weight="bold")
)

dwg.add(dwg.line((100, 110), (100, 400), 
	stroke=svgwrite.rgb(0,0,0, '%'))
)


#l'association
dwg.add(dwg.line((210, 430), (8, 430), 
	stroke=svgwrite.rgb(0,0,0, '%'))
)
dwg.add(dwg.circle(center=(100,250),
    r=60, 
    stroke=svgwrite.rgb(15, 15, 15, '%'),
    fill='white')
)

dwg.add(dwg.text(nomAssos,
    insert=(70, 250),
    fill='black',
    font_size='15px',
    font_weight="bold",
    font_family="Arial")
)





# output our svg image as raw xml
print(dwg.tostring())

# SAUVEGARDER LE FICHIER SVG
#dwg.save()zimport sys
import xml.etree.ElementTree as ET
import svgwrite
import requests

#verifier si l'option -i
if  sys.argv[2]=="-i":
	if sys.argv[3]=="xml" :
		if sys.argv[5]=="-t" :
			r = requests.get("http://sgbdproject.000webhostapp.com/files/qtDTO.html")
			fichier = open("fluxXml.xml","w")
			fichier.write(r.text)
			fichier.close()
			tree = ET.parse("fluxXml.xml")
		pass
		tree = ET.parse(sys.argv[1])
root = tree.getroot()
#PARCOURIR LE FICHIER XML AFIN DE RECUPERER LES ENTITES ET LES ASSOCIATIONS ET LEURS ATTRIBUTS
for entite1 in root.findall('entite1'):
     
    # name = entite.get('id')
    nomEntite = entite1.find('nomEntite').text
    for attribut in entite1.findall('attribut'):
     	ide = attribut.find('id').text
     	nom = attribut.find('nom').text
    	prenom = attribut.find('prenom').text
    card1 = entite1.find('cardinalite').text


for entite2 in root.findall('entite2'):
     
    # name = entite.get('id')
    nomEntite2 = entite2.find('nomEntite').text
    for attribut in entite2.findall('attribut'):
     	ide2 = attribut.find('id').text
     	intitule = attribut.find('intitule').text
    card2 = entite2.find('cardinalite').text

for association in root.findall('association'):
     
    # name = entite.get('id')
     nomAssos = association.find('nomAssos').text
     for attribut in association.findall('attribut'):
     	date = attribut.find('date').text

#trace du fichier xml
#if sys.argv[4] in globals():
  	print nomEntite
	print ide
	print nom
	print prenom
	print nomEntite2
	print nomEntite2
	print ide
	print intitule
	print card2

	print nomAssos
	print date
	#CREATION DU FICHIER SVG
dwg = svgwrite.Drawing('projet.svg')

# CREATION D'UNE ENTITE
dwg.add(dwg.rect((10, 10), (200, 100),
    stroke=svgwrite.rgb(0,0, 0, '%'),

    fill='white')
)

# ASSOCIER LA CARDINALITE A L'ENTITE
dwg.add(dwg.text(card1,
    insert=(65,125),
    stroke='none',
    fill=svgwrite.rgb(15, 15, 15, '%'),
    font_size='15px',
    font_weight="bold")
)
# LINE RELIANT DEUX CLASSE
dwg.add(dwg.line((210, 40), (8, 40), 
	stroke=svgwrite.rgb(0,0,0, '%'))
)

# NOM DE L'ENTITE
dwg.add(dwg.text(nomEntite,
    insert=(65,25),
    stroke='none',
    fill='black',
    font_size='15px',
    font_weight="bold",
    font_family="Arial")
)


# 
dwg.add(dwg.rect((10, 400), (200, 100),
    stroke=svgwrite.rgb(0, 0, 0, '%'),
    fill='white')
)

# 
dwg.add(dwg.text(nomEntite2,
    insert=(70, 420),
    fill='black',
    font_size='15px',
    font_weight="bold",
    font_family="Arial")
)


# 
dwg.add(dwg.text(card2,
    insert=(65,395),
    stroke='none',
    fill=svgwrite.rgb(15, 15, 15, '%'),
    font_size='15px',
    font_weight="bold")
)

dwg.add(dwg.line((100, 110), (100, 400), 
	stroke=svgwrite.rgb(0,0,0, '%'))
)


#l'association
dwg.add(dwg.line((210, 430), (8, 430), 
	stroke=svgwrite.rgb(0,0,0, '%'))
)
dwg.add(dwg.circle(center=(100,250),
    r=60, 
    stroke=svgwrite.rgb(15, 15, 15, '%'),
    fill='white')
)

dwg.add(dwg.text(nomAssos,
    insert=(70, 250),
    fill='black',
    font_size='15px',
    font_weight="bold",
    font_family="Arial")
)





# output our svg image as raw xml
print(dwg.tostring())

# SAUVEGARDER LE FICHIER SVG
#dwg.save()
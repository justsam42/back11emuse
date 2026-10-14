texts = [
    {
        "name" : "roman-alphabet-letter-6", # format (Note 1)
        "nature" : "litterary",
        "type" : "character",
        "categorie" : "alphabet romain",
        "description" : "Sixième lettre de l'alphabet romain, appelée 'f' ou 'F' en majuscule",
        "value" : "F" 
    },
    { 
        "name" : "user-first-name", # format (Note 1)
        "nature" : "word",
        "type" : "name",
        "categorie" : "first",
        "description" : "1st argument  of attribut name - identity - user",
        "value" : "Fatou"
    },
    { 
        "name" : "website-title-11emuse", # format (Note 1)
        "nature" : "sentence",
        "type" : "title",
        "categorie" : "website",
        "description" : "Titre du site de la 11e muse",
        "value" : "La Onzieme Muse."
    },
    { 
        "name" : "idee-blocTitle-landingSection-homePage-11emuseWebsite", # format (Note 1)
        "nature" : "title",
        "type" : "target",
        "categorie" : "value prop",
        "description" : "Titre bloc idee - landing view - homepage site 11emuse ",
        "value" : "Une idée ?"
    },
    { 
        "name" : "projet-blocTitle-landingSection-homePage-11emuseWebsite", # format (Note 1)
        "nature" : "title",
        "type" : "target",
        "categorie" : "value prop",
        "description" : "Titre bloc projet - landing view - homepage site 11emuse ",
        "value" : "Une projet ?"
    },
    { 
        "name" : "besoin-blocTitle-landingSection-homePage-11emuseWebsite", # format (Note 1)
        "nature" : "title",
        "type" : "target",
        "categorie" : "value prop",
        "description" : "Titre bloc besoin - landing view - homepage site 11emuse ",
        "value" : "Une besoin ?"
    },
    {
        "name" : "url-homePage-11emuse-website", # format (Note 1)
        "nature" : "address",
        "type" : "url",
        "categorie" : "website",
        "description" : "Adresse de la page d'acceuil du site de la 11 emuse",
        "value" : "127.0.0.1:8000"
    },
    { 
        "name" : "catchphrase-11emuse", # format (Note 1)
        "nature" : "sentence",
        "type" : "catchphrase",
        "categorie" : "business",
        "description" : "Slogan de la Onzième Muse ",
        "value" : "Ne croyez pas en l'impossible, croyez en vous !"
    },
    { 
        "name" : "valueProp-summary-11emuse", # format (Note 1)
        "nature" : "sentence",
        "type" : "summary",
        "categorie" : "value prop",
        "description" : "Résumé de la proposition de valeur de la 11emuse ",
        "value" : "Partenaire de votre créativité, j'accompagne et facilite la gestion de vos projets les plus originaux."
    },
    { 
        "name" : "besoin-blocTitle-landingSection-homePage-11emuseWebsite", # format (Note 1)
        "nature" : "title",
        "type" : "target",
        "categorie" : "value prop",
        "description" : "Titre bloc besoin - landing view - homepage site 11emuse ",
        "value" : "Une besoin ?"
    },
    { 
        "name" : "targetMain-value-summary-11emuse", # format (Note 1)
        "nature" : "paragraphe",
        "type" : "summary",
        "categorie" : "value prop",
        "description" : "Resumé de la proposition de valeur pour la cible principale de l'entreprise la Onzième Muse",
        "value" : "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repellendus consequuntur similique nisi inventore excepturi culpa iusto sed soluta doloribus error ea adipisci quod."
    }
]




######## Notes :

#-------Note 1 : "format de name pour les atoms"

# est de la forme "of_objectB-objectA_is-related_to_objectC"

# encodé cela donne : name = f"{of_objectB}-{objectA_is}-{related_to_objectC}"

# First, we observe that the static symbols of this formatted string are the "-"
# There are representing the relation btw the 3 obects [{A},{B},{C}]

# Toutefois, si on s'attarde sur la nature de ces relations on remarque :
# A appartient à B car le statement est : {ObjectA_is} {of_ObjetB} 

# on a donc en réalité : 2 objets de type (ObjectA, is) (of, Object).
# En effet "_" repésente l'espace qu'il existe en "ObjetA" et "is" dans
#  l'expression "L'objet named A is "
# A is also an attribute but insecable de objet, il est ce qui le distingue des autres objets B et C, 
# leur nom ou identité en tant que qu'individu de leur Classe ou ensemble parent.


# Pour cette raison, on note {ObjetA} et non {Objet_A} ou {Objet-A} à ce niveau de representation des objets.

# reprenant le proposition selon laquelle 
# {ObjetA_is} = {(ObjectA), is)}

#permet de reformatter la string ainsi : f"{(ObjectB), of)}-{(ObjectA), is)}-{(ObjectC), related_to)}"

#-------(followed by) Note 2 : "format de name pour les blocs" dans blocs.py 
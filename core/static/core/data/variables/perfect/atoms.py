atoms = [
   { 
       "meta-data" : {
            "data_nature" : "litterary",
            "data_type" : "string",
            "categorie" : "short-string",
       },
       "attributes" : {
            "id" : "objectId",
            "name" : "website-title-11emuse", # format (Note 1)
            "description" : "",
            "location" : [
                {
                    "to_root" : "",
                    "to_self" : "/my-name-or-id",
                    "to_relatives" : [
                        {
                            "id" : "objectId",
                            "relation_type" : '',
                            "location" : [
                                "to_root", 
                                "to_self", 
                                "to_common_relatives"
                            ]
                        },
                    ]
                }
            ]
        },
        "value" : ["Ceci est une string."] 
    },
    { 
        "meta-data" : {
            "data_nature" : "ltterary",
            "data_type" : "string",
            "categorie" : "link",
        },
        "attributes" : {
            "id" : "objectId",
            "name" : "website-link-11emuse", # format (Note 1)
            "description" : "",
        },
        "value" :["Ceci est le path absolu d'un link"]
    },
    { 
        "meta-data" : {
            "data_nature" : "graphique",
            "data_type" : "medias",
            "categorie" : "image",
        },
        "attributes" : {
            "id" : "objectId",
            "name" : "website-icon-11emuse", # format (Note 1)
            "description" : "",
        },
        "value" :["Ceci est le path de cette image" ]
    },
    
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
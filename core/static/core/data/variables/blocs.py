from core.static.core.data.variables import atoms

blocs = [
    { 
        "meta-data" : {
            "bloc_nature" : "components",
            "bloc_type" : "actionable",
            "categorie" : "button",
        },
        "attributes" : {
            "id" : "objectId",
            "name" : "website-11emuse-home-button-logo", # format (Note 2)
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
        "value" : [  
            atoms[1], 
            atoms[3]
        ]   # Note 3 : Content Acces -- > les atoms ? 
    },
    { 
        "meta-data" : {
            "bloc_nature" : "components",
            "bloc_type" : "actionable",
            "categorie" : "button",
        },
        "attributes" : {
            "id" : "objectId",
            "name" : "website-11emuse-home-button-logo", # format (Note 2)
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
        "value" : [  
            atoms[1], 
            atoms[3]
        ]   # Note 3 : Content Acces -- > les atoms ? 
    }
]

######## Notes :

#-------(following) Note 1 : "format de name les blocs atoms" dans atoms.py
#--------------------Note 2 : "format de name pour les blocs 










# ----------------------Note 3 : Quel moyen ou possibilité d'accès au contenu
# 
# ----------------(Following) Note 4 "" APi dans texts.py

# Query SET ? 
# 
# ou SET[constantes] ?
# 
# 
# pour QUI ? 
# 
# 
# Fait par des ?
# 
# 
# Views SQL ou 
# 
# 
# Temp View SQL  
# 
# 
# Envoyé sous quel format ? 
# 
# JSON ou 
# 
# XML 
from django.db import models
from core.models import *


# Pour implementer @classmethod __save__  et __export__ pour class Text()
# TO DO : 
# ------------------chercher format meta-data pour parse API : 
# - IONOS (Hebergement ext)
# - NGINX-Router (Auto-hebergement)
# - PSQL Api (Ext DBpsy-copg2?) 
# - SQLite3 (Local storage pour standalone APP)
# - Rest-frameswork (Backend API) :
#       - (application/json)
#       - (app/parse-data/-qqchose)
# - React-router-dom (Frontend router Vite-react-js)

# ----------------------- chercher format meta-data pour parse migrations ext: 
# - UNITY (Export pour migrations)
# - UNREAL
#

character = {
    "meta-data" : {
        "var_type" : "char",
        "var_size" : 8
    },
    "attributes" : {
        "value" : {
            "unicode" : "",
            "hexadecimal" : "",
            "ASCII" : "",
            "binary" : "",
            "representations" : {
                "parsers" : [], 
                "dictionnaries" : [], 
                "libraries" : []
            }
        },
        "position" : {
                "grid" : {
                    "start_line" : 1,
                    "end_line" : 1,
                    "start_col" : 0,
                    "end_col" : 0
                },
                "origin" : {
                    "x" : 0,
                    "y" : "",
                    "z" : ""
                },
                "box" : {} 
        },
        "style" : {},
    },
}

word = {
    "meta-data" : {
        "var_super" : "char",
        "var_type" : ["list", "str"],
        "var_size" : character["var_size"] * character.length(),
        "position" : {
            "grid" : {
                "start_col" : character[0]["attributes"]["position"]["grid"],
                "end_col" : character[-1]["attributes"]["position"]["grid"],
                "start_line" : character[0]["attributes"]["position"]["grid"],
                "end_line" : character[-1]["attributes"]["position"]["grid"],
            }
        },
    },
    "attributes" : {
        "value" : [character["value"], character["value"], character["value"]],
        "chars_count" : [character["value"], character["value"], character["value"],].__len__(),
        "style" : {},
    },   
}

sentence = {
    "name" : "str",
    "meta-data" : {
        "position" : {
            "start_line" : 1,
            "end_line" : 1
        },
        "signs_count" : 0,
        "words_count" : 0,
    },
    "words" : [word] 
}

paragraphe = {
    "name" : "§",
    "meta-data" : {
        "start_line" : 1,
        "end_line" : 1,
        "signs_count" : 0,
        "spaces_count" : 0,
        "sentences_count" : 0,
    },
    "sentences" : [sentence],    
}

text = {
    "meta-data" : {
        "file_format" : "document",
        "data_type" : ".txt",
        "export_as" : [".txt",".pdf"]
    },
    "attributs" : {
        "id" : "",
        "nature" : "",
        "type" : "",
        "categorie" : "catchPhrase",
        "name" : ""
    },
    "content" : {
        "id" : 1,
        "name" : "",
        "paragraphes" : [paragraphe] 
    },
    "style" : {},
}


class Text(models.Model): 

    create_type = {
            "name" : "name",
            "description" : "xxxxx"
        }

    name = models.CharField(max_length=64, null=False, unique=True)
    nature = models.ForeignKey(Nature, null=False, on_delete=models.PROTECT, default=1)
    type = models.ForeignKey(Type, null=False, on_delete=models.PROTECT, default=1)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.PROTECT)
    description = models.CharField(max_length=128, blank=True)
    content = models.TextField(blank=False, null=False, unique=True)

    class Meta:
        ordering = ['type', 'categorie','name']

    def __str__(self):
        return f"{self.name} ({self.type.__getattribute__("name")}, {self.categorie.__getattribute__("name")} ) : {self.description}"


class Text:
    TYPOGRAPHIE = {
        "TITLE" : "Titre",
        "CORPS" : "Corps de texte",
        "LABEL" : "Label",
        "CTA" : "Call To Action",
        "DEFAULT" : "Unset"
    }

    def __init__(self, name, content, style):
        self.name = name
        self.content = content
        self.style = style


    @classmethod
    def __new__(cls):
        while True:
            name = input("New text name:")
            content = input("Start typing...")
            print(f"You entered : {name} - {content[0-64]}...")
            
            save = input(f"Save change (Y/N): {name} ?")

            if save in ["Y","Yes", "y", "yes"]:
                return cls(name, content)
            else :
                change = input(f"Change:\n Name (1)? Content (2)?")

                if change == 1 :
                    name = input("Rename:")
                    return cls(name, content)
                    
                elif change == 2:
                    content = content + input()
                    return cls(name, content)


    def __set__(self, instance, value):
        print(instance)
        change = input(f"Change (Enter #):\n 1.Name: {instance.name} ?\n2.Content: {instance.content[0-64]}?")

        if change == 1 :
            instance.name = value
            
        elif change == 2:
            instance.content = instance.content + value

        while True:
            save = input(f"Save change (Y/N): {instance.name} - {instance.content[0-64]}... ?")

            if save in ["Y","Yes", "y", "yes"]:
                return instance
            else:
                confirm =input("Disregard changes ? (Y/N)") 
                if confirm in ["Y","Yes", "y", "yes"]:
                    return f"{instance} was not changed."


    def __delete__(self, instance):
        while True:
            confirm_deletion = input(f"Delete (Y/N): {instance.name} - {instance.content[0-64]}... ?")
        
            if confirm_deletion in ["Y","Yes", "y", "yes"]:
                del instance
            else:
                return f"{instance} deletion cancelled."


    def __str__(self):
            return f"{self.name}"

    

    


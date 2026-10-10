from django.db import models
class Text(models.Model):
    TYPOGRAPHIE = {
        "TITLE" : "Titre",
        "CORPS" : "Corps de texte",
        "LABEL" : "Label",
        "CTA" : "Call To Action",
        "DEFAULT" : "Unset"
    } 

    create_type = {
            "name" : "name",
            "description" : "xxxxx"
        }

    name = models.CharField(max_length=64, null=False, unique=True)
    nature = models.ForeignKey(models.Nature, null=False, on_delete=models.PROTECT, default=1)
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

    

    


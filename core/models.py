from django.db import models


# Create your models here.

class Nature(models.Model):
    name = models.CharField(max_length=64, null=False)
    description = models.CharField(max_length=128, blank=False, null=False, unique=True)

    def __str__(self):
        return f"{self.name} : {self.description}"


class Type(models.Model):
    name = models.CharField(max_length=64, null=False)
    nature = models.ForeignKey(Nature, null=False, on_delete=models.PROTECT, default=1)
    description = models.CharField(max_length=128, blank=False, null=False, unique=True)

    class Meta:
        ordering = ['nature','name']
                
    def __str__(self):
        return f"{self.name}({self.nature.__getattribute__("name")}) : {self.description}"


class Categorie(models.Model):
    name = models.CharField(max_length=64, null=False)
    nature = models.ForeignKey(Nature, null=False, on_delete=models.PROTECT, default=1)
    type = models.ForeignKey(Type, null=False, on_delete=models.PROTECT, default=1)
    description = models.CharField(max_length=128, blank=False, null=False, unique=True)
    
    class Meta:
            ordering = ['type','name']

    def __str__(self):
        return f"{self.name} ({self.type.__getattribute__("name")}) : {self.description}"
    

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
    nature = models.ForeignKey(Nature, null=False, on_delete=models.PROTECT, default=1)
    type = models.ForeignKey(Type, null=False, on_delete=models.PROTECT, default=1)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.PROTECT)
    description = models.CharField(max_length=128, blank=True)
    content = models.TextField(blank=False, null=False, unique=True)

    class Meta:
        ordering = ['type', 'categorie','name']

    def __str__(self):
        return f"{self.name} ({self.type.__getattribute__("name")}, {self.categorie.__getattribute__("name")} ) : {self.description}"


class Media(models.Model):
    MEDIA_TYPES = {
        "DOC" : "Document",
        "IMG" : "Image",
        "AUD" : "Audio",
        "VID" : "Video",
        "DEFAULT" : "Unset"
    }

# TO DO : create a fonction to figure out file type 
# if value not provided in type(choices=MEDIA_TYPES, null=False, default=type_value())
# or create TABLE with that function linked to every other tables AS FOREIGN KEY

    """ def type_value():

        file = ""
        if file.__getattribute__("format"):
            return  """

    name = models.CharField(max_length=64, null=False)
    nature = models.ForeignKey(Nature, null=False, on_delete=models.PROTECT, default=1)
    type = models.ForeignKey(Type, null=False, on_delete=models.PROTECT, default=1)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.PROTECT)
    description = models.CharField(max_length=128, null=False)
    path = models.CharField(null=True, unique=True, error_messages={"double" : "File already exists in database"}, help_text="Please, indicate a path or url." )
    
    class Meta:
            ordering = ['type', 'categorie','name']
    
    def __str__(self):
        return f"{self.name} ({self.type.__getattribute__("name")}, {self.categorie.__getattribute__("name")} ) : {self.description}"


class Link(models.Model):
    link_types = {
        "TXT" : "Hypertext",
        "MEDIA" : "Media",
        "URL" : "Website",
        }
    
    name = models.CharField(max_length=64, blank=True, default="Type de lien")
    nature = models.ForeignKey(Nature, null=False, on_delete=models.PROTECT, default=1)
    type = models.ForeignKey(Type, null=False, on_delete=models.PROTECT, default=1)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.PROTECT)
    label = models.ForeignKey(Text, max_length=128, null=False, default="undefined-link", on_delete=models.PROTECT)
    description = models.CharField(max_length=128, null=False)
    path = models.CharField(null=False, unique=True, error_messages={"double" : "File already exists in database"}, help_text="Please, indicate a path or url." )
    target = models.ForeignKey("Bloc", on_delete=models.CASCADE, null=True )

    class Meta:
        ordering = ['type', 'categorie','name']
    
    def __str__(self):
        return f"{self.name} ({self.type.__getattribute__("name")}, {self.categorie.__getattribute__("name")} ) : {self.description}"



class Page(models.Model):
    NATURE = {
        "WEB" : "Format Web",
        "DOC" : "Format Papier",
        "DEFAULT" : "Unset"
    } 

    TYPES = {
        "ART" : "Article",
        "NOTE" : "Note",
        "FORM" : "Formulaire",
        "DEFAULT" : "Unset"
    }

    name = models.CharField(max_length=64, null=False, unique=True)
    nature = models.ForeignKey(Nature, null=False, on_delete=models.PROTECT, default=1)
    type = models.ForeignKey(Type, null=False, on_delete=models.PROTECT, default=1)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.PROTECT)
    description = models.TextField(max_length=128, blank=False, null=False, unique=True)
    sections = models.ManyToManyField(
        symmetrical=False,
        related_name="used_in", 
        to="Section")

    class Meta:
        ordering = ['type', 'categorie','name']

    def __str__(self):
        return f"{self.name} ({self.type.__getattribute__("name")}, {self.categorie.__getattribute__("name")} ) : {self.description}"
    


class Section(models.Model):
    SECTION_TYPES = {
        "PRIMARY" : "Main Content",
        "SECOND" : "Secondary Content",
        "MANDATORY" : "Mandatory Content",
        "ADD" : "Suggested Content",
        "DEFAULT" : "Unset"
    } 

    name = models.CharField(max_length=64, blank=False, null=False, unique=True)
    nature = models.ForeignKey(Nature, null=False, on_delete=models.PROTECT, default=1)
    type = models.ForeignKey(Type, null=False, on_delete=models.PROTECT, default=1)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.PROTECT)
    title = models.CharField(max_length=64, blank=False, null=False, unique=True, error_messages={"double" : "File already exists in database"} )
    subtitle = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(max_length=128, blank=False, null=False, unique=True)
    components = models.ManyToManyField(
        to="Bloc",
        symmetrical=False,
        related_name="used_in")

    class Meta:
        ordering = ['type', 'categorie','name']

    def __str__(self):
        return f"{self.name} ({self.type.__getattribute__("name")}, {self.categorie.__getattribute__("name")} ) : {self.description}"



class Bloc(models.Model):
    BLOC_TYPES = {
        "HEADER" : "Header",
        "MENU" : "Menu",
        "LABEL" : "Label",
        "CTA" : "Call To Action",
        "DEFAULT" : "Unset"
    }

    name = models.CharField(max_length=64, null=False)
    nature = models.ForeignKey(Nature, null=False, on_delete=models.PROTECT, default=1)
    type = models.ForeignKey(Type, null=False, on_delete=models.PROTECT, default=1)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.PROTECT)
    description = models.CharField(max_length=128, blank=False, null=False, unique=True)
    texts = models.ManyToManyField(Text, related_name="used_in")
    medias = models.ManyToManyField(Media, related_name="used_in")
    links = models.ManyToManyField(Link, related_name="used_in")
    pointer = models.ManyToManyField(Link, related_name="targets")

    class Meta:
        ordering = ['type', 'categorie','name']

    def __str__(self):
        return f"{self.name} ({self.type.__getattribute__("name")}, {self.categorie.__getattribute__("name")} ) : {self.description}"






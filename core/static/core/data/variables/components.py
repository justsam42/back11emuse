from core.static.core.data.variables.atoms import texts

medias = [
    {
        "name" : "brand-guidelines-11emuse", # format (Note 1)
        "nature" : "document",
        "type" : "guidelines",
        "categorie" : "business",
        "description" : "Guide communication de l'organisation La Onzième Muse",
        "value" :"Ceci est le path absolu d'un link"
    },
    {
        "name" : "brandLogo-11emuse", # format (Note 1)
        "nature" : "pictural",
        "type" : "image",
        "categorie" : "logo",
        "description" : "Logo de l'organisation La Onzième Muse",
        "value" :"Ceci est le path absolu d'un link"
    },
    {
        "name" : "brandLogo-11emuse", # format (Note 1)
        "nature" : "sonore",
        "type" : "musical",
        "categorie" : "opening",
        "description" : "Musique du générique d'ouverture de OTP",
        "value" :"Ceci est le path absolu d'un link"
    },
    {
        "name" : "brandLogo-11emuse", # format (Note 1)
        "nature" : "motion",
        "type" : "video",
        "categorie" : "game scene",
        "description" : "Cinématique d'ouverture de OTP",
        "value" :"Ceci est le path absolu d'un link"
    },
]

components = [
    { 
        "name" : "commentaire1-homePage-website-11emuse", # format (Note 5)
        "nature" : "feedback",
        "type" : "users",
        "categorie" : "reviews",
        "description" : "social proof - commentaires - homepage - website 11emuse",
        "value" : [  
            texts[1], 
            texts[3]
        ]   # Note 3 : Content Acces -- > les texts ? 
    },
    { 
        "name" : "hero-homePage-website-11emuse", # format (Note 5)
        "nature" : "header",
        "type" : "primary content",
        "categorie" : "hero",
        "description" : "hero section - homepage - website 11emuse",
        "value" : [  
            texts[1], 
            texts[3]
        ]   # Note 3 : Content Acces -- > les texts ? 
    },
    { 
        "name" : "columnFlexbox-buttons", # format (Note 5)
        "nature" : "interactive",
        "type" : "user",
        "categorie" : "Call to Action",
        "description" : "colomne de buttons pour website",
        "value" : [  
            texts[1], 
            texts[3]
        ]   # Note 3 : Content Acces -- > les texts ? 
    },
    {
        "name" : "website-link-11emuse", # format (Note 1)
        "nature" : "link",
        "type" : "navigation",
        "categorie" : "website",
        "description" : "Lien vers le site de la 11ème muse",
        "value" : [
            texts[7], 
            texts[3]
        ]
    },
]

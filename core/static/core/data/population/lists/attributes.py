LISTS = {
    "document_types_file" : ["txt", "doc", "pdf", "odt"],
    "struct_types_file" : ["dict", "sql", "csv", "json", "html", "xml"],
    "image_types_file" : ["png", "jpeg", "bmp"],
    "audio_types_file" : ["mp3", "mp4", "wav"],
    "video_types_file" : ["mp4", "avi", "mkv"],
    "web_types_file" : ["html", "webp", "webv"],
}


attributes = [
    #---------------------distinctive property attributes
    { 
        "name" : "first_name", 
        "nature" : "variable",
        "type" : "string", 
        "classe" : "word", 
        "categorie": "name", 
        "description" : "" 
    },
    { 
        "name" : "last_name", 
        "nature" : "variable", 
        "type" : "string", 
        "classe" : "word", 
        "categorie": "name", 
        "description" : "" 
    },
 #---------------------state property attributes
    { 
        "name" : "xml", 
        "nature" : "file", 
        "type" : "media", 
        "classe": "document",
        "categorie" : "data structure", 
        "description" : "" 
    },
    { 
        "name" : "html", 
        "nature" : "file",  
        "type" : "media", 
        "classe": "document", 
        "categorie" : "data structure", 
        "description" : "" 
    },
    { 
        "name" : "json", 
        "nature" : "file",  
        "type" : "media", 
        "classe": "document", 
        "categorie" : "data structure", 
        "description" : "" 
    },

 #---------------------visaual property attributes

    { 
        "name" : "jpeg", 
        "nature" : "file",  
        "type" : "media", 
        "classe": "image", 
        "description" : "" 
    },
    { 
        "name" : "png", 
        "nature" : "file",  
        "type" : "media", 
        "classe": "image", 
        "description" : "" 
    },
    { 
        "name" : "bmp", 
        "nature" : "file",  
        "type" : "media", 
        "classe": "image", 
        "description" : "" 
    },

    #---------------------motion property attributes
    { 
        "name" : "gif", 
        "nature" : "file",  
        "type" : "media", 
        "classe": "video", 
        "description" : "" 
    },
    { 
        "name" : "mkv", 
        "nature" : "file", 
        "type" : "media", 
        "classe": "video", 
        "description" : "" 
    },
    { 
        "name" : "avi", 
        "nature" : "file", 
        "type" : "media", 
        "classe": "video", 
        "description" : "" 
    },
    { 
        "name" : "mp4", 
        "nature" : "file",  
        "type" : "media", 
        "classe": "video", 
        "description" : "" 
    },

 #---------------------audio property attributes
    { 
        "name" : "mp3", 
        "nature" : "file",
        "type" : "media", 
        "classe": "video", 
        "description" : "" 
    },
    { 
        "name" : "mp4", 
        "nature" : "file",  
        "type" : "media", 
        "classe": "video", 
        "description" : "" 
    },
    { 
        "name" : "wav", 
        "nature" : "file", 
        "type" : "media", 
        "classe": "video", 
        "description" : "" 
    },

 #---------------------multimedia property attributes
    { 
        "name" : "doc", 
        "nature" : "file", 
        "type" : "media", 
        "classe": "video", 
        "description" : "" 
    },
    { 
        "name" : "pdf", 
        "nature" : "file", 
        "type" : "media", 
        "classe": "video", 
        "description" : "" 
    },
    { 
        "name" : "website", 
        "nature" : "file", 
        "type" : "html", 
        "classe": "web", 
        "description" : "" 
    },
    { 
        "name" : "webapp", 
        "nature" : "file", 
        "type" : "html", 
        "classe": "web", 
        "description" : "" 
    },


    #---------------------location property attributes
    { 
        "name" : "coordinates", 
        "nature" : "variable", 
        "type" : "dict", 
        "classe": "location", 
        "categorie": "address", 
        "description" : "" 
    },
    { 
        "name" : "postal", 
        "nature" : "variable", 
        "type" : "string", 
        "classe": "location", 
        "categorie": "address", 
        "description" : "" 
    },
    { 
        "name" : "url", 
        "nature" : "variable", 
        "type" : "string", 
        "classe": "location", 
        "categorie": "address", 
        "description" : "" 
    },
    { 
        "name" : "hypertext",
        "nature" : "variable", 
        "string" : "dict", 
        "classe": "location", 
        "categorie": "address", 
        "description" : "" 
    },
]
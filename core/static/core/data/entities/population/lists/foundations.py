value_nature = [
    { "name" : "variable", "description" : "" },
    { "name" : "function", "description" : "" },
    { "name" : "file", "description" : "" },
]

value_type = [
    { "name" : "int", "nature" : "variable", "description" : "" },
    { "name" : "char", "nature" : "variable", "description" : "" },
    { "name" : "string", "nature" : "variable", "description" : "" },
    { "name" : "list", "nature" : "variable", "description" : "" },
    { "name" : "dict", "nature" : "variable", "description" : "" },
# objects au dessus des data
    { "name" : "media", "nature" : "file", "description" : "" },
  
       
]

LISTS = {
            "document_types_file" : ["txt", "doc", "pdf", "odt"],
            "struct_types_file" : ["dict", "sql", "csv", "json", "html", "xml"],
            "image_types_file" : ["png", "jpeg", "bmp"],
            "audio_types_file" : ["mp3", "mp4", "wav"],
            "video_types_file" : ["mp4", "avi", "mkv"],
            "web_types_file" : ["html", "webp", "webv"],
        }

my_classes = [
#----------------------------string var
    { "name" : "character", "nature" : "variable", "type" :"string", "description" : "" },
    { "name" : "word", "nature" : "variable", "type" : "string", "description" : "" },
    { "name" : "sentence", "nature" : "variable", "type" : "list", "description" : "" },
    { "name" : "paragraph", "nature" : "variable", "type" :"list", "description" : "" },
    { "name" : "texte", "nature" : "file", "type" : "list", "description" : "" },
#----------------------------dict var
    { "name" : "alphabet", "nature" : "file", "type" : "dict", "description" : "" },

    

#----------------------------media file var
    { "name" : "image", "nature" : "file", "type" : "media", "description" : "" },
    { "name" : "audio", "nature" : "file", "type" : "media", "description" : "" },
    { "name" : "video", "nature" : "file", "type" : "media", "description" : "" },
    { "name" : "document", "nature" : "file", "type" : "media", "description" : "" },
    { "name" : "web", "nature" : "file", "type" :"html", "description" : "" },

#----------------------------attribute dict var
    { "name" : "state", "nature" : "variable", "type" : "dict", "description" : "" },
    { "name" : "location", "nature" : "variable", "type" : "dict", "description" : "" },
    { "name" : "relation", "nature" : "variable", "type" : "dict", "description" : "" },
]

categories = [
      #----------------------------lexical attributes var
    { "name" : "name", "nature" : "variable", "type" : "string", "classe" : "word", "description" : "" },
    { "name" : "label", "nature" : "variable", "type" : "string", "classe" : "sentence", "description" : "" },
    { "name" : "title", "nature" : "variable", "type" : "string", "classe": "sentence", "description" : "" },
    { "name" : "catchphrase", "nature" : "variable", "type" : "string", "classe": "sentence", "description" : "" },
    { "name" : "summary", "nature" : "variable", "type" : "list", "classe": "text", "description" : "" },

    #----------------------------state attribute dict var
    { "name" : "romain", "nature" : "variable", "type" : "dict", "classe": "alphabet", "description" : "" },
    
    #----------------------------location attributes var
    { "name" : "path", "nature" : "variable", "type" : "dict", "classe": "relation", "description" : "" },
    { "name" : "address", "nature" : "variable", "type" : "dict", "classe": "relation", "description" : "" },
    { "name" : "navigation", "nature" : "variable", "type" : "dict", "classe": "relation", "description" : "" },
    { "name" : "upload", "nature" : "variable", "type" : "dict", "classe": "relation", "description" : "" },
    { "name" : "download", "nature" : "variable", "type" : "dict", "classe": "relation", "description" : "" },

    
]

attributes = [
    #---------------------distinctive property attributes
    { "name" : "first_name", "nature" : "variable","type" : "string", "classe" : "word", "categorie": "name", "description" : "" },
    { "name" : "last_name", "nature" : "variable", "type" : "string", "classe" : "word", "categorie": "name", "description" : "" },

 #---------------------state property attributes
    { "name" : "xml", "nature" : "file", "type" : "media", "classe": "document", "description" : "" },
    { "name" : "html", "nature" : "file",  "type" : "media", "classe": "document", "description" : "" },
    { "name" : "json", "nature" : "file",  "type" : "media", "classe": "document", "description" : "" },

 #---------------------visaual property attributes
    { "name" : "jpeg", "nature" : "file",  "type" : "media", "classe": "image", "description" : "" },
    { "name" : "png", "nature" : "file",  "type" : "media", "classe": "image", "description" : "" },
    { "name" : "bmp", "nature" : "file",  "type" : "media", "classe": "image", "description" : "" },

    #---------------------motion property attributes
    { "name" : "gif", "nature" : "file",  "type" : "media", "classe": "video", "description" : "" },
    { "name" : "mkv", "nature" : "file", "type" : "media", "classe": "video", "description" : "" },
    { "name" : "avi", "nature" : "file", "type" : "media", "classe": "video", "description" : "" },
    { "name" : "mp4", "nature" : "file",  "type" : "media", "classe": "video", "description" : "" },

 #---------------------audio property attributes
    { "name" : "mp3", "nature" : "file", "type" : "media", "classe": "video", "description" : "" },
    { "name" : "mp4", "nature" : "file",  "type" : "media", "classe": "video", "description" : "" },
    { "name" : "wav", "nature" : "file", "type" : "media", "classe": "video", "description" : "" },

 #---------------------multimedia property attributes
    { "name" : "doc", "nature" : "file", "type" : "media", "classe": "video", "description" : "" },
    { "name" : "pdf", "nature" : "file", "type" : "media", "classe": "video", "description" : "" },
    
    { "name" : "website", "nature" : "file", "type" : "html", "classe": "web", "description" : "" },
    { "name" : "webapp", "nature" : "file", "type" : "html", "classe": "web", "description" : "" },


    #---------------------location property attributes
    { "name" : "coordinates", "nature" : "variable", "type" : "dict", "classe": "location", "categorie": "address", "description" : "" },
    { "name" : "postal", "nature" : "variable", "type" : "string", "classe": "location", "categorie": "address", "description" : "" },
    { "name" : "url", "nature" : "variable", "type" : "string", "classe": "location", "categorie": "address", "description" : "" },
    { "name" : "hypertext", "nature" : "variable", "string" : "dict", "classe": "location", "categorie": "address", "description" : "" },

]
character = {
    "meta-data" : {
        "var_type" : "char",
        "var_size" : 8
    },
    "attributes" : {
        "id" : "",
        "name" : "roman-alphabet-letter-6",
        "description" : "Sixième lettre de l'alphabet romain, appelée 'f' ou 'F' en majuscule",
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
        ],
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
    "value" : {
        "unicode" : "",
        "hexadecimal" : "",
        "ASCII" : "",
        "binary" : "",
        "representations" : {
            "parsers" : [], 
            "dictionnaries" : ["roman-alphabet[6]", "some-other-dict"], 
            "libraries" : []
        }
    },
}

word = {
    "meta-data" : {
        "var_super" : "char",
        "var_type" : ["list", "str"],
        "var_size" : "varsize(str)",
    },
    "attributes" : {
        "id" : "",
        "name" : "Fatou",
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
        ],
        "position" : {
            "grid" : {
                "start_col" : character[0]["attributes"]["position"]["grid"],
                "end_col" : character[-1]["attributes"]["position"]["grid"],
                "start_line" : character[0]["attributes"]["position"]["grid"],
                "end_line" : character[-1]["attributes"]["position"]["grid"],
            }
        },   
        "chars_count" : [character["value"], character["value"], character["value"],].__len__(),
        "style" : {},
    },
    "value" : [character["value"], 'a', 56, '\n', "symbol"],   
}

sentence = {
    "meta-data" : {
        "var_super" : ["str", "list"],
        "var_type" : ["list", "str"],
        "var_size" : word*3,
        "data_nature" : "litterary",
        "data_type" : "string",
        "categorie" : "string",
    },
    "attributes" : {
        "id" : "",
        "name" : "mon-titre",
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
        ],
        "position" : {
            "start_line" : 1,
            "end_line" : 1
        },
        "signs_count" : 0,
        "words_count" : 0,
        "style" : {},
    }, 
    "value" : [word, word, "Fatou", word] 
}

paragraphe = {
    "meta-data" : {
        "var_super" : ["str", "list"],
        "data_nature" : "litterary",
        "data_type" : "string",
        "categorie" : "short-text",
        "file_format" : ".txt",
        "export_as" : [".txt",".pdf", ".html", ".json", ".xml"]
    },
    "attributes" : {
        "id" : "",
        "name" : "$truc",
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
        ],
        "position" : {
            "start_line" : 1,
            "end_line" : 1
        },      
        "signs_count" : 0,
        "spaces_count" : 0,
        "new_line_count" : 0

    },
    "value" : [sentence, word, sentence, "Fatou", sentence],    
}

text = {
    "meta-data" : {
        "var_super" : ["str", "list"],      
        "data_nature" : "litterary",
        "data_type" : "string",
        "categorie" : "text",
        "file_format" : ".txt",
        "file_type" : "document",
        "export_as" : [".txt",".pdf", ".html", ".json", ".xml"]
    },
    "attributs" : {
        "id" : "",
        "name" : "ma bio",
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
        ],
        "position" : {
            "start_line" : 1,
            "end_line" : 1
        },      
        "style" : {},
    },
    "value" : [character, word, sentence, paragraphe, "Fatou", paragraphe,paragraphe],
}

# Retour au plus petit constituant ou atom ou unit d'un objet composé
# qui en l'occurence est commposé que d'une recursion d'objet composé 
# par ce constitant premier {char}
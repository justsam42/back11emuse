from  core.static.core.data.variables import blocs

sections = [
    {
        "meta-data" : {
            "section_nature" : "header",
            "section_type" : "actionnable",
            "categorie" : "menu",
        },
        "attributes" : {
            "id" : "objectId",
            "name" : "website-11emuse-header-menu", # format (Note 5)
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
            blocs[1],
            blocs[1],
            blocs[1]
        ]
    },
    {
        "meta-data" : {
            "section_nature" : "primary content",
            "section_type" : "landing",
            "categorie" : "hero",
        },
        "attributes" : {
            "id" : "objectId",
            "name" : "website-11emuse-home-button-logo", # format (Note 5)
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
            blocs[2],
            blocs[2],
            blocs[2]
        ]
    }
]


# ------------Note 5 : "format des objets du Design system"
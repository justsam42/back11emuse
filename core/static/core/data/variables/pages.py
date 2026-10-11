from core.static.core.data.variables import sections

pages = [
    {
        "meta-data" : {
            "page_nature" : "interactive",
            "page_type" : "website",
            "categorie" : "index",
        },
        "attributes" : {
            "id" : "objectId",
            "name" : "website-11emuse-index-page", # format (Note 5)
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
        "value" :[
            sections[1],
            sections[2],
            sections[3]
        ]
    },
    {
        "meta-data" : {
            "page_nature" : "interactive",
            "page_type" : "website",
            "categorie" : "services",
        },
        "attributes" : {
            "id" : "objectId",
            "name" : "website-11emuse-services-page", # format (Note 5)
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
        "value" :[
            sections[1],
            sections[2],
            sections[3]
        ]
    }
]


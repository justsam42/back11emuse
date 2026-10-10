texts = {
    1 : {
        "name" : "",
        "categorie" : "catchPhrase",
        "content" : ""
    },
}

medias = {
    1: {
        "name" : "",
        "categorie" : "",
        "path" : "",
        "description" : ""
    },
}

links = {
    1 : {
        "name" : "",
        "label" : "",
        "description" : "",
        "targetId" : ""
    }
}

blocs = {
    1 : {
        "name" : "focus1",
        "type" : "",
        "texts" : [],
        "medias" : [],
        "links" : []
    }
}

sections = {
    1 : {
        "name" : "landing",
        "title" : "",
        "subtitle" : "",
        "content" : [blocs[1],blocs[2],blocs[3]]
    },
    2 : {
        "name" : "scrolling",
        "title" : "",
        "subtitle" : "",
        "content" : [blocs[4],blocs[5],blocs[6], blocs[7]]
    },
    3: {
        "name" : "highlight",
        "tile" : "",
        "subtitle" : "",
        "content" : [blocs[8]]
    }
}


indexContext = {
    "name" : "",
    "title" : "",
    "description" : "",
    "content" :{
        1 : sections[1],
        2 : sections[2],
        3 : sections[3] 
    }
}

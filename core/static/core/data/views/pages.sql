CREATE TABLE "atoms" ();
CREATE TABLE "blocs" ();
CREATE TABLE "relations" (
    "id",
    "name", 
    "nature",
    "type",
    "objetA.id",
    "ObjetB.id"
);

-- Un bloc est un grouping de plusieurs {atoms} en une instance de {bloc}.
-- Un {bloc} étant constitué des mêmes {attributs} qu'un {atom} :
-- il aura les mêmes champs qu'une {entity} leur parent commun   



CREATE VIEW "blocs" AS
    SELECT "bloc_id" FROM "id", "name", "nature", "type", "categorie"
    FROM "atoms"
    LEFT JOIN "atoms" ON "atoms.id" = "atoms.id"
    GROUP BY "bloc_id" DESC;
@ECHO OFF

IF EXIST fisier.sql DEL fisier.sql
SET PGPASSWORD=maria

ECHO Realizam procesarea tabelelor


(FOR %%t IN ("aplicatia_mea_categorie" "aplicatia_mea_furnizor" "aplicatia_mea_parfum" "aplicatia_mea_parfum_furnizori" "aplicatia_mea_compozitiaparfumului" "aplicatia_mea_stoc" "aplicatia_mea_vanzarizilnice") DO (
    ECHO Tabelul %%t

    "C:\Program Files\PostgreSQL\18\bin\pg_dump.exe" --column-inserts --data-only --inserts -h localhost -U maria -p 5432 -d proiectparfum -t %%t >> fisier.sql
))

SET PGPASSWORD=
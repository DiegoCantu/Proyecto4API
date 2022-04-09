Instalar la librerias del proyecto (Flask, SQL Alchemy, etc):
pip install -r requirement.txt

Ejecutar la aplicación desde Visual Studio Code:

py -3 -m venv venv

. venv/Scripts/activate

--
Seleccionar la terminal virtual:
View
Command Palette
Python:Select Interpreter
Python <Version> ('venv')
--

Establecer la variable de ambiente del server y ejecutarlo:
set FLASK_ENV=development
set FLASK_APP=ArchivoPython.py
$env:FLASK_APP = "ArchivoPython.py"
flask run

Ejecutar la aplicación desde PyCharm:
1.Abrir la configuración de Run/Debug
2.Establecer el Script Path: C:\Users\<SuUsuario>\PycharmProjects\Proyecto4API\app.py
3.Establecer las variables de ambiente: PYTHONUNBUFFERED=1;FLASK_APP=app.py;FLASK_ENV=development;FLASK_DEBUG=1
4.Seleccionar un interprete para Python: Selecciona una versión de Python instalada

Abrir la url generada en la linea de comandos:
LOCALHOST = http://127.0.0.1:5000/

1. Guarda las predicciones que generaste en tu proyecto 3 en una tabla en una base de datos de Postgres.

POST:
LOCALHOST/predictions

Body:
{
    "predicciones": [
        {
            "data": { <DATA> ,  "date": "2022-04-07"}
        },
        {
            "data": { <DATA> ,  "date": "2022-04-11"}
        }
    ]
}

Response:

{
    "body": "Predicciones guardadas correctamente",
    "statusCode": 201
}

Estructura de la tabla en postgressql:
CREATE TABLE public."PrediccionesTbl"
(
    "Id" integer NOT NULL DEFAULT nextval('"PrediccionesTbl_Id_seq"'::regclass),
    "Data" json,
    "Date" date,
    CONSTRAINT "PrediccionesTbl_pkey" PRIMARY KEY ("Id")
)

2. Genera el endpoint /prediction_id que recibe como parámetro el id de una inspección en la que estemos interesados
 en obtener su predicción y obtén su predicción de la tabla de predicciones correspondiente a la última fecha de la
 que tengas predicciones. La salida corresponde a un objeto json.

GET:
{LOCALHOST}/prediction_id/<int:prediction_id>
{LOCALHOST}/prediction_id/1

Ejemplo response:

{
    "prediction_by_id": [
        {
            "Data": {
                <DATA>
            },
            "Date": "Thu, 07 Apr 2022 00:00:00 GMT",
            "Id": 1
        }
    ]
}


3. Genera el endpoint /predictions_date que recibe como parámetro en la fecha en la que estás interesado en obtener
las predicciones. La salida corresponde a todas las predicciones correspondiente a la fecha seleccionada en formato json.

GET:
LOCALHOST/predictions_date/<predictions_date>
LOCALHOST/predictions_date/2022-04-07

Ejemplo response:

{
    "prediction_by_date": [
        {
            "Data": {
                <DATA>
            },
            "Date": "Thu, 07 Apr 2022 00:00:00 GMT",
            "Id": 1
        }
    ]
}

-app.py:
Aquí se encuentran los controladores/endpoints
-predicciones.database.py
Aquí se encuentra la conexión con la base de datos
-postgressql_connector.py
Aquí se encuentra la configuración de conexión a la base de datos postgressql

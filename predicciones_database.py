from sqlalchemy import text
import postressql_connector

engine = postressql_connector.engine()


def save_predictions(predictions):
    try:
        for prediction in predictions:
            tilde = "'"
            data = str("'") + str(prediction["data"]).replace(f'{tilde}', '"') + str("'")
            date = str("'") + str(prediction["data"]["date"]).replace(f'{tilde}', '"') + str("'")
            sqlstring = f'INSERT INTO public."PrediccionesTbl"("Data", "Date") VALUES ({data} , {date})'
            sqlquery = text(sqlstring)
            engine.execute(sqlquery)
    except Exception as e:
        return e
    return {'statusCode': 201, 'body': 'Predicciones guardadas correctamente'}


def get_prediction_by_id(prediction_id):
    sqlquery = text(f'''SELECT * FROM public."PrediccionesTbl" WHERE "Id" =  {prediction_id}''')
    results = engine.execute(sqlquery)
    return {"prediction_by_id": map_prediction(results)}


def get_predictions_by_date(predictions_date):
    sqlquery = text(f'''SELECT * FROM public."PrediccionesTbl" WHERE "Date" = '{str(predictions_date)}' ''')
    results = engine.execute(sqlquery)
    return {"prediction_by_date": map_prediction(results)}


def map_prediction(results):
    data = []
    for result in results:
        data.append(dict(result))
    return data



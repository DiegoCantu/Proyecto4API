from sqlalchemy import create_engine

user = "postgres"
password = "postgress12"
host = "localhost"
port = "5432"
database = "Predicciones"


def engine():
    db_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    db = create_engine(db_string)
    return db

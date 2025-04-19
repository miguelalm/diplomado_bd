import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="",
        host="localhost",
        port="15432",
        options="-c search_path=dbo,diplomado"
    )
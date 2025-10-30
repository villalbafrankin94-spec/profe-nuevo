from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            host="db",
            database="mydb",
            user="user",
            password="pass"
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Conexión exitosa a PostgreSQL: {db_version[0]}"
    except Exception as e:
        return f"Error al conectar con la base de datos: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

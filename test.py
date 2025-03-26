import psycopg2
from flask import Flask

app = Flask(__name__)

DB_HOST = 'db'  
DB_NAME = 'week1'
DB_USER = 'postgres'
DB_PASSWORD = 'root'


def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD, port="5432")
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    records = cur.fetchall()
    cur.close()
    conn.close()
    return f'Database records: {records}'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

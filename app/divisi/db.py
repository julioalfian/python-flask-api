import json
from app.conn.conn import connection
class db:
    def get_all_divisi():
        cursor = connection.cursor()

        cursor.execute('SELECT divisi.id, divisi.nama FROM divisi')
        data = cursor.fetchall()
        return data

    def delete_divisi(id):
        cursor = connection.cursor()

        cursor.execute('DELETE FROM divisi WHERE divisi.id=%s', (id))
        connection.commit()
        return {"status":True}

    def add_divisi(json):
        cursor = connection.cursor()

        cursor.execute('INSERT INTO divisi (nama) VALUES (%s)', (json['nama']))
        connection.commit()
        return {"status":True}

    def update_divisi(json):
        cursor = connection.cursor()

        cursor.execute('UPDATE divisi SET nama=%s WHERE divisi.id=%s', (json['nama'], json['id']))
        connection.commit()
        return {"status":True}
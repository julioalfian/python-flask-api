import json
from app.conn.conn import connection
class db:
    def get_all_pegawai():
        cursor = connection.cursor()

        cursor.execute('SELECT pegawai.id, pegawai.nama, divisi.nama FROM pegawai JOIN divisi ON divisi.id=pegawai.id_divisi')
        data = cursor.fetchall()
        return data

    def delete_pegawai(id):
        cursor = connection.cursor()

        cursor.execute('DELETE FROM pegawai WHERE pegawai.id=%s', (id))
        connection.commit()
        return {"status":True}

    def add_pegawai(json):
        # print(json['nama'])
        cursor = connection.cursor()

        cursor.execute('INSERT INTO pegawai (nama, id_divisi) VALUES (%s, %s)', (json['nama'], json['id_divisi']))
        connection.commit()
        return {"status":True}

    def update_pegawai(json):
        # print(json['nama'])
        cursor = connection.cursor()

        cursor.execute('UPDATE pegawai SET nama=%s, id_divisi=%s WHERE pegawai.id=%s', (json['nama'], json['id_divisi'], json['id']))
        connection.commit()
        return {"status":True}
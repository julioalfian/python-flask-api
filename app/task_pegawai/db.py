import json
from app.conn.conn import connection
class db:
    def get_all_task_pegawai():
        cursor = connection.cursor()

        cursor.execute('SELECT id, id_pegawai, id_task FROM task_pegawai')
        data = cursor.fetchall()
        return data

    def delete_task_pegawai(id):
        cursor = connection.cursor()

        cursor.execute('DELETE FROM task_pegawai WHERE task_pegawai.id=%s', (id))
        connection.commit()
        return {"status":True}

    def add_task_pegawai(json):
        cursor = connection.cursor()

        cursor.execute('INSERT INTO task_pegawai (id_pegawai, id_task) VALUES (%s, %s)', (json['id_pegawai'], json['id_task']))
        connection.commit()
        return {"status":True}

    def update_task_pegawai(json):
        cursor = connection.cursor()

        cursor.execute('UPDATE task_pegawai SET id_pegawai=%s, id_task=%s WHERE task_pegawai.id=%s', (json['id_pegawai'], json['id_task'], json['id']))
        connection.commit()
        return {"status":True}
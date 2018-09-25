import json
from app.conn.conn import connection
class db:
    def get_all_task():
        cursor = connection.cursor()

        cursor.execute('SELECT id, id_status, deskripsi FROM task')
        data = cursor.fetchall()
        return data

    def delete_task(id):
        cursor = connection.cursor()

        cursor.execute('DELETE FROM task WHERE task.id=%s', (id))
        connection.commit()
        return {"status":True}

    def add_task(json):
        cursor = connection.cursor()

        cursor.execute('INSERT INTO task (id_status, deskripsi) VALUES (%s, %s)', (json['id_status'], json['deskripsi']))
        connection.commit()
        return {"status":True}

    def update_task(json):
        cursor = connection.cursor()

        cursor.execute('UPDATE task SET id_status=%s, deskripsi=%s WHERE task.id=%s', (json['id_status'], json['deskripsi'], json['id']))
        connection.commit()
        return {"status":True}
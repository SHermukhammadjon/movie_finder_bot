import sqlite3
from picsum import now

class Database:
    def __init__(self, file_name):
        self.name = file_name

    def conect(self, movies_tb = 'movies_data', user_tb = 'users_data', admin_tb = 'admins_data', movies_note = "movies_note"):
        """
        """
        self.movies = movies_tb
        self.users = user_tb
        
        self.admin = admin_tb
        self.m_note = movies_note

        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.movies} ('id' INTEGER PRIMARY KEY, 'file_id', 'title', 'caption', 'file_size' INTEGER );")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.m_note} ('id' INTEGER PRIMARY KEY, 'file_id', 'caption', 'file_size' INTEGER);")

        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.users} ('user_id' INTEGER , 'user_name', 'lang', 'registred');")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.admin} ('id' INTEGER , 'name', 'lang', 'registred');")

        conection.commit()
        conection.close()
        print(f"database sucsesfuly conected...")

    def add_movi_note(self, caption, movie_id = None, size = 0, file_id = None):
        """_summary_

        Args:
            caption (_type_): _description_
            movie_id (_type_, optional): _description_. Defaults to None.
            size (int, optional): _description_. Defaults to 0.
            file_id (_type_, optional): _description_. Defaults to None.
        """
        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()

        try:
            caption = caption.replace('"', "\'")
            match = f"INSERT INTO {self.m_note} ('id', 'file_id', 'caption', 'file_size') VALUES ({movie_id}, {file_id}, '{caption}', '{file_id}');)"
            cursor.execute(match)
            print("New movi added ...")
        except:
            print("Can't added {movie_id} ...")
        
        conection.commit()
        conection.close()

    def add_user(self, user_id = None, user_name = None, registr_time = None,lang = 'uz'):
        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()

        match = f"INSERT INTO users_data ('user_id', 'user_name', 'lang', 'registred') VALUES ({user_id}, '{user_name}', '{lang}', '{registr_time}');"
        cursor.execute(match.replace('"', "'"))
        print(f'{user_name} added sucsefuly database ...')

        conection.commit()
        conection.close()
    
    def remove_user(self, user_id):
        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()

        cursor.execute(f"DELETE FROM users_data WHERE user_id == {user_id};")
        
        conection.commit()
        conection.close()

    def get_users(self):
        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()
        users_data = {}

        match = f"SELECT * FROM {self.users};"
        for row in cursor.execute(match.replace('"', "'")):
            id, name, lang, registred_time = row[0], row[1], row[2], row[3]
            users_data[id] = {'name' : name, 'lang' : lang, 'where' : 'none', 'action' : 'none', 'registred' : registred_time}
            # print(row) 
        conection.commit()
        conection.close()

        return users_data
    
    def get_admins(self):
        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()
        users_data = {}

        match = f"SELECT * FROM {self.admin};"
        for row in cursor.execute(match.replace('"', "'")):
            id, name, lang, registred_time = row[0], row[1], row[2], row[3]
            users_data[id] = {'name' : name, 'lang' : lang, 'where' : 'none', 'action' : 'none', 'registred' : registred_time}
            # print(row) 
        conection.commit()
        conection.close()
        return users_data
    
    def check_user(self, user_id = None):
        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()

        respons = cursor.execute(f"SELECT user_id FROM {self.users} WHERE user_id == {user_id};").fetchall()
        
        conection.commit()
        conection.close()

        if len(respons) == 1:
            return True
        return False
    
    def add_admin(self, id = None, name = None, registred_time = None, lang = 'uz'):
        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()

        match = f"INSERT INTO {self.admin} ('id', 'name', 'lang', 'registred') VALUES ({id}, '{name}', '{lang}', '{registred_time}');"
        cursor.execute(match.replace('"', "'"))
        print(f'New admin {name} added sucsefuly database ...')

        conection.commit()
        conection.close()
    

if __name__ == '__main__':
    database = Database('database.db')
    database.conect()
    # database.add_movi('kino"', message_id = 1, size = 0, file_id = 'btenvu2g556ivn')
    # database.add_user(user_id=100, user_name='SHermukhmmad', registr_time = now())
    # a  = database.check_user(user_id = 0)
    # print(a)
    database.remove_user(user_id = 1661189380)
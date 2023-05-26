import sqlite3


class Database:
    def __init__(self, file_name):
        self.name = file_name

    def conect(self, movies_tb = 'movies_data', user_tb = 'users_data'):
        """
        """
        self.movies = movies_tb
        self.users = user_tb

        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.movies} ('message_id' INTEGER, 'file_id', 'caption', 'file_size' INTEGER, 'id' INTEGER PRIMARY KEY);")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.users} ('user_id' INTEGER , 'user_name', 'lang');")

        conection.commit()
        conection.close()
        print(f"database sucsesfuly conected...")

    def add_movi(self, caption, message_id = None, size = 0, file_id = None):
        """
            caption : str
            message_id : int
            size : int
            file_id : str
        """
        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()

        try:
            caption = caption.replace('"', "\'")
            cursor.execute(f"INSERT INTO {self.movies} ('message_id', 'file_id', 'caption', 'file_size') VALUES ({message_id}, '{file_id}', \"{caption}\", {size});")
            print("New movi added ...")
        except:
            print("Datbase Error ...")
        
        conection.commit()
        conection.close()

    def add_user(self, user_id = None, user_name = None, lang = 'uz'):
        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()

        match = f"INSERT INTO users_data ('user_id', 'user_name', 'lang') VALUES ({user_id}, '{user_name}', '{lang}');"
        cursor.execute(match.replace('"', "'"))
        print(f'{user_name} added sucsefuly database ...')

        conection.commit()
        conection.close()

    def get_users(self):
        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()
        users_data = {}

        match = f"SELECT * FROM {self.users};"
        for row in cursor.execute(match.replace('"', "'")):
            id, name, lang = row[0], row[1], row[2]
            users_data[id] = {'name' : name, 'lang' : lang, 'where' : 'head_menu', 'action' : 'none'}
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
    

if __name__ == '__main__':
    database = Database('database.db')
    database.conect()
    # database.add_movi('kino"', message_id = 1, size = 0, file_id = 'btenvu2g556ivn')
    # database.add_user(user_id=100, user_name='SHermukhmmad')
    a  = database.check_user(user_id = 0)
    print(a)
import csv 
from random import randint

def load_movi_data():
    line_count = 0
    titles = []
    movies_dataset = []
    with open('dataset/movies.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if line_count != 0:
                titles.append(row[5])
                movies_dataset.append({'caption' : row[2], 'file_id' : row[1], 'title' : row[5], 'id' : row[4], 'message_id' : row[0], 'photo' : row[6]})
            line_count+=1
    print("Movies databes sucsesfuly conected ...")
    return titles, movies_dataset, line_count


class RAM:
    def __init__(self, db = None):
        self.users_code = {}
        self.block_users = {}
        self.users_data = {}
        self.admin_data = {}
        self.db = db

    def block_user(self, user_id = None, clear_caount = False, count = False):
        if clear_caount:
            self.block_users[user_id] = 0
        if count:
            if self.block_users.get(user_id):
                return self.block_users[user_id]
            return 0
        
        if self.block_users.get(user_id):
            self.block_users[user_id] += 1
        else:
            self.block_users[user_id] = 1
        if self.block_users[user_id] > 3:
            return False
        return True

    def random_code(self, user_id):
        if self.users_code.get(user_id):
            return self.users_code[user_id]
        else:
            self.users_code[user_id] = str(randint(1000, 9999))
            return self.users_code[user_id]

    def load_users(self):
        try:
            self.users_data = self.db.get_users()
            return True
        except:
            return False

    def check_user(self, user_id = None):
        if self.users_data.get(user_id):
            return True
        return False

    def add_user(self, id = None, name = None, lang = 'uz'):
        self.users_data[id] = {'name' : name, 'lang' : lang, 'where' : 'head_menu', 'action' : 'none'}
        return True
    
    def check_admin(self, id = None):
        if self.admin_data.get(id):
            return True
        else:
            return False
    
    def get_action(self, user_id = None):
        return self.users_data[user_id]['action']
    
    def wher_user(self, user_id = None):
        return self.users_data[user_id]['where']

    def update_action(self, user_id = None, action = 'none'):
        self.users_data[user_id]['action'] = action
    
    def update_user_loc(self, user_id = None, where = 'head_menu'):
        self.users_data[user_id]['where'] = where


if __name__ == "__main__":
    titles, movies_dataset, line_count = load_movi_data()
    for title in movies_dataset[:10]:
        print(title['photo'])
    
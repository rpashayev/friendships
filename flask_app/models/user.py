from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = 'friendships_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.friends = []
    
    @classmethod
    def show_all_friendships(cls):
        all_users = []
        query = '''
            SELECT *
            FROM users
            JOIN friendships ON friendships.user_id = users.id
            JOIN users AS friends ON friends.id = friendships.friend_id
            ORDER BY users.first_name;
        '''
        
        result = connectToMySQL(cls.DB).query_db(query)
        for row in result:
            user = cls(row)
            friend_info = {
                'id': row['friends.id'],
                'first_name': row['friends.first_name'],
                'last_name': row['friends.last_name'],
                'created_at': row['friends.created_at'],
                'updated_at': row['friends.updated_at']
            }
            user.friends.append(cls(friend_info))
            all_users.append(user)
        return all_users
    
    @classmethod
    def add_user(cls, data):
        query = '''
            INSERT 
            INTO users(first_name, last_name)
            VALUES ( %(first_name)s, %(last_name)s );
        '''
        
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def show_all_users(cls):
        all_users = []
        query = '''
            SELECT *
            FROM users;
        '''
        result = connectToMySQL(cls.DB).query_db(query)
        
        for user in result:
            all_users.append(cls(user))
        return all_users
        
    @classmethod
    def new_friendship(cls, data):
        query = '''
            INSERT INTO friendships(user_id, friend_id)
            VALUES ( %(user_id)s, %(friend_id)s );
        '''
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def show_friendship_ids(cls):
        all_friendships = []
        query = '''
            SELECT *
            FROM friendships;
        '''
        result = connectToMySQL(cls.DB).query_db(query)
        
        for friendship in result:
            all_friendships.append(friendship)
        return all_friendships
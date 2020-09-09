from pymongo import MongoClient
from datetime import datetime
from utils import Config


class Database:
    def __init__(self, database='notes'):
        self.database = database

        self.mongo_config = Config('mongo.yml').read_config()
        host = self.mongo_config['host']
        port = self.mongo_config['port']
        self.client = MongoClient(host, port)

        self.notes_db = self.client['notes_db']
        self.notes = self.notes_db['notes']


class DatabaseWrite(Database):
    def __init__(self, tag, title, desc):
        Database.__init__(self)
        self.tag = tag
        self.title = title
        self.desc = desc

    def add_note(self):
        time = datetime.now()
        data = {
            "tag": self.tag,
            "title": self.title,
            "desc": self.desc,
            "time": time
        }
        self.notes.insert_one(data)


class DatabaseRead(Database):
    def __init__(self, **kwargs):
        Database.__init__(self)
        self.tag = kwargs.get('tag', None)
        self.title = kwargs.get('title', None)
        self.desc = kwargs.get('desc', None)

    def get_all_by_tag(self):
        return self.notes.find({"tag": self.tag})

    def read_all(self):
        return self.notes.find()

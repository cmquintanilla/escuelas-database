import pymongo
class MongoDB():

    def __init__(self, connectionString):
        self.connect(connectionString)

    def connect(self, connectionString):
        self.client = pymongo.MongoClient(connectionString, tls=True,tlsAllowInvalidCertificates=True)        
    
    def setDatabase(self, database):
        self.mydb = self.client[database]
        
    def setCollection(self, collection):
        self.collection = self.mydb[collection]
    
    def insert(self, dictionary):
        curs = self.collection.find().sort([("_id", -1)]).limit(1)
        maxID = ''
        for x in curs:
            maxID = str(int(x['_id']) + 1)
        maxID = "1" if maxID == '' else maxID 
        dictionary["_id"] = maxID
        x = self.collection.insert_one(dictionary)
        return x.inserted_id
    
    def find(self, query):
        self.document = self.collection.find(query)
    
    def update(self, query, set):
        self.document = self.collection.update_one(query, set)
    
    def delete(self, query):
        self.document = self.collection.delete_one(query)


from couchdb import Server



# server = Server() # connects to the local_server
# >>> remote_server = Server('http://example.com:5984/')
# >>> secure_remote_server = Server('https://username:password@example.com:5984/')

class db_server(object):

    def __init__(self,username,login):
        self.secure_server=Server('http://%s:%s@130.56.252.58:5984' %(username,login))
        self.db=self.secure_server["tweet"]

    def insert(self,data):
        try:
            doc_id,doc_rev=self.db.save(data)
        except Exception as e:
            with open('log','a') as f:
                f.write(str(e)+'\n')
                f.write((data['_id']+'\n'))

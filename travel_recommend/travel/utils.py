from pymongo import MongoClient

# DB접속 구현

def get_db_handle(db_name, host, port):
    client = MongoClient(host=host,
                         port=int(port),
                        )
    db_handle = client[db_name]
    return db_handle, client


def get_collection_handle(db_handle, collection_name):
    return db_handle[collection_name]
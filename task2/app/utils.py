from sqlalchemy import create_engine

def connect():
    #TODO move login info to dockerfile
    db_name = 'postgres'
    db_user = 'postgres'
    db_pass = 'postgres'
    db_host = 'postgres'
    db_port = '5432'
    db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
    return create_engine(db_string)

def get_db_result(query):
    """
    input: query - string with executable sql code

    output: result of query execution
    """
    db = connect()
    return db.execute(query)  

def query_to_dict(query):
    """
    input: query - result of query execution

    output: list with query result in dumpable format
    """
    result = []
    for r in query:
        row = {}
        for i in r.iterkeys():
            print(i, r[i])
            row[i] = r[i]
        result.append(row)
    return result
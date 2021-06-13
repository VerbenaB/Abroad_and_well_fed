import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None):
    connection = None
    results = []
    
    try:
        connection=psycopg2.connect("dbname='Italian_restaurants'")
        cursor = connection.cursor(cursor_factory=ext.DictCursor)   
        cursor.execute(sql, values)
        connection.commit()
        results = cursor.fetchall()
        cursor.close()           
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return results
import mariadb

def executeQuery(databasepath, query, commit):  
    try:
        connection = mariadb.connect( host     = databasepath.get('host'),
                                      port     = databasepath.get('port'),
                                      user     = databasepath.get('user'),
                                      password = databasepath.get('password'),
                                      database = databasepath.get('database'))        
        cursor = connection.cursor()
        cursor.execute(query)  

        if commit:
            connection.commit() 
            Result = 'Exito en la tarea'
        else:               
            Result = cursor.fetchall()   
     
        cursor.close()
        connection.close() 
        
        return Result

    except mariadb.Error as error:        
        return f'Error: {error}'
import mysql.connector
from datetime import datetime
from movieDbConnect import moviedb

class MoviesInfo:
    db=moviedb

    @staticmethod
    def add_movie_info(moviename, moviedate):
        connection = MoviesInfo.db
        formatted_date = datetime.strptime(moviedate, "%Y/%m/%d").date()        
        cursor = connection.cursor()
        sql = "INSERT INTO movieinfo (moviename, moviedate) VALUES (%s, %s)"
        values = (moviename, formatted_date)
        movieid = None
    
        try:
            cursor.execute(sql, values)
            connection.commit()
            movieid = cursor.lastrowid
        except mysql.connector.Error as er:
            print("Error: ", er)
        finally:
            cursor.close()


        return movieid


    @staticmethod
    def add_Director(directorname):
        connection = MoviesInfo.db
        cursor = connection.cursor()
        sql = "INSERT INTO directors (directorname) VALUES (%s)"
        values = (directorname,)
        directorid = None

        try:
            cursor.execute(sql, values)
            connection.commit()
            directorid = cursor.lastrowid
        except mysql.connector.Error as er:
            if er.errno == 1062:
                print(f"The director already exists: {directorname}")
            else:
                print("Error: ", er)
        finally:
            cursor.close()
            

        return directorid


    @staticmethod
    def add_Actor(actorname):
        connection = MoviesInfo.db
        cursor = connection.cursor()
        sql = "INSERT INTO actors (actorname) VALUES (%s)"
        values = (actorname,)
        actorid = None

        try:
            cursor.execute(sql, values)
            connection.commit()
            actorid = cursor.lastrowid
        except mysql.connector.Error as er:
            if er.errno == 1062:
                print(f"The actor already exists: {actorname}")
            else:
                print("Error: ", er)
        finally:
            cursor.close()
            

        return actorid
    

    @staticmethod
    def add_Movie_types(type):
        connection = MoviesInfo.db
        cursor = connection.cursor()
        sql = "INSERT INTO movietypes (type) VALUES (%s)"
        values = (type,)
        movie_type_id = None

        try:
            cursor.execute(sql, values)
            connection.commit()
            movie_type_id = cursor.lastrowid
        except mysql.connector.Error as er:
            if er.errno == 1062:
                print(f"The type already exists: {type}")
            else:
                print("Error: ", er)
        finally:
            cursor.close()
            

        return movie_type_id


    @staticmethod
    def add_movie_director(movie_id, director_id):
        connection = MoviesInfo.db
        cursor = connection.cursor()
        sql = "INSERT INTO moviedirector (movie, director) VALUES (%s, %s)"
        values = (movie_id, director_id)

        try:
            cursor.execute(sql, values)
            connection.commit()
        except mysql.connector.Error as er:
            print("Error: ", er) 
        finally:
            cursor.close()
           

    @staticmethod
    def add_movie_actor(movie_id, actor_id):
        connection = MoviesInfo.db
        cursor = connection.cursor()
        sql = "INSERT INTO movieactor (movie, actor) VALUES (%s, %s)"
        values = (movie_id, actor_id)

        try:
            cursor.execute(sql, values)
            connection.commit()
        except mysql.connector.Error as er:
            print("Error: ", er)
        finally:
            cursor.close()
            

    @staticmethod
    def add_movie_type_info(movie_id, type_id):
        connection = MoviesInfo.db
        cursor = connection.cursor()
        sql = "INSERT INTO movietypeinfo (movie, movietype) VALUES (%s, %s)"
        values = (movie_id, type_id)

        try:
            cursor.execute(sql, values)
            connection.commit()
        except mysql.connector.Error as er:
            print("Error: ", er)
        finally:
            cursor.close()
            
class MoviesUptade:

    db=moviedb
    
    @staticmethod
    def update_movie_info(moviename, moviedate, id):
        connection = MoviesUptade.db
        cursor = connection.cursor()
        formatted_date = datetime.strptime(moviedate, "%Y/%m/%d").date()        
        sql = "UPDATE movieinfo SET moviename = %s, moviedate = %s WHERE idmovieinfo = %s"
        values = (moviename, formatted_date, id)
        
        try:
            cursor.execute(sql, values)
            connection.commit()  
        except Exception as er:
            print(f"Error: {er}")
        finally:
            cursor.close()   



    @staticmethod
    def update_director(directorname, id):
        connection = MoviesUptade.db
        cursor = connection.cursor()
        get_director=GetInfo.get_directors(id)
        sql_for_select="SELECT director FROM moviedirector WHERE movie=%s"
        sql_for_old="DELETE FROM directors WHERE iddirectors=%s"
        sql_for_new="INSERT INTO directors (directorname) VALUES (%s)"
        

        for ud in get_director:
            try:
                cursor.execute(sql_for_select,(ud,))
                result=cursor.fetchall()
                if result:    
                    for row in result:
                        cursor.execute(sql_for_old,(row,))
                else:
                    cursor.execute(sql_for_new,(directorname,))
                connection.commit()
            except mysql.connector.Error as er:
                if er.errno == 1062:
                    print(f"The actor already exists: {directorname}")
                else:
                    print("Error: ", er)
            finally:
                cursor.close()
                
            
        
    @staticmethod
    def update_actor(actorname, id):
        connection = MoviesUptade.db
        cursor = connection.cursor()
        get_actor=GetInfo.get_actors(id)
        sql_for_select="SELECT actor FROM movieactor WHERE movie=%s"
        sql_for_old="DELETE FROM actors WHERE actorname=%s"
        sql_for_new="INSERT INTO actors (actorname) VALUES (%s)"
        
        
        for ud in get_actor:
            try:
                cursor.execute(sql_for_select,(ud,))
                result=cursor.fetchall()
                if result:    
                    for row in result:
                        cursor.execute(sql_for_old,(row,))
                else:
                    cursor.execute(sql_for_new,(actorname,))
                connection.commit()
            except mysql.connector.Error as er:
                if er.errno == 1062:
                    print(f"The actor already exists: {actorname}")
                else:
                    print("Error: ", er)
            finally:
                cursor.close()
        
    

    @staticmethod
    def update_movie_types(type, id):
        connection = MoviesUptade.db
        cursor = connection.cursor()
        get_type=GetInfo.get_type(id)
        sql_for_select="SELECT movietype FROM movietypeinfo WHERE movie=%s"
        sql_for_old="DELETE FROM movietypes WHERE type=%s"
        sql_for_new="INSERT INTO movietypes (type) VALUES (%s)"
        
        
        for ud in get_type:
            try:
                cursor.execute(sql_for_select,(ud,))
                result=cursor.fetchall()
                if result:    
                    for row in result:
                        cursor.execute(sql_for_old,(row,))
                else:
                    cursor.execute(sql_for_new,(type,))
                connection.commit()
            except mysql.connector.Error as er:
                if er.errno == 1062:
                    print(f"The actor already exists: {type}")
                else:
                    print("Error: ", er)
            finally:
                cursor.close()

class MovieInfoDelete:

    db=moviedb

    @staticmethod
    def delete_info(id):
        connection = MovieInfoDelete.db
        cursor = connection.cursor()
        sql = "DELETE FROM movieinfo WHERE idmovieinfo = %s"
        values = (id,)
       
        try:
            cursor.execute(sql,values)
        
            connection.commit()
        except mysql.connector.Error as er:
            print(f"Error: {er}")
        finally:
            cursor.close()
            print("The data deletion process has been completed.")
            
class GetInfo:

    db=moviedb

    @staticmethod
    def get_directors(id):
        connection = GetInfo.db
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM moviedirector WHERE movie=%s",(id,))
        directors = cursor.fetchall()
        id_list=[]
        for idx in directors:
            print(f"ID: {idx[0]}, director ID: {idx[1]}")
            if idx[0] == id:
                id_list.append(idx[1])  
        cursor.close()
        
        return id_list 
    
    @staticmethod
    def get_actors(id):
        connection = GetInfo.db
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM movieactor WHERE movie=%s",(id,))
        actors = cursor.fetchall()  
        id_list=[]
        for idx in actors:
            print(f"ID: {idx[0]}, Actor ID: {idx[1]}")
            if idx[0] == id:
                id_list.append(idx[1]) 
        cursor.close()
        
        return id_list
    
    @staticmethod
    def get_type(id):
        connection = GetInfo.db
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM movietypeinfo WHERE movie=%s",(id,))
        type = cursor.fetchall()  
        id_list=[]
        for idx in type:
            print(f"ID: {idx[0]}, type ID: {idx[1]}")
            if idx[0] == id:
                id_list.append(idx[1]) 
        cursor.close()
        
        return id_list 
    

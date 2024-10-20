from client import db_client

def read_alumne():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT alumne.NomAlumne, alumne.Cicle, alumne.Curs, alumne.Grup, aula.DescAula from alumne JOIN aula ON alumne.IdAula = aula.IdAula") #Seleccionar tots els alumes
    
        students = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return students

def read_idAlumne(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "select * from alumne WHERE idAlumne = %s"
        value = (id,)
        cur.execute(query, value)
        
        student = cur.fetchone() #fetchONE perquè nomès retornarà un resultat.

    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return student

def create_student(IdAula,NomAlumne,Cicle,Curs,Grup,CreatedAt):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "insert into alumne (IdAula,NomAlumne,Cicle,Curs,Grup,CreatedAt) VALUES (%s,%s,%s,%s,%s,%s);"
        values=(IdAula,NomAlumne,Cicle,Curs,Grup, CreatedAt)
        cur.execute(query,values)
    
        conn.commit()
        student_id = cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return student_id

def update_alumne(idAlumne, Grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "update ALUMNE SET grup = %s WHERE idAlumne = %s;"
        values=(Grup,idAlumne)
        cur.execute(query,values)
        updated_recs = cur.rowcount
    
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return updated_recs

def delete_alumne(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "DELETE FROM alumne WHERE IdAlumne = %s;"
        cur.execute(query,(id,))
        deleted_recs = cur.rowcount
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
        
    return deleted_recs

def read_all_alumnes():
    try:
        conn = db_client()
        cur = conn.cursor()
        query = """
        SELECT 
            a.IdAlumne, 
            a.IdAula, 
            a.NomAlumne, 
            a.Cicle, 
            a.Curs, 
            a.Grup, 
            au.DescAula,
            au.Edifici,
            au.Pis
        FROM 
            alumne AS a
        JOIN 
            aula AS au ON a.IdAula = au.IdAula;
        """
        cur.execute(query)
        results = cur.fetchall()
        return results
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Cursor

def sql_connection(db):
    try:
        con = sqlite3.connect(db)
        return con;
    except Error:
        print(Error)
        
def sql_consultar_datos_existentes(bd, nombreDeUsuario, email):
    strsql = "select nombreDeUsuario, email from personas where nombreDeUsuario='{0}' OR email='{1};".format(nombreDeUsuario, email)
    con = sql_connection(bd)
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    registros_existentes = cursorObj.fetchall()
    return registros_existentes

def crear_nueva_persona(bd, nombre, apellido, nombreDeUsuario, email, contrasena):
    #crear prepared statement
    strsql = "insert into persona (nombre, apellido, permisoAdmin, permisoSuperadmin, usuarioActivo, nombreDeUsuario, URL_fotoDePerfil, email, contrasena) values('{0}', '{1}', {2}, {3}, {4}, '{5}', '{6}', '{7}', '{8}')".format(nombre, apellido, 'FALSE', 'FALSE', 'TRUE', nombreDeUsuario, 'url', email, contrasena)
    #conexion
    con = sql_connection(bd)
    #variable para ejecutar queries
    cursor_obj = con.cursor()
    #ejecutar query
    cursor_obj.execute(strsql)
    #actualizar base de datos
    con.commit()
    con.close()
       
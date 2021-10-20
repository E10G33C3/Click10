import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Cursor

def sql_connection(db):
    try:
        con = sqlite3.connect(db)
        return con;
    except Error:
        print(Error)
        
def sql_consultar_datos_existentes(bd, nombreDeUsuario):
    strsql = "select contrasena from persona where nombreDeUsuario='{0}';".format(nombreDeUsuario)
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
    
def sql_consultar_datos_usuario(bd, nombreDeUsuario):
    strsql = "select * from persona where nombreDeUsuario='{0}';".format(nombreDeUsuario)
    con = sql_connection(bd)
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    registros_existentes = cursorObj.fetchall()
    return registros_existentes
       
def editar_datos(bd, nombre, apellido, email, nombre_de_usuario):
    strsql = "update persona set nombre='{0}', apellido='{1}', email='{2}' where nombreDeUsuario='{3}';".format(nombre,apellido,email,nombre_de_usuario)
    con = sql_connection(bd)
    cursor_obj = con.cursor()
    cursor_obj.execute(strsql)
    con.commit()
    con.close()
    

def eliminar_datos(bd, nombreDeUsuario, email):
    strsql = "update persona set usuarioActivo=0 where nombreDeUsuario='{0}';".format(nombreDeUsuario, email)
    con = sql_connection(bd)
    cursor_obj = con.cursor()
    cursor_obj.execute(strsql)
    con.commit()
    con.close()

# def eliminar_datos(bd, nombreDeUsuario, email):
#     strsql = "delete from persona where nombreDeUsuario = '{0}';".format(nombreDeUsuario, email)
#     con = sql_connection(bd)
#     cursor_obj = con.cursor()
#     cursor_obj.execute(strsql)
#     con.commit()
#     con.close()

def cambiar_contrasena(bd, contrasenaActual, contrasenaNueva, confirmarContrasena, nombreDeUsuario):
    strsql = "update persona set contrasena='{0}' where nombreDeUsuario='{1}';".format(contrasenaActual,contrasenaNueva,confirmarContrasena, nombreDeUsuario)
    con = sql_connection(bd)
    cursor_obj = con.cursor()
    cursor_obj.execute(strsql)
    con.commit()
    con.close()

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
    

def eliminar_datos(bd, nombreDeUsuario):
    strsql = "update persona set usuarioActivo=0 where nombreDeUsuario='{0}';".format(nombreDeUsuario)
    con = sql_connection(bd)
    cursor_obj = con.cursor()
    cursor_obj.execute(strsql)
    con.commit()
    con.close()

def cambiar_contrasena(bd, contrasena, nombreDeUsuario):
    strsql = "update persona set contrasena='{0}' where nombreDeUsuario='{1}';".format(contrasena, nombreDeUsuario)
    con = sql_connection(bd)
    cursor_obj = con.cursor()
    cursor_obj.execute(strsql)
    con.commit()
    con.close()
    
def crear_nueva_publicacion(bd, usuario, timestamp, ULR_imagen, descripcion):
    #crear prepared statement
    strsql = "insert into publicaciones (ID_usuario, timeStampImagenes, URL_imagen, descripcion ) values({0}, {1}, '{2}', '{3}')".format(usuario, timestamp, ULR_imagen,descripcion)
    #conexion
    con = sql_connection(bd)
    #variable para ejecutar queries
    cursor_obj = con.cursor()
    #ejecutar query
    cursor_obj.execute(strsql)
    #actualizar base de datos
    con.commit()
    con.close()

def obtener_id_usuario(bd, usuario):
    strsql = "select ID_usuario from persona where nombreDeUsuario='{0}';".format(usuario)
    con = sql_connection(bd)
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    registros_existentes = cursorObj.fetchall()
    return registros_existentes[0][0]
    
# funcion para cargar las imagenes encontradas en la BDD
def consulta_de_imagenes_general(bd):
    strsql = "select publicaciones.URL_imagen, publicaciones.descripcion, persona.nombreDeUsuario from publicaciones INNER JOIN persona ON publicaciones.ID_usuario=persona.ID_usuario;"
    con = sql_connection(bd)
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    registros_existentes = cursorObj.fetchall()
    return registros_existentes
    
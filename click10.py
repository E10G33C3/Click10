from os import error
import os
import re
from sqlite3.dbapi2 import IntegrityError
from flask import Flask,redirect,url_for, render_template, request , flash , session, send_file
from clases import Persona
import sqlite3
from sqlite3 import Error
from metodos import editar_datos, eliminar_datos, sql_consultar_datos_existentes, crear_nueva_persona, sql_consultar_datos_usuario, consulta_de_imagenes_general
from werkzeug.security import generate_password_hash, check_password_hash
from s3_functions import upload_file, show_image
from werkzeug.utils import secure_filename


app=Flask(__name__)

app.secret_key = "click10"

app.before_request
def session_management():
    session.permanent = True
    
UPLOAD_FOLDER = "uploads"
BUCKET = "click10"

@app.route("/")
@app.route('/Templates/pantallaInicio',methods=['GET','POST'])
def inicio():
    if request.method=='POST':
        # Handle POST Request here
        p = Persona('nombre', 'apellido', request.form['nombreDeUsuario'], 'email', request.form['contrasena'], False, False, False, "url")

        # 
        usuario_encontrado = sql_consultar_datos_existentes('click10.db', p.nombre_de_usuario)
        # print(check_password_hash(usuario_encontrado[0][0], p.contrasena))
        
        if usuario_encontrado:
            if check_password_hash(usuario_encontrado[0][0], p.contrasena):
                # return redirect('/Perfil/{}/'.format(p.nombre_de_usuario))
                #session.clear()
                session["user"] = p.nombre_de_usuario
                session["auth"] = 1
                user = session["user"]
                #return pantallaPerfilUsuario()
                return redirect("pantallaPerfilUsuario.html/"+user)
            else:
                error = 'Contraseña incorrecta'
                return render_template("pantallaInicio.html")
        else:
            return render_template("pantallaInicio.html")
        # except:
            # return render_template('pantallaRegistro.html')
    return render_template('pantallaInicio.html')

@app.route('/Templates/pantallaContrasena.html',methods=['GET','POST'])
def contrasena():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template('pantallaContrasena.html')

@app.route('/Templates/pantallaRegistro.html',methods=['GET','POST'])
def registro():
    if request.method=='POST':
        # Handle POST Request here
        p = Persona(request.form['nombre'], request.form['apellido'], request.form['nombreDeUsuario'], request.form['email'], request.form['contrasena'], False, False,False, "URL")
        p.contrasena = generate_password_hash(p.contrasena)
        try:
            crear_nueva_persona('click10.db', p.nombre, p.apellido, p.nombre_de_usuario, p.email, p.contrasena)
            session["user"] = p.nombre_de_usuario
            session["auth"] = 1
            user = session["user"]
            return redirect("pantallaPerfilUsuario.html/"+user)
        except IntegrityError:

            return render_template("pantallaRegistro.html")
    return render_template("pantallaRegistro.html")

@app.route('/Templates/pantalla1GestionPerfil.html',methods=['GET','POST'])
def editar():
    # sesión
    try:
        user = session["user"]
        auth = session["auth"]
    except:
        user = "unknown"
        auth = 0
    if user == "unknown":
        return redirect(url_for('inicio'))
    
    consulta = sql_consultar_datos_usuario('click10.db', user)
    print(consulta)
    p = Persona(consulta[0][1], consulta[0][2], consulta[0][6], consulta[0][8], consulta[0][9], consulta[0][3], consulta[0][4], consulta[0][5], consulta[0][7])
    
    if request.method=='POST':
        # Handle POST Request here
        p = Persona(request.form['nombre'], request.form['apellido'], request.form['nombreDeUsuario'], request.form['email'], 'contrasena', False, False,False, "URL")
        try:
            editar_datos('click10.db', p.nombre, p.apellido, p.email, p.nombre_de_usuario)
            return render_template("pantallaPerfilUsuario.html")
        except IntegrityError:
            return render_template("pantalla1GestionPerfil.html")
        
    return render_template("pantalla1GestionPerfil.html", user=user, nombre=p.nombre, apellido=p.apellido, email=p.email )

@app.route('/Templates/pantalla2GestionPerfil.html',methods=['GET','POST'])
def cambiarContrasena():
    # sesión
    try:
        user = session["user"]
        auth = session["auth"]
    except:
        user = "unknown"
        auth = 0
    if user == "unknown":
        return redirect(url_for('inicio'))
    
    if request.method=='POST':
        # Handle POST Request here
        p = Persona('nombre', 'apellido', request.form['nombreDeUsuario'], 'email', request.form['contrasena'], False, False,False, "URL")
        p.contrasena = generate_password_hash(p.contrasena)
        
        try:
            editar_datos('click10.db', p.contrasena, p.nombre_de_usuario)
            return render_template("pantallaPerfilUsuario.html")
        except IntegrityError:

            return render_template("pantalla2GestionPerfil.html")
    return render_template("pantalla2GestionPerfil.html", user=user)

@app.route('/Templates/pantalla3GestionPerfil.html',methods=['GET','POST'])
def eliminar():
    
    # sesión
    try:
        user = session["user"]
        auth = session["auth"]
    except:
        user = "unknown"
        auth = 0
    if user == "unknown":
        return redirect(url_for('inicio'))
    
    
    if request.method=='POST':
        # Handle POST Request here
        p = Persona('nombre', 'apellido', request.form['nombreDeUsuario'], request.form['email'], 'contrasena', False, False,False, "URL")
       
        try:
            eliminar_datos('click10.db', p.nombre_de_usuario, p.email)
            return render_template("pantallaPerfilUsuario.html")
        except IntegrityError:

            return render_template("pantalla3GestionPerfil.html")
    return render_template("pantalla3GestionPerfil.html", user=user)


# -------RUTAS DASHBOARD ADMIN---------------
@app.route('/Templates/dashboardAdmin.html',methods=['GET','POST'])
def dashboardAdmin():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("dashboardAdmin.html")


@app.route('/Templates/dashAdmin__Config.html',methods=['GET','POST'])
def dashAdmin__Config():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("dashAdmin__Config.html")


@app.route('/Templates/dashAdmin__listaPubli.html',methods=['GET','POST'])
def dashAdmin__listaPubli():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("dashAdmin__listaPubli.html")


@app.route('/Templates/dashAdmin__listaUsuario.html',methods=['GET','POST'])
def dashAdmin__listaUsuario():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("dashAdmin__listaUsuario.html")



# -------RUTAS DASHBOARD SUPER ADMIN---------------
@app.route('/Templates/dashboardSuperadmin.html',methods=['GET','POST'])
def dashboardSuperAdmin():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("dashboardSuperadmin.html")

@app.route('/Templates/dashSuperAdmin__listaAdmin.html',methods=['GET','POST'])
def dashSuperAdmin__listaAdmin():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("dashSuperAdmin__listaAdmin.html")

@app.route('/Templates/dashSuperAdmin__listaPubli.html',methods=['GET','POST'])
def dashSuperAdmin__listaPubli():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("dashSuperAdmin__listaPubli.html")

@app.route('/Templates/dashSuperAdmin__listaUsuario.html',methods=['GET','POST'])
def dashSuperAdmin__listaUsuario():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("dashSuperAdmin__listaUsuario.html")
# -------RUTAS DASHBOARD SUPER ADMIN---------------

@app.route('/Templates/pantallaGestionPublicaciones.html',methods=['GET','POST'])
def pantallaGestionPublicaciones():
    try:
        user = session["user"]
        auth = session["auth"]
    except:
        user = "unknown"
        auth = 0
    # Hacer algo si auth == 0
    if user == "unknown":
        return redirect(url_for('inicio'))
    
    # crear variable lista de elementos
    
    lista = consulta_de_imagenes_general('click10.db')
    print("La lista es --> ")
    print(lista)
    # disponer lista para LIFO
    lista.reverse()
    
    
    # crear variable de depliegue de imagenes
    elements = show_image(BUCKET, lista)
    # disponer elements para LIFO
    
    
    # lista.reverse()
    
    # manejar consultas POST
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("pantallaGestionPublicaciones.html", elements=elements, user=user, lista=lista)

@app.route('/Templates/pantallaMensajes.html',methods=['GET','POST'])
def pantallaMensajes():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("pantallaMensajes.html")

@app.route('/Templates/pantallaPerfilUsuario.html',methods=['GET','POST'])
@app.route('/Templates/pantallaPerfilUsuario.html/<user>',methods=['GET','POST'])
def pantallaPerfilUsuario(user = None):
    # if request.method=='POST':
    #     # Handle POST Request here
    #     pass
    # return render_template("pantallaPerfilUsuario.html")
    try:
        user = session["user"]
        auth = session["auth"]
    except:
        user = "unknown"
        auth = 0
    # Hacer algo si auth == 0
    if user == "unknown":
        return redirect(url_for('inicio'))
    # Por ejemplo cargar el template de login
    #return "<p>¡Hola %s!</p>" % user
    return render_template("pantallaPerfilUsuario.html", user = user)

@app.route('/Templates/pantallaVistaPublicacion.html',methods=['GET','POST'])
def pantallaVistaPublicacion():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("pantallaVistaPublicacion.html")

@app.route("/logout")
def logout():
  session.clear()
  session["user"] = "unknown"
  session["auth"] = 0
  return redirect(url_for('inicio'))

@app.route("/Templates/cargaDeImagenes.html", methods=['POST'])
def cargaDeImagenes():
        # sesión
    try:
        user = session["user"]
        auth = session["auth"]
    except:
        user = "unknown"
        auth = 0
    if user == "unknown":
        return redirect(url_for('inicio'))
    
    if request.method=='POST':
        # Handle POST Request here
        return render_template("cargaDeImagenes.html")
    return render_template("cargaDeImagenes.html")

@app.route("/upload", methods=['POST'])
def upload():
        # sesión
    try:
        user = session["user"]
        auth = session["auth"]
    except:
        user = "unknown"
        auth = 0
    if user == "unknown":
        return redirect(url_for('inicio'))
    
    if request.method == "POST":
        f = request.files['file']
        descripcion = request.form['descripcion']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        upload_file(f"{f.filename}", BUCKET, user, descripcion)
        # os.remove(f.filename)
        return redirect("/Templates/pantallaGestionPublicaciones.html")
    
@app.route("/pics")
def list():
    dummy = ["",""]
    contents = show_image(BUCKET, dummy)
    return render_template('collection.html', contents=contents)


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
    

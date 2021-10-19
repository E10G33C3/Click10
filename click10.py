from os import error
from sqlite3.dbapi2 import IntegrityError
from flask import Flask,redirect,url_for, render_template, request , flash  
from clases import Persona
import sqlite3
from sqlite3 import Error
from metodos import sql_consultar_datos_existentes, crear_nueva_persona, sql_consultar_datos_usuario
from werkzeug.security import generate_password_hash, check_password_hash


app=Flask(__name__)

@app.route("/")
@app.route('/Templates/pantallaInicio',methods=['GET','POST'])
def inicio():
    if request.method=='POST':
        # Handle POST Request here
        p = Persona('nombre', 'apellido', request.form['nombreDeUsuario'], 'email', request.form['contrasena'], False, False, False, "url")

        # 
        usuario_encontrado = sql_consultar_datos_existentes('click10.db', p.nombre_de_usuario)
        # print(check_password_hash(usuario_encontrado[0][0], p.contrasena))
        
        if check_password_hash(usuario_encontrado[0][0], p.contrasena):
            return redirect('/Perfil/{}/'.format(p.nombre_de_usuario))
        else:
            error = 'Contraseña incorrecta'
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
            return render_template("pantallaPerfilUsuario.html")
        except IntegrityError:

            return render_template("pantallaRegistro.html")
    return render_template("pantallaRegistro.html")

@app.route('/Perfil/<string:nombreDeUsuario>/',methods=['GET','POST'])
def gestionPerfil1(nombreDeUsuario):
    datos = sql_consultar_datos_usuario('click10.db', nombreDeUsuario)
    print(datos)
    if request.method=='POST':
        # Handle POST Request here
        return "perfil POST de {}".format(nombreDeUsuario)
    return "perfil GET de  {}".format(nombreDeUsuario)

@app.route('/Templates/pantalla2GestionPerfil.html',methods=['GET','POST'])
def gestionPerfil2():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("pantalla2GestionPerfil.html")

@app.route('/Templates/pantalla3GestionPerfil.html',methods=['GET','POST'])
def gestionPerfil3():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("pantalla3GestionPerfil.html")

@app.route('/Templates/dashboardAdmin.html',methods=['GET','POST'])
def dashboardAdmin():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("dashboardAdmin.html")

@app.route('/Templates/dashboardSuperadmin.html',methods=['GET','POST'])
def dashboardSuperadmin():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("dashboardSuperadmin.html")

@app.route('/Templates/pantallaGestionPublicaciones.html',methods=['GET','POST'])
def pantallaGestionPublicaciones():
    times = 10
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("pantallaGestionPublicaciones.html", times=times)

@app.route('/Templates/pantallaMensajes.html',methods=['GET','POST'])
def pantallaMensajes():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("pantallaMensajes.html")

@app.route('/Templates/pantallaPerfilUsuario.html',methods=['GET','POST'])
def pantallaPerfilUsuario():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("pantallaPerfilUsuario.html")

@app.route('/Templates/pantallaVistaPublicacion.html',methods=['GET','POST'])
def pantallaVistaPublicacion():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("pantallaVistaPublicacion.html")

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
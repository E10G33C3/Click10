from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route("/")
@app.route('/Templates/pantallaInicio.html',methods=['GET','POST'])
def inicio():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('pantallaInicio.html')
    return render_template('pantallaInicio.html')

@app.route('/Templates/pantallaContrasena.html')
def contrasena():
    return render_template('pantallaContrasena.html')

@app.route('/Templates/pantallaRegistro.html')
def registro():
    return render_template("pantallaRegistro.html")

@app.route('/Templates/pantalla1GestionPerfil.html')
def gestionPerfil1():
    return render_template("pantalla1GestionPerfil.html")

@app.route('/Templates/pantalla2GestionPerfil.html')
def gestionPerfil2():
    return render_template("pantalla2GestionPerfil.html")

@app.route('/Templates/pantalla3GestionPerfil.html')
def gestionPerfil3():
    return render_template("pantalla3GestionPerfil.html")

@app.route('/Templates/dashboardAdmin.html')
def dashboardAdmin():
    return render_template("dashboardAdmin.html")

@app.route('/Templates/pantallaGestionPublicaciones.html')
def pantallaGestionPublicaciones():
    return render_template("pantallaGestionPublicaciones.html")

@app.route('/Templates/pantallaMensajes.html')
def pantallaMensajes():
    return render_template("pantallaMensajes.html")

@app.route('/Templates/pantallaPerfilUsuario.html')
def pantallaPerfilUsuario():
    return render_template("pantallaPerfilUsuario.html")

@app.route('/Templates/pantallaVistaPublicacion.html')
def pantallaVistaPublicacion():
    return render_template("pantallaVistaPublicacion.html")

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
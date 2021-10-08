from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route("/")
@app.route('/Templates/pantallaInicio.html',methods=['GET','POST'])
def inicio():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('pantallaInicio.html')
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
        pass
    return render_template("pantallaRegistro.html")

@app.route('/Templates/pantalla1GestionPerfil.html',methods=['GET','POST'])
def gestionPerfil1():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("pantalla1GestionPerfil.html")

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

@app.route('/Templates/pantallaGestionPublicaciones.html',methods=['GET','POST'])
def pantallaGestionPublicaciones():
    if request.method=='POST':
        # Handle POST Request here
        pass
    return render_template("pantallaGestionPublicaciones.html")

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
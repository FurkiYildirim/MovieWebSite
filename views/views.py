""" Flask Projesi """

from flask import Flask, render_template, request

# App pbjesi flask için tanımlıyoruz
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    """ Ana sayfa """
    return "Burası ana sayfa"

@app.route("/")
def ulogin():
    if request.method == 'POST':
        uname = request.form.get('usern')
        psw = request.form.get('pswd')

        """
        if loginControl(uname, psw):
            return render_template("anasayfa.html")
        else:
            return redirect(url_for("ulogin"))    
        """

    if request.method == 'GET':

        return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True, host="127.0.1.1", port=4444)
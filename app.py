from flask import Flask, render_template
#main flask code 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("Recommended.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login-process', methods=["POST"])
def login_process():
    if requests.methods == "POST":
        email=request.form("email")
        password=request.form("password")
        row = services.login(email,password)
        if not row:
            return redirect(url_for("login"))
    return redirect(url_for("index"))
@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/register-process', methods=["POST"])
def register_process():
    if requests.methods == "POST":
        user_name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        row = services.register(name, email, password)
        if not row:
            return redirect(url_for("register"))
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)


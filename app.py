from flask import flask 
#main flask code 
app = Flask(_name_)
@app.route('/')
def index():
    return render_templates("index.html")

@app.route('/login')
def login():
    return render_templates("login.html")

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
    return render_templates("register.html")

@app.route('/register-process', method=["POST"])
 def register_process():
    if requests.methods == "POST":
        user_name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        row = services.register(name, email, password)
        if not row:
            return redirect(url_for("register"))
        return redirect(url_for("login"))

if _name_ == "__main__":
    app.run()


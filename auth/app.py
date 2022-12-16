import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

# config
app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
app.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")


@app.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401

    #check db for username and password
    cur = mysql.connection.cursor()
    res = cur.execute(
        "SELECT email, password FROM user WHERE email=%s", (auth.username)
    )
    if res != 0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]

        if auth.username != email or auth.password != password:
            return "invalid credentials", 401
        else:
            return createJWT(auth.username, envs["JWT_SECRET"], True)
    else:
        return "invalid credentials", 401


@app.route("/validate", methods=["POST"])
def validate():
    encoded_jwt = request.headers["Authorization"]

    if not encoded_jwt:
        return "missing credentials", 401

    # format of encoded_jwt => Bearer token 
    token = encoded_jwt.split(" ")[1]

    try:
        decoded = jwt.decode(
            token, os.environ.get("JWT_SECRET"), algorithm="HS256"
        )
    except:
        return "not authorized", 403
    return decoded, 200


def createJWT(username, secret, is_admin):
    return jwt.encode(
        {
            "username": username, 
            "exp": datetime.datetime. now(tz=datetime.timezone.utc) + datetime.timedelta(days=1), #expiry in 24 hrs
            "iat": datetime.datetime.now(),
            "admin": is_admin
        },
        secret, 
        algorithm="HS256"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

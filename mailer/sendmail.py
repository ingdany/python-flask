from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config["DEBUG"] = True
app.config["TESTING"] = False
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = "daniel.perez@sonatasmx.com"
app.config["MAIL_PASSWORD"] = "M1P@$$w0rd"
app.config["MAIL_DEFAULT_SENDER"] = "daniel.perez@sonatasmx.com"
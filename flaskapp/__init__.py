from flask import Flask

app = Flask(__name__)
app.run(debug=True)

from flaskapp import routes

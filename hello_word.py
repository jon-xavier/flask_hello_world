from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

@app.route("/jedi/<first_name>/<last_name>")
def jedi_name(first_name, last_name):
    jedi_name = last_name[0:2] + first_name[0:2]
    html = """
    <p>
        Your Jedi Name is:
    </p>
    <h1>
        {}
    </h1>
    """
    return html.format(jedi_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheeeee!",
                           my_list=[0,1,2,3,4,5])

@app.route("/hello/<name>")
def hello_person(name):
    return render_template('hello_person.html', name = name)

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
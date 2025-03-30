from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "John Elder's Blog"
    return render_template("index.html", title = title)

@app.route('/about')
def about():
    title = "About John Elder"
    names = ["John", "Mary", "Wes", "Sally"]
    return render_template("about.html", names = names, title = title)

# create custom error


#invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
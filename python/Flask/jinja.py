from flask import Flask,render_template,request

app = Flask(__name__)  ## Instance of flask app for WSGI


@app.route("/")
def welcome():
    return "<html><h1>Welcome to my Home Page</h1></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name}"
    return render_template("form.html")

## Variable rule
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res ="FAILED"
    return render_template("result.html",results=res)

@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res ="FAILED"
    
    exp = {"score":score,"res":res}

    return render_template("result1.html",results=exp)


@app.route("/successif/<int:score>")
def successif(score):

    return render_template("result2.html",results=score)

if __name__=="__main__":
    app.run(debug=True)
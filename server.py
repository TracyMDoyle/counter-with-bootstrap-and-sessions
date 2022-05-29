from filecmp import clear_cache
import numbers
from typing import Counter
from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)
app.secret_key = "The first rule of the secret key, don't tell the secret key."

@app.route('/')
# def index():
#     return render_template("index.html")
#testing function to ensure server is up amd running before proceeding

def session_count():
    print("counting")
    if "counter" not in session:
        session ["counter"] = 0
    else: 
        session["counter"] += 1
    return render_template("index.html")

@app.route("/destroy")
def destroy_session():
    session.clear()
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True, port=5001) #when testing debug set true, when moved set to False, 5001 used because I am on a mac
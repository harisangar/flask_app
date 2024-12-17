from flask import Flask,render_template
from db import getTaskList
app=Flask(__name__)

# tasklist=[['walk dog',True],['shopping',True],['study python',False]]
tasklist=getTaskList()

@app.route('/')
def home():
    return render_template('tasklist.html',TaskList=tasklist)


app.run()
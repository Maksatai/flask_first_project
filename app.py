from flask import Flask,render_template
from openpyxl import load_workbook

excel=load_workbook('report.xlsx')
page=excel["Sheet"]

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html',goods=page.values)

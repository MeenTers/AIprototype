#import pandas
from inspect import getargvalues
from operator import index
from flask import Flask, request, render_template
import json
app = Flask(__name__)

@app.route("/") 
def home():
    return "Hello, World!"

@app.route("/name") 
def hellemeenters():
    return "Hello, MeenTers!"

##api
@app.route('/request',methods=['POST'])
def request_detail():

    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload)

    print(inmessage) 

    json_data = json.dumps({'y', 'received!'})
    return json_data

##webapp
@app.route("/home",methods=['POST','GET'])
def homes():

    if request.method == "POST":
        pddb = read_csv("testdb.csv")
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        pddb = pddb.append({'name':first_name,'lastname':last_name},ignore_index=True)
        pddb.to_csv(db.csv,index=False)
        return render_template("home.html",name= f"{first_name} {last_name}")
    if request.method == "GET":
        getval = request.args
        print(getval)
        print(getval.get('name'))

    return render_template("home.html",name = "MeenTers")    

    

        
@app.route("/home1",methods=['POST','GET'])
def home1():
    if request.method == "POST":
       agent = request.form.get("fav_agent")
       return render_template("home.html",name= "MeenTers" , item= (agent))
        
    

if __name__ == "__main__":
    app.run() #host='0.0.0.0',port=5001
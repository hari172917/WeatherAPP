from flask import Flask,request,render_template
import requests
app=Flask(__name__)
@app.route("/")
def render_index():
    return render_template("index.html")


@app.route("/weatherdata",methods=["POST","GET"])
def weather():
    url="https://api.openweathermap.org/data/2.5/weather?"
    
    param={
        'q':request.form.get("Place"),
        'unit':request.form.get("Units"),
        'appid':request.form.get("Appid")
    }
    response=requests.get(url,params=param)
    data =response.json()
    return f"data :{data}"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)


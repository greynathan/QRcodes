from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/')
def QRcode():
    filename = "placeholder.jpg"
    return render_template('index.html', filename = filename)

@app.route('/generate')
def generate():
    website = request.args.get('url', '')
    filename= website+".png"
    if (website ==''):
        return QRcode()
    else:
        img = qrcode.make(website)
        img.save("static/"+filename)
        return render_template('index.html', filename= filename)
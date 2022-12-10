from flask import Flask, render_template, request 
from app_main import main,generate_code,generate_QR
#print("dj")
app = Flask(__name__)  

@app.route('/')  
def upload():  
    return render_template("index.html")  
 
@app.route('/send_signal', methods = ['POST'])  
def get_signal():  
    if request.method == 'POST': 
        weldsem_signal = request.form.get('WS') 
        printer_signal = request.form.get('PS') 
        
    main(weldsem_signal,printer_signal)    
       

    #return render_template("index.html", QR_Image = 'img_path')  
    return render_template("index.html")

if __name__ == '__main__':  
    app.run(debug = True) 
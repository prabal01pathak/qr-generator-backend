from flask import Flask, render_template, request, jsonify
from app_main import Manager, generate_QR

# print("dj")
app = Flask(__name__)

WELDSEM_SIGNAL = False
PRINTER_SIGNAL = False


manager = Manager()


@app.route("/")
def upload():
    return render_template("index.html")


@app.route("/send_signal", methods=["POST"])
def get_signal():
    if request.method == "POST":
        weldsem_signal = True if request.form.get("WS") == "on" else False
        printer_signal = True if request.form.get("PS") == "on" else False
        print(weldsem_signal, printer_signal)
    manager.main(weldsem_signal, printer_signal)
    # return render_template("index.html", QR_Image = 'img_path')
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

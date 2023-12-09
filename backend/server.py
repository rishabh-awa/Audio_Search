from flask import Flask,request, send_from_directory
from scri import transcribe, questioA

app = Flask(__name__)

@app.route("/mess", methods=["POST"])
def printa():
    url = request.form["url"]
    prompt = request.form["prompa"]
    text=transcribe(url)
    answer = questioA(text, prompt,url)
    return answer

@app.route("/<path:filename>", methods=["GET"])
def reta(filename):
    return send_from_directory(r"C:\Users\Shiv\Desktop\Transcript\frontend\src",filename)

if __name__ == '__main__':
    app.run(debug=True)

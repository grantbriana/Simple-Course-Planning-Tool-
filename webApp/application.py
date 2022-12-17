import os
import json
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "uploads"

dictionary = {
   "fileName": "",
   "track": ""
}

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/browserSchedule')
def browserSchedule():
   return render_template('browserSchedule.html')


def runApp():
   import fileReader as fr
   import scheduleGenerator as gen
   import DAG as dag


@app.route('/success', methods = ['POST'])
def uploadFile():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

      #Load to JSON
      dictionary["fileName"] = filename
      dictionary["track"] = request.form.get("track")
      with open("upload.json", "w") as outfile:
         json.dump(dictionary, outfile)

   runApp()
   from main import displaySchedule
   schedule = displaySchedule()


   return render_template('browserSchedule.html', variable = schedule)


if __name__ == '__main__':
   app.run(debug = True)





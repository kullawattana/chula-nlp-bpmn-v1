import os
from flask import Flask, request, render_template, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from main_generate_bpmn_xml import BPMN
from neural_coref import NeuralCoref

ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'data'
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024  # 4MB max-limit.

flow = []
lane = []
svo = []

# check input file's file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# home page
@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], "result_bpmn_process_from_nlp.bpmn"))
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], "result_bpmn_process_from_nlp.xml"))

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        read_text = []
        for text in request.files.get('file'):
            read_text.append(str(text).replace("b'",""))

        # run the test function
        neuralCoref = NeuralCoref(read_text[0])
        text = neuralCoref.get_sentence()

        process_name = "BPMN Process"
        is_show_lane = True
        is_show_gateway = False
        bpmn = BPMN(text, process_name)
        list_flow, json_list_lane, list_svo_to_generate_bpmn_in_out_diagram = bpmn.bpmn_process(is_show_lane, is_show_gateway)
        flow.append(list_flow)
        lane.append(json_list_lane)
        svo.append(list_svo_to_generate_bpmn_in_out_diagram)

        # if the user does not select a file, browser submits an empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # if the user submits a file with the correct format
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file'))

    return render_template('index.html')

# download page
@app.route('/download', methods=['POST', 'GET'])
def download_file():
    if request.method == 'POST':
        if request.form['Download Result File'] == 'Download BPMN File':
            return send_from_directory(app.config['UPLOAD_FOLDER'], 'result_bpmn_process_from_nlp.bpmn')
    return render_template('download.html', flow=flow[0], lane=lane[0], svo=svo[0])  

# show xml
@app.route('/showxml', methods=['POST', 'GET'])
def show_xml():
    if request.method == 'GET':
        return send_from_directory(app.config['UPLOAD_FOLDER'], 'result_bpmn_process_from_nlp.xml')

if __name__ == '__main__':
    app.run(debug=True)
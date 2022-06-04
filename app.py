from flask import Flask, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired
from main import bpmn_process

import os
SECRET_KEY = os.urandom(32)

csrf = CSRFProtect()
app = Flask(__name__)
app.config['SECRET_KEY'] = '325245hkhf486axcv5719bf9397cbn69xv'
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024  # 4MB max-limit.
csrf.init_app(app)

class DocumentUploadForm(FlaskForm):
    document = FileField('Document', validators=[FileRequired(), FileAllowed(['txt'], 'Text File only!')])

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = DocumentUploadForm()
    if form.validate_on_submit():

        assets_dir = os.path.join(
            os.path.dirname(app.instance_path), 'assets'
        )

        d = form.document.data
        docname = secure_filename(d.filename)

        # Document save
        d.save( os.path.join(assets_dir, docname))
        flash('Document uploaded successfully.')

        # Got data from file
        is_show_lane = True
        bpmn_process("", is_show_lane)

        return redirect(url_for('index'))

    return render_template('index.html', form=form)
    
if __name__ == '__main__':
    app.run(debug=True)
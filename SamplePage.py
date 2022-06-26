from flask import render_template
from flask_classful import FlaskView


class SampleView(FlaskView):
    def index(self):
        # return render_template('about_camel.html')
        return render_template('registerpage.html')
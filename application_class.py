from flask_classful import FlaskView, route
from flask import render_template

from token_autheticator import token_required


class ApplicationView(FlaskView):
    @token_required
    @route('/app_page')
    def app_page(self):
        return render_template('about_camel.html')
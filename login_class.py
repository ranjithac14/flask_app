from functools import wraps
from select import select
from flask import render_template, request, flash,redirect,url_for,session
from flask_classful import FlaskView, route
import regex as re

from token_autheticator import token_required



class LoginView(FlaskView):
    def index(self):
        return render_template('registerpage.html')

    @route('/login_page')
    def login_page(self):
        return render_template('loginpage.html')

    @route('/log_out')
    def log_out(self):
        session.clear()
        return "Logged Out"










import os
import requests
import json
from giphy_api_key import api_key
from flask import Flask, render_template, session, redirect, request, url_for, flash
from flask_script import Manager, Shell
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, PasswordField, BooleanField, SelectMultipleField, ValidationError
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from werkzeug.security import generate_password_hash, check_password_hash



baseurl = "https://api.giphy.com/v1/gifs/search"
search_string = 'cats'
url = baseurl + '?api_key=' + api_key + '&q=' + search_string + '&limit=5'
results = requests.get(url)
json_data = json.loads(results.text)
for item in json_data['data']:
    print(item['url'], item['title'])
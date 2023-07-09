import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET KEY') or 'DogAdopt12345'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://bartek:Bartek12345!@localhost' \
                                                                '/dogadopt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = '/home/bartek/projects/DogAdopt/app/static/Images'

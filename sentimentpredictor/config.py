"""
	Configuration will be set up as an object named "Config" with a list
        of attributes or members as config variables
"""
import os
import pickle
basedir = os.path.abspath(os.path.dirname(__file__))
from webapp.models import Mlmodel
"""
basedir is:
.../DIPLOMADO-UPEL-EducacionUniversitaria/TEMAS-o-AREAS/COMPUTER-SCIENCE/EJEMPLOS/PYTHON/FLASK/sentimentpredictor
"""
#print("Base dir is: {}".format(basedir))
class Config(object):
    """ if no OS env variable is set, SECRET_KEY will assume the hardcoded string as its value """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    """
	The location of the application's database. If the DATABASE_URL envvar is not set,
	then
    """
    """
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 465 )
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') or True
    #MAIL_USE_TLS = int(os.environ.get('MAIL_USE_TLS') or 1)#
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'victor.liendo@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'Jwl10_c3sar'
    ADMINS = ['victor.liendo@gmail.com']
    """
    """ For email management during development phase
		DEBUG MODE MUST BE SET TO 0, and the FAKE email server must be running
		python -m smtpd -n -c DebuggingServer localhost:8025
    """

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 8025)
    ADMINS = ['victor.liendo@gmail.com']
    print("HOLA Base dir is: {}".format(basedir))
    """THE PREVIOUSLY SAVED ML MODEL"""
    MODEL = pickle.load(open(os.path.join(basedir, 'ML-model/LR-with-CountVectorizer-for-SentimentAnalisis.pkl'), 'rb'))
    VECTOR = pickle.load(open(os.path.join(basedir, 'ML-model/CountVectorizer-vector.pkl'), 'rb'))
    APPMODEL=Mlmodel(MODEL,VECTOR)
    print(APPMODEL.get_model_type())
    print(APPMODEL.get_vector_type())

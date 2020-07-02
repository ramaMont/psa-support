# -- FILE: features/environment.py
# flaskr is the sample application we want to test
from app import create_app, setup_database
from behave import given

import os
import tempfile


@given(u'I am an Analista de mesa de ayuda')
def step_impl(context):
    print(u'STEP: Given I am an Analista de mesa de ayuda')
    pass


def before_scenario(context, feature):
    # -- HINT: Recreate a new flaskr client before each feature is executed.
    app = create_app(False)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
    #context.db, app.config['DATABASE'] = tempfile.mkstemp()
    app.testing = True
    context.tc = app.test_client()
    setup_database(app)
    #os.close(context.db)
    #os.unlink(app.config['DATABASE'])
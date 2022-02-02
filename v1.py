from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import or_

from flask import Flask, request, render_template, redirect

#Example 4.2 Flask Webform dev
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from pprint import pprint

import viewform

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

from flask_moment import Moment
moment = Moment(app)

@app.route('/', methods=['GET'])
def sql():

    engine = create_engine("shillelagh://")
    connection = engine.connect()

    table = Table('https://docs.google.com/spreadsheets/d/1RZstNkiNBTEBo8mJBwAYh29bQHOynEDxFb54hvHRsAc/edit#gid=1835168426', MetaData(bind=engine),autoload=True)

    print(table.name)
    print(table.columns.keys())

    try:
        rf = viewform.RowForm()
    except Exception as e:
        print("************GOT EXCEPTION************")
        print(e)
        print("************GOT EXCEPTION************")

    for k in table.columns.keys():
        k = k.replace(" ", "_")
        k = k.replace(".", "_")
        k = k.replace("(", "_")
        k = k.replace(")", "_")
        k = k.replace("/", "_")
        k = k.replace("\\", "_")
        #print(k)
        #rf.newAttr(k)
        setattr(rf, k, StringField("testing"))
    print("---------------------------------")
    pprint(dir(rf))
    #pprint(vars(rf))
    print("---------------------------------")
    return render_template('table.html', data=table.columns.keys())

    select_st = select([table]).where(table.c.Org == "CME")
    res = connection.execute(select_st)

    for _row in res:
        print(_row)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    rows = session.query(table.c.Org).all()
    for r in rows:
        print(r)

    l = [v for v, in rows]

    print(l)

    #Find all columns
    for c in table.columns:
        rows = session.query(c).all()
        #Find values from all columns
        l = [v for v, in rows]
        print(l)

if __name__ == '__main__':
    app.run(debug=True)

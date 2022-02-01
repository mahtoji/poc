#Example 4.2 Flask Webform dev
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FinalMeta(type(FlaskForm), type(Base)):
    pass

class RowForm(FlaskForm):
    def newAttr(self, attr):
        try:
            setattr(self, attr, attr)
        except Exception as e:
            pass

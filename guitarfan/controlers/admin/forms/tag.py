#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms.fields import TextField, HiddenField, SubmitField
from wtforms.widgets import HiddenInput
from wtforms.validators import Required

from guitarfan.utilities import validator
from guitarfan.models import *


class TagFrom(Form):
    id = HiddenField(widget=HiddenInput())
    name = TextField(u'Tag Name', validators=[Required(message=u'Tag name is required'),
                     validator.Unique(Tag, Tag.name, message=u'The current tag is already in use')])
    submit = SubmitField(u'Submit', id='submit')

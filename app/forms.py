from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import re

class MacForm(FlaskForm):
    data = TextAreaField('Ingrese listado de direcciones MAC', validators=[DataRequired()])
    submit = SubmitField('Generar script')

    def validate_data(form, field):
        mac_addresses = re.split(r'[,\s]+', field.data.strip())
        for mac in mac_addresses:
            if mac and not re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac):
                raise ValidationError(f'Invalid MAC address format: {mac}')

class UserForm(FlaskForm):
    users = TextAreaField('Ingrese usuarios y contraseñas', validators=[DataRequired()])
    submit = SubmitField('Generar script')

class IpForm(FlaskForm):
    ips = TextAreaField('Ingrese direcciones IPv4', validators=[DataRequired()])
    submit = SubmitField('Generar script')
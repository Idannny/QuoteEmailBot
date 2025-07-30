from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

class MaterialForm(FlaskForm):
    component_type = SelectField('Component Type', choices=[
        ('blk_rings', 'Blanked Rings'),
        ('bar', 'Bar'),
        ('tube', 'Tube'),
        ('ball', 'Spherical Ball'),
        ('roller', 'Cylindrical Roller'),
        ('cage', 'Cage'),
        ('separator', 'Separator'),
        ('lube', 'Lubricant'),
        ('oil', 'Oil'),
        ('adhesive', 'Adhesive'),
        ('solutions', 'Solutions (Acetone, Coolant, Nitric)'),
        ('grease', 'Grease'),
        ('cleaners', 'Cleaners/Degreasers'),
        ('seal', 'Seals'),
        ('shield', 'Shields')
    ], validators=[DataRequired()])
    uom = SelectField('Unit of Measure', choices=[
        ('ft', 'Feet'),
        ('oz', 'Ounces'),
        ('lb', 'Pounds'),
        ('gal', 'Gallons'),
        ('unit', 'Units'),
        ('cc', 'Cubic Centimeter (cc)'),
        ('qrt', 'Quarts')
    ], validators=[DataRequired()])

    # ball_grade = SelectField('Grade', choices=[('g5','Grade 5'), ('g25','Grade 25')])

    quantity = IntegerField('Quantity', validators=[DataRequired()])
    alloy = StringField('Material Alloy', validators=[DataRequired()])
    vendor = StringField('Vendor', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MaterialForm()
    
    if form.validate_on_submit():
        print("preparing Email: ")
        app.logger.info('Items assembled to Emailed')
        email_content = prepare_email(form.data)
        flash('Email prepared successfully!')
        return render_template('email.html', email_content=email_content)
    return render_template('form.html', form=form)

def prepare_email(form_data):
    ring_template = f"""
    To whom it may concern at the offices of {form_data['vendor']}

    We would like to place an order for the following materials:

    Raw Material Type: {form_data['uom']}
    Quantity: {form_data['quantity']}
    Material Alloy: {form_data['alloy']}

    Please confirm the availability and provide a quote for this order.

    Thank you,
    Procurement Team
    """

 
    ball_template = f"""
    To whom

    We would like to place an order for the following Rolling Elements:

    Material Type: {form_data['uom']}
    Quantity: {form_data['quantity']}
    Material Alloy: {form_data['alloy']}
    Grade: 

    Please confirm the availability and provide a quote for this order.

    Thank you,
    Procurement Team
    """
    
    fluid_template = f"""
    """

    

    return ring_template

if __name__ == '__main__':
    app.run(debug=True)


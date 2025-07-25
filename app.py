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
    shape = SelectField('Geometry', choices=[
        ('cylinder', 'Cylindrical'),
        ('rectangular', 'Rectangular')
        
        ])
    uom = SelectField('Unit of Measure', choices=[
        ('ft', 'Feet'),
        ('oz', 'Ounces'),
        ('lb', 'Pounds'),
        ('gal', 'Gallons'),
        ('unit', 'Units'),
        ('cc', 'Cubic Centimeter (cc)'),
        ('qrt', 'Quarts')
    ], validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    alloy = StringField('Material Alloy', validators=[DataRequired()])
    who_email = StringField('User Email', validators=[DataRequired()])
    who_first_name = StringField('User First Name', validators=[DataRequired()])
    who_last_name = StringField('User Last Name', validators=[DataRequired()])
    vendor = StringField('To Which Vendor?', validators=[DataRequired()])
   
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MaterialForm()
    
    if form.validate_on_submit() :
        print("validated")
        email_content = prepare_email(form.data)

        print("Look out", email_content)
        flash('Email prepared successfully!')
        return render_template('email.html', email_content=email_content)
    
    
    return render_template('form.html', form=form)

def prepare_email(form_data):
    raw_template = f"""
    To whom it may concern at {form_data['vendor']},

    We would like to place an order for the following:

    Raw Material Type: {form_data['component_type']}
    Shape of Item: {form_data['shape']}
    Quantity: {form_data['quantity']} {form_data['uom']}
    Material Alloy: {form_data['alloy']}

    Please confirm the availability and provide a quote for this order.

    Thank you,
    {form_data['who_first_name']} {form_data['who_last_name']}

    """
    
    fluid_template=f"""
    To whom it may concern at {form_data['vendor']},

    We would like to place an order for the following:

    Chemical Type: {form_data['component_type']}
    Quantity: {form_data['quantity']} {form_data['uom']}


    Please confirm the availability and provide a quote for this order.

    Thank you,
    {form_data['who_first_name']} {form_data['who_last_name']}

    """

    # fluid_list =['lube', 'adhesive', 'oil',  'solutions', 'grease', 'cleaners']
    
    # if {form_data['component_type']} == 'lube':
    # # if {form_data['component_type']} in fluid_list:
    #     print("Made it in prewpare_email")
    #     return fluid_template

    return raw_template

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request, url_for
import math
# Referencing this file
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',)

@app.route('/profile')
def profile():
    return render_template('profile.html', page_name = 'Profile')

@app.route('/works')
def works():
    return render_template('works.html', page_name = 'Works')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result, page_name = 'to Uppercase')

@app.route('/contact')
def contact():
    return render_template('contacts.html', page_name = 'Contacts')

def calculate_circle_area(radius):
    if radius < 0:
        return "Radius cannot be negative"
    
    area = math.pi * radius**2
    return round(area , 2)

@app.route('/areaOfcircle' , methods=['GET', 'POST'])
def areaOfcirle():
    radius = 0
    area = 0
    if request.method == 'POST':
        radius = float(request.form['radius'])
        area = calculate_circle_area(radius)
    return render_template('areaOfcircle.html', radius = radius, area = area, page_name = 'Area')

def calculate_triangle_area(base, height):
    if base < 0 or height < 0:
        return "Base and height cannot be negative"
    
    area = (base * height) / 2
    return round(area, 2) 

@app.route('/areaOfTriangle', methods = ['GET', 'POST'])
def areaOfTriangle():
    base = 0     
    height = 0   
    area = 0  
    
    if request.method == 'POST':
        base = float(request.form['base'])
        height = float(request.form['height'])
        area = calculate_triangle_area(base, height)
   
    return render_template('areaOfTriangle.html', base=base, height=height, area=area, page_name = 'Triangle')



if __name__ == "__main__":
    app.run(debug=True)

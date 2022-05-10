
from flask import Flask, render_template
import smbus, time
app = Flask(__name__)
#from bme280 import cTemp

data_route = '/home/debian/Prog_Res/server/data.txt'

global moyenne_temp
global moyenne_hum
global moyenne_pressure

global mt
temp_m=0
humi_m=0
pres_m=0
temp =0
pres = 0
humi = 0
def refresh():
	global temp_m, humi_m, pres_m, temp, pres, humi

	with open(data_route, 'r') as f:
        	lectures = f.readlines()
       		last_line = lectures[-1]
        	print (last_line)
        	data = last_line
        	stringdata = last_line.split()
        	print (stringdata)
        	temp = stringdata[1]
        	pres = stringdata[3]
        	humi = stringdata[5]
        	humi_m = stringdata[8]
        	pres_m = stringdata[7]
        	temp_m = stringdata[6]


@app.route("/")
def hello():
	global temp_m, humi_m, pres_m, temp, pres, humi
	refresh()
	return render_template('page.html', temp=temp, pres=pres, humi=humi, temp_m=temp_m, pres_m=pres_m, humi_m=humi_m) 

@app.route("/moyenne_temperature")
def temp_html():
	global temp_m
	refresh()
	return render_template('sub_temp.html', temp_m=temp_m)

@app.route("/moyenne_pressure")
def pression_html():
	global pres_m
	refresh()
	return render_template('sub_pressure.html', pres_m=pres_m)

@app.route("/moyenne_humidite")
def humidite_html():
	refresh()
	global humi_m
	return render_template('sub_hum.html', humi_m=humi_m)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

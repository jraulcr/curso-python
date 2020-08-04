from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	#return 'Hola mundo'
	#Cuando se crea la carpeta se le llamara 'templates' para que el servidor lo reconozca
	return render_template('home.html')

@app.route('/about')
def about():
	#return 'Acerca de'
	return render_template('about.html')

if __name__ == '__main__':
	#app.run()
	#Para no reiniciar a menudo la aplicacion, insertamos 'debug=True'
	app.run(debug=True)
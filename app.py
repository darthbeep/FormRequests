#This is officially my sigunature and it is mine.

#<Firstname> <Lastname>
#SoftDev1 pd<p>
#HW<n> -- <Title/Topic/Summary>
#<yyyy>-<mm>-<dd>

from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)


@app.route('/')
def index():
	return '<a href="/login">life would be so much more fun if you used the login page</a>'


@app.route('/login', methods=['GET', 'POST'])
def login():
	searchword = request.args.get('name', '') #If you look closely you can tell I got help online
	if request.method == 'POST':
		return render_template('echo.html', name=request.form['name'], req=request.method)
	if request.method == 'GET' and searchword != '':
		return render_template('echo.html', name=searchword, req=request.method)
	return render_template('form.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)

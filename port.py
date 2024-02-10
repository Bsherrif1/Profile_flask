from flask import Flask, render_template, url_for, request, redirect
import csv
#using flask class to instantiate an app.
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')

# @app.route('/work')
# def work():
#     return render_template('./work.html')

# @app.route('/works')
# def works():
#     return render_template('./works.html')

# @app.route('/components')
# def components():
#     return render_template('./components.html')

# @app.route('/contact')
# def contact():
#     return render_template('./contact.html')

# @app.route('/thank')
# def thank():
#     return render_template('./thankyou.html')

# @app.route('/about')
# def about():
#     return render_template('./about.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# @app.route('/submit_form', methods=['POST', 'GET'])
# def login(error):
#     return render_template('login.html', error=error)


# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     # return render_template('login.html', error=error)
#     return 'form submitted oshey akowe.'

@app.route('/route_name')
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, \n{subject}, \n{message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # csv_write = database2.write(f'\n{email}, \n{subject}, \n{message}')
        csv_write = csv.writer(database2, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # return render_template('login.html', error=error)
    if request.method == 'POST':
        data = request.form.to_dict()
        # print(data)
        # write_to_file(data)
        write_to_csv(data)
        # return 'form submitted successfully'
        return redirect('./thankyou.html')
    else:
        return 'something went wrong. Try again!'


# @app.route('/submit_form', methods=['POST','GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'], request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     return render_template('login.html', error=error)
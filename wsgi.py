from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "OpenShift Hello World!"

    
@application.route('/')
def main():
    return "Hello word"

@application.route('/iot', methods=['GET', 'POST'])
def index():
    return "IOT"

@application.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


if __name__ == "__main__":
    application.run()

from flask import Flask, render_template, abort

app = Flask(__name__)

app.config.from_pyfile('settings.py')

#The PAGE not found error being handled
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

#The Internal Server error being handled
@app.errorhandler(500)
def internal(error):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/messages/<int:idx>/')
def message(idx):
    # Logging within the application
    app.logger.info('Building the messages list ...')
    messages = ['Message Zero', 'Message One', 'Message Two']
    try:
        app.logger.debug('Getting the message with index: {}'.format(idx))
        return render_template('message.html', messages=messages[idx])
    except IndexError:
        app.logger.error('Index: {} is causing the index Error'.format(idx))
        abort(404)



#Route to see the Internal server error in action
@app.route('/500')
def error500():
    abort(500)

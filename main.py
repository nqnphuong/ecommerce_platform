from flask import render_template
from ecommerce_platform import create_app
import setting

app = create_app()


@app.route('/')
@app.route("/home")
def home():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host=setting.FLASK_HOST, port=setting.FLASK_PORT, debug=setting.FLASK_DEBUG)
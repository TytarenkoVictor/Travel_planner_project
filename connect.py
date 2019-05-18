from flask import Flask, request, render_template
import main
app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def register():
    try:
        u_from = request.form.get("location1")
        u_to = request.form.get("location2")
        d_from = request.form.get("date1")
        d_to = request.form.get("date2")
        main.main(u_from, u_to, d_from, d_to)
    except:
        return render_template('error.html')
    return render_template('file.html')


@app.after_request
def add_header(request):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    request.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    request.headers["Pragma"] = "no-cache"
    request.headers["Expires"] = "0"
    request.headers['Cache-Control'] = 'public, max-age=0'
    return request

if __name__ == '__main__':
    app.run(debug=True)

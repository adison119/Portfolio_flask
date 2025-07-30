from flask import Flask, render_template, request, redirect, url_for
from livereload import Server
app = Flask(__name__)

# หน้าแรก
@app.route('/')
def index():
    return render_template('index.html',title = 'Homepage')

# # แบบฟอร์มส่งข้อมูล
# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     # ประมวลผลข้อมูลหรือบันทึกลงฐานข้อมูลได้ที่นี่
#     return f'สวัสดี {name}! ขอบคุณที่ส่งข้อมูลเข้ามา.'
# หน้าเกี่ยวกับ
@app.route('/about')
def about():
    return render_template('about.html',title = 'About me')

@app.route('/project')
def project():
    return render_template('project.html',title = '')
# หน้า 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

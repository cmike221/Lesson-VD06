from flask import render_template, request, redirect, url_for
from app import app

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tittle = request.form.get('tittle')
        content = request.form.get('content')
        if tittle and content:
            posts.append({'tittle': tittle, 'content': content})
            return redirect(url_for('index'))
    return render_template('blog.html', posts=posts)




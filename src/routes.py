from app import app
from flask import (
        redirect,
        render_template,
        request,
        session,
        flash
    )

@app.route("/")
def home():
    return render_template("page.html")

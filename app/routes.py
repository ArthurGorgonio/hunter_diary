from flask import render_template


def index(user):
    try:
        page = render_template('index.html', title="Home", user=user)

        return page
    except:
        raise

        return "Template not found", 404

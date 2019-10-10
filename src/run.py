from app import app
from pymodm import connect

if __name__ == "__main__":
    connect('mongodb://mongo:27017/char')
    app.run(host="0.0.0.0", debug=True)

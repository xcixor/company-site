"""Creates and runs the app"""

from app import create_app

app = create_app('default')

if __name__ == '__main__':
    app.run(debug=True)
    
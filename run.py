from app import app

print(f'inside run.py2')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

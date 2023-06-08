from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8001, debug=False)
    print(f'Server is running on http://0.0.0.0:8001/')

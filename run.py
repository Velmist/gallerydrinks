from app import app

@app.route('/')
def home():
    return "¡Hola, mundo!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) #puerto para el host
    app.run(host="0.0.0.0", port=port)

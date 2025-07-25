from app import db, CreateApp
app = CreateApp()
app = app .getapp()

with app.app_context():
    db.create_all()  
    print("Database and tables created.")

if __name__ == '__main__':
    app.run(debug=True)

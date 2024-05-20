from flask import Flask
from src.routes.CreateORUpdateUser import create_update_blueprint
from src.routes.DeleteUser import delete_blueprint
from src.routes.scheduleEndpoint import schedule_blueprint
from src.routes.IteratorDailyEndpoint import start_schedule_blueprint
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'
toolbar = DebugToolbarExtension(app)
app.register_blueprint(create_update_blueprint)
app.register_blueprint(delete_blueprint)
app.register_blueprint(schedule_blueprint)
app.register_blueprint(start_schedule_blueprint)

        
if __name__ == "__main__":
    app.run(debug=True)
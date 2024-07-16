from datetime import datetime, timedelta, timezone
import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager,get_jwt,get_jwt_identity, jwt_required, create_access_token,set_access_cookies
from src.routes.users import users_blueprint
from src.routes.schedule import schedule_blueprint
from src.routes.news import news_blueprint
from src.routes.auth import auth_blueprint
from src.routes.crontab import cron_blueprint

app = Flask(__name__)

CORS(app,supports_credentials=True,origins=["http://localhost:3000"])
app.config.from_object('config.Config')

jwt = JWTManager(app)


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response
    
    

# app.register_blueprint(start_schedule_blueprint, url_prefix="/api/v1")
app.register_blueprint(users_blueprint, url_prefix="/api/v1")
app.register_blueprint(schedule_blueprint, url_prefix="/api/v1")
app.register_blueprint(news_blueprint, url_prefix="/api/v1")
app.register_blueprint(auth_blueprint, url_prefix="/api/v1")
app.register_blueprint(cron_blueprint, url_prefix="/api/v1")

        
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
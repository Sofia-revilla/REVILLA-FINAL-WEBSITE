import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
# Allow your future Vue app to talk to this backend
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Connect to Supabase
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Backend is running!"}), 200

# GET Method: Fetch all comments for the guestbook
@app.route('/api/messages', methods=['GET'])
def get_messages():
    try:
        response = supabase.table('guestbook').select('*').order('created_at', desc=True).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST Method: Add a new comment to the guestbook
@app.route('/api/messages', methods=['POST'])
def add_message():
    try:
        data = request.json
        name = data.get('name', 'Anonymous')
        message = data.get('message')
        
        if not message:
            return jsonify({"error": "Message is required"}), 400
        
        # Insert into Supabase
        response = supabase.table('guestbook').insert({"name": name, "message": message}).execute()
        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return f"<h1>Welcome</h1>"

@app.route('/get_info', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    day_of_week = datetime.datetime.now().strftime('%A')

    # Get current UTC time with validation of +/-2 hours
    utc_time = datetime.datetime.utcnow()
    
    # Construct response data
    response_data = {
        'Slack_name': slack_name,
        'Current_day_of_week': day_of_week,
        'Current_UTC_time': utc_time.isoformat(),
        'Track': track,
        'GitHub_URL_of_file': 'https://github.com/ByteScrib/king/blob/main/backend/app.py',
        'GitHub_URL_of_source_code': 'https://github.com/ByteScrib/king',
        'Status_Code': 'Success'
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request

app = Flask(__name__)

# Log IPs of visitors
log_file = "camera_access_log.txt"

@app.route('/log', methods=['POST'])
def log_ip():
    data = request.json
    with open(log_file, "a") as file:
        file.write(f"Access from {data['ip']} at {data['timestamp']}\n")
    return {"status": "logged"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route('/stream', methods=['POST'])
def receive_stream():
    with open("camera_feed.webm", "ab") as f:
        f.write(request.data)
    return {"status": "streaming"}, 200

from flask import Flask, jsonify, request
import os

app = Flask(__name__)
LIKE_FILE = "likes.txt"

def read_likes():
    if not os.path.exists(LIKE_FILE):
        with open(LIKE_FILE, "w") as f:
            f.write("0")
    with open(LIKE_FILE, "r") as f:
        try:
            return int(f.read())
        except ValueError:
            return 0

def write_likes(count):
    with open(LIKE_FILE, "w") as f:
        f.write(str(count))

@app.route("/", methods=["GET", "POST"])
def like_api():
    count = read_likes()

    if request.method == "POST":
        count += 1
        write_likes(count)
        return jsonify({"message": "Liked!", "total_likes": count})
    else:
        return jsonify({"total_likes": count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

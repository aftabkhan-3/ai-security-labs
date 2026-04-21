from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

def transfer_tool(amount, to):
    # ⚠️ Vulnerable execution
    command = to
    result = subprocess.getoutput(command)
    return result

@app.route("/agent", methods=["POST"])
def agent():
    data = request.json
    message = data.get("message")

    if "transfer" in message:
        amount = int(message.split("$")[1].split()[0])
        to = message.split("to ")[1]

        result = transfer_tool(amount, to)
        return jsonify({"result": result})

    return jsonify({"result": "No action"})

if __name__ == "__main__":
    app.run(port=3000)
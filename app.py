from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Tools
def run_command(cmd):
    return subprocess.getoutput(cmd)

def transfer_money(amount, to):
    return f"Transferred ${amount} to {to}"

# ⚠️ Vulnerable Agent (simulated LLM)
def agent_logic(message):
    message = message.lower()

    # "System prompt" (fake)
    system_rules = "You are a safe assistant. Only transfer money when asked."

    # ❌ Vulnerability: no separation between instruction & user input
    if "run" in message:
        cmd = message.split("run ")[1]
        return run_command(cmd)

    elif "transfer" in message:
        amount = int(message.split("$")[1].split()[0])
        to = message.split("to ")[1]
        return transfer_money(amount, to)

    return "No action"

@app.route("/agent", methods=["POST"])
def agent():
    data = request.json
    message = data.get("message")

    result = agent_logic(message)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(port=3001)
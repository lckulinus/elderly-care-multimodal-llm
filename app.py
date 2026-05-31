from quart import Quart, request, jsonify, render_template
from llm.qwen_client import ask_qwen

app = Quart(__name__)

@app.route("/")
async def index():
    return await render_template("index.html")

@app.route("/chat", methods=["POST"])
async def chat():
    data = await request.get_json()
    message = data.get("message", "")
    answer = await ask_qwen(message)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)

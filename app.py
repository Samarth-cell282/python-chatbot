from flask import Flask, request, jsonify, render_template_string
from chatbot import chatbot_response

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Samarth Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 40px auto;
            padding: 20px;
            background: #f4f4f4;
        }
        #chat {
            background: white;
            padding: 20px;
            min-height: 250px;
            border-radius: 10px;
            margin-bottom: 15px;
        }
        input {
            width: 70%;
            padding: 12px;
        }
        button {
            padding: 12px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Samarth Chatbot 🤖</h1>
    <div id="chat"></div>
    <input id="message" placeholder="Type your message...">
    <button onclick="sendMessage()">Send</button>

    <script>
        async function sendMessage() {
            const input = document.getElementById("message");
            const chat = document.getElementById("chat");
            const message = input.value.trim();

            if (!message) return;

            chat.innerHTML += "<p><b>You:</b> " + message + "</p>";
            input.value = "";

            try {
                const response = await fetch("/chat", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({message: message})
                });

                const data = await response.json();
                const reply = document.createElement("p");
                reply.textContent = "Bot: " + data.reply;
                chat.appendChild(reply);
            } catch (error) {
                chat.innerHTML += "<p>Unable to contact the chatbot.</p>";
            }
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message", "")
    reply = chatbot_response(message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, json
import config, json, requests
import pyautogui

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('dashboard.html')

@app.route('/g20webhook/',methods=['POST'])
def webhook():
    webhook_message = json.loads(request.data)

    if webhook_message['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            'code': 'error',
            'message': 'wrong password'
        }

    action = str(webhook_message['action'])

    if action == "Long":
        print("Long")
        pyautogui.click(x=1047, y=475)
    if action == "Short":
        print("Short")
        pyautogui.click(x=1047, y=506)
    if action == "Exit":
        pyautogui.click(x=1227, y=440)
        print("Exit")

    return action

if __name__ == '__main__':
    app.run(debug=True)
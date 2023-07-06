# webhook-tradingview-lux

Step 1:
Register and download Ngrok: https://ngrok.com/
Download PyCharm: https://www.jetbrains.com/pycharm/ (other python editor and runners might work)
Download Mpos: https://sourceforge.net/projects/mpos/files/v.0.5/
Download the config.py, __init__.py and dashboard.html

Step 2:
Create a new project in PyCharm and import my files.

Step 3.
Click on terminal in PyCharm and install the following:
pip install pyautogui
pip install flask
pip install requests
pip install config
pip install json

Step 4.
Open MPos and find the correct X and Y cordinates for Buy Mkt, Sell Mkt and Close. 
Swap them to yours in the python code.

Run the Python code, wait for it to start. 

Step 5. 
Open Ngrok and tyupe ngrok.exe http 5000
Copy the forwarding URL

Step 6. 
https://www.tradingview.com/script/q73IArst-Webhook-OG/
https://www.tradingview.com/script/nffua7ew-Webhook-Smart-Trail/

In trading view add the two different indicators and select correct soruces in their settings.
Add alarts and choose alert() function calls only, in notifications paste in your forward webhook link from ngrok.

Step 7.
Let python run have the NjinjaTrader windows open and visable.

DM me if you have any question, will try to make a video. 

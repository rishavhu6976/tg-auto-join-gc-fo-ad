<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Telegram Auto Group Joiner</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      max-width: 900px;
      margin: auto;
      padding: 20px;
      background: #0d1117;
      color: #c9d1d9;
    }
    h1, h2, h3 {
      color: #58a6ff;
    }
    code {
      background: #161b22;
      padding: 4px 6px;
      border-radius: 5px;
      display: inline-block;
    }
    pre {
      background: #161b22;
      padding: 15px;
      border-radius: 8px;
      overflow-x: auto;
    }
    .box {
      background: #161b22;
      padding: 15px;
      border-left: 4px solid #58a6ff;
      margin: 15px 0;
    }
  </style>
</head>
<body>

<h1>🚀 Telegram Auto Group Joiner</h1>

<p>
Automate joining multiple groups on 
<strong>Telegram</strong> using Python and Pyrogram.
</p>

<div class="box">
Bulk join public & private groups with smart rate-limit handling and summary reports.
</div>

<h2>✨ Features</h2>
<ul>
  <li>Join hundreds of groups automatically</li>
  <li>Removes duplicate links</li>
  <li>Handles FloodWait, PeerFlood, invalid links</li>
  <li>Adjustable delay system</li>
  <li>Final summary output</li>
</ul>

<h2>🧰 Tech Stack</h2>
<ul>
  <li>Python 3</li>
  <li>Pyrogram</li>
  <li>TgCrypto</li>
</ul>

<h2>📦 Installation</h2>
<pre>
git clone https://github.com/your-username/telegram-auto-joiner.git
cd telegram-auto-joiner
pip install pyrogram tgcrypto
</pre>

<h2>⚙️ Configuration</h2>
<pre>
API_ID = 123456
API_HASH = "your_api_hash"
SESSION_NAME = "joiner_session"
DELAY_BETWEEN_JOINS = 4
</pre>

<h2>🔑 Get API Credentials</h2>
<ol>
  <li>Go to https://my.telegram.org</li>
  <li>Login with your phone</li>
  <li>Create an app</li>
  <li>Copy API ID & Hash</li>
</ol>

<h2>📂 Input Groups</h2>
<pre>
RAW_LINKS = """
https://t.me/group1
https://t.me/+invitehash
"""
</pre>

<h2>▶️ Usage</h2>
<pre>
python main.py
</pre>

<h2>📊 Output Example</h2>
<pre>
[  1/500] @group → joined
[  2/500] @group → already_in
[  3/500] @group → invalid_link
</pre>

<h2>⚠️ Limitations</h2>
<ul>
  <li>Telegram group limit ~500</li>
  <li>Fast joining may cause bans</li>
</ul>

<h2>🛡️ Safety Tips</h2>
<ul>
  <li>Use secondary account</li>
  <li>Increase delay if needed</li>
  <li>Avoid spam groups</li>
</ul>

<h2>📁 Project Structure</h2>
<pre>
telegram-auto-joiner/
│── main.py
│── requirements.txt
│── README.md
</pre>

<h2>📜 License</h2>
<p>MIT License</p>

<h2>🚫 Disclaimer</h2>
<p>
This project is for educational purposes only. Misuse may violate Telegram terms.
</p>

</body>
</html>

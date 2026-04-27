<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Telegram Auto Group Joiner</title>

  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial;
      background: #0d1117;
      color: #c9d1d9;
      line-height: 1.6;
    }

    .container {
      max-width: 900px;
      margin: auto;
      padding: 30px 20px;
    }

    h1 {
      font-size: 2.2rem;
      color: #58a6ff;
      margin-bottom: 10px;
    }

    h2 {
      margin-top: 30px;
      margin-bottom: 10px;
      color: #58a6ff;
      border-bottom: 1px solid #30363d;
      padding-bottom: 5px;
    }

    p {
      margin: 10px 0;
    }

    ul {
      margin-left: 20px;
      margin-top: 10px;
    }

    li {
      margin-bottom: 8px;
    }

    pre {
      background: #161b22;
      padding: 15px;
      border-radius: 8px;
      overflow-x: auto;
      margin-top: 10px;
    }

    code {
      background: #161b22;
      padding: 3px 6px;
      border-radius: 5px;
    }

    .box {
      background: #161b22;
      padding: 15px;
      border-left: 4px solid #58a6ff;
      margin: 20px 0;
      border-radius: 6px;
    }

    .footer {
      margin-top: 40px;
      font-size: 0.9rem;
      color: #8b949e;
      text-align: center;
    }

    .badge {
      display: inline-block;
      background: #238636;
      color: white;
      padding: 5px 10px;
      border-radius: 5px;
      margin-right: 5px;
      font-size: 0.85rem;
    }

  </style>
</head>

<body>
  <div class="container">

    <h1>🚀 Telegram Auto Group Joiner</h1>

    <p>
      Automate joining multiple groups on <strong>Telegram</strong> using Python and Pyrogram.
    </p>

    <div class="box">
      Bulk join public & private groups with smart rate-limit handling and summary reports.
    </div>

    <div>
      <span class="badge">Python</span>
      <span class="badge">Pyrogram</span>
      <span class="badge">Automation</span>
    </div>

    <h2>✨ Features</h2>
    <ul>
      <li>Join hundreds of groups automatically</li>
      <li>Removes duplicate links</li>
      <li>Handles FloodWait, PeerFlood, invalid links</li>
      <li>Adjustable delay system</li>
      <li>Final summary output</li>
    </ul>

    <h2>📦 Installation</h2>
    <pre>
git clone https://github.com/your-username/telegram-auto-joiner.git
cd telegram-auto-joiner
pip install -r requirements.txt
    </pre>

    <h2>⚙️ Configuration</h2>
    <pre>
API_ID = 123456
API_HASH = "your_api_hash"
SESSION_NAME = "joiner_session"
DELAY_BETWEEN_JOINS = 4
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
      <li>Fast joining may trigger FloodWait</li>
    </ul>

    <h2>🛡️ Safety Tips</h2>
    <ul>
      <li>Use a secondary account</li>
      <li>Increase delay if needed</li>
      <li>Avoid spam groups</li>
    </ul>

    <h2>📜 License</h2>
    <p>MIT License</p>

    <div class="footer">
      Made for educational purposes • Use responsibly
    </div>

  </div>
</body>
</html>

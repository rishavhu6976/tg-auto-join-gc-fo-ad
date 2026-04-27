# 🚀 Telegram Auto Group Joiner

Automate joining multiple Telegram groups using Python and Pyrogram.

> Bulk join public & private groups with smart rate-limit handling and detailed summary reports.

---

## ✨ Features

- 🔗 Join **hundreds of Telegram groups automatically**
- 🔁 Removes duplicate links
- ⚠️ Handles Telegram limits:
  - FloodWait
  - PeerFlood
  - Invalid / expired links
  - Already joined groups
- ⏱ Adjustable delay between joins
- 📊 Clean final summary report

---

## 🧰 Tech Stack

- Python 3
- Pyrogram
- TgCrypto

---

## 📦 Installation

```bash
git clone https://github.com/rishavhu6976/tg-auto-join-gc-fo-ad.git
cd tg-auto-join-gc-fo-ad
pip install -r requirements.txt
⚙️ Configuration

Edit the script and update:

API_ID = 123456
API_HASH = "your_api_hash"
SESSION_NAME = "joiner_session"
DELAY_BETWEEN_JOINS = 4
🔑 Get Telegram API Credentials
Go to https://my.telegram.org
Login with your phone number
Click API Development Tools
Create a new app
Copy your api_id and api_hash
📂 Input Groups

Modify the RAW_LINKS variable:

RAW_LINKS = """
https://t.me/group1
https://t.me/+invitehash
"""

✔ Supported formats:

Public groups → https://t.me/groupname
Private invite links → https://t.me/+hash
▶️ Usage
python main.py
📊 Example Output
[  1/500] @groupname → joined
[  2/500] @groupname → already_in
[  3/500] @groupname → invalid_link
Final Summary
✅ Newly joined
👤 Already in
🔗 Invalid links
🚫 Banned
⚠️ Flood issues
⏳ Wait handled
❌ Errors
⚠️ Limitations
Telegram group/channel limit ≈ 500
Fast joining may trigger FloodWait / PeerFlood
Some groups may auto-ban new users
🛡️ Safety Tips
Use a secondary Telegram account

Increase delay if you hit limits:

DELAY_BETWEEN_JOINS = 10
Avoid suspicious or spam groups
📁 Project Structure
telegram-auto-joiner/
│── main.py
│── requirements.txt
│── README.md
📜 requirements.txt
pyrogram>=2.0.106
tgcrypto>=1.2.5
🚫 Disclaimer

This project is for educational purposes only.
Using automation aggressively may violate Telegram’s Terms of Service and can result in account restrictions or bans.

⭐ Contributing

Pull requests are welcome!
If you have ideas (multi-account, proxy support, GUI), feel free to contribute.

📄 License

MIT License

💬 Support

If you found this useful, consider giving the repo a ⭐


---

### 👍 Why this is “perfect”
- ✅ 100% GitHub compatible (Markdown only)
- ✅ Clean sections + emojis (modern style)
- ✅ No broken HTML/CSS
- ✅ Ready for public repo
- ✅ Scalable (you can add badges later)

---

If you want next upgrade, I can:
- add **GitHub badges (stars, forks, license, Python version)**  
- create a **pro-level README like top repos**  
- add **screenshots + GIF demo** 🚀

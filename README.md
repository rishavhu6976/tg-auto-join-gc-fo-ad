# 📲 Telegram Group Auto-Joiner

A Python script that automatically joins a list of Telegram groups/channels using the [Pyrogram](https://docs.pyrogram.org/) MTProto client.

---

## ✨ Features

- ✅ Supports **public usernames** (`t.me/username`) and **private invite links** (`t.me/+hash`)
- 🛡️ Graceful error handling: `FloodWait`, `PeerFlood`, bans, expired links, group limits
- 🔁 Auto-deduplication of the link list before processing
- 📊 Live progress log + final summary report
- 🛑 Auto-stops when Telegram's group membership limit is reached

---

## 📦 Requirements

- Python **3.8+**
- Pyrogram + TgCrypto

```bash
pip install pyrogram tgcrypto
```

---

## ⚙️ Setup

### 1. Get API credentials

Go to [my.telegram.org](https://my.telegram.org), log in, and create an app to get your **API ID** and **API Hash**.

### 2. Edit the config

Open the script and fill in your credentials at the top:

```python
API_ID   = 123456          # From my.telegram.org
API_HASH = "your_api_hash"
SESSION_NAME = "joiner_session"
DELAY_BETWEEN_JOINS = 4    # Seconds between each join
```

### 3. Add your group links

Paste your group URLs into the `RAW_LINKS` string (one per line):

```python
RAW_LINKS = """
https://t.me/+SomePrivateHash
https://t.me/SomePublicGroup
...
"""
```

### 4. Run the script

```bash
python joiner.py
```

> On first run, Pyrogram will ask for your phone number and OTP to create a session file.

---

## 🔧 Configuration

| Variable | Default | Description |
|---|---|---|
| `API_ID` | — | Your Telegram API ID |
| `API_HASH` | — | Your Telegram API Hash |
| `SESSION_NAME` | `joiner_session` | Name of the saved `.session` file |
| `DELAY_BETWEEN_JOINS` | `4` | Seconds to wait between each join request |
| `RAW_LINKS` | — | Newline-separated list of group URLs |

---

## 📋 Sample Output

```
==================================================
  🤖 Logged in as: John (@john_doe)
  📋 Total groups to process: 320
==================================================

[  1/320] @SomeGroup                          → joined
[  2/320] @AnotherGroup                       → already_in
[  3/320] @+ExpiredHash                       → invalid_link
...

==================================================
           📊  FINAL SUMMARY
==================================================
  ✅  Newly joined      : 42
  👤  Already in        : 18
  🔗  Invalid/expired   : 5
  🚫  Banned            : 1
  ⚠️   Peer flood hit    : 0
  ⏳  Flood waited      : 2
  ❌  Errors            : 3
  📦  Group limit hit   : 0
──────────────────────────────────────────────────
  📌  Total processed   : 71 / 320
==================================================
```

---

## ⚠️ Notes

- Telegram limits accounts to **500 groups/channels** total. The script stops automatically when this limit is hit.
- Keep `DELAY_BETWEEN_JOINS` at **4+ seconds** to avoid flood errors. Use **10–15s** for newer accounts.
- This uses a **user account** (not a bot token) — use responsibly and in accordance with [Telegram's Terms of Service](https://telegram.org/tos).

---

## 📄 License

MIT

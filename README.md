# auto-react-telethon
Telethon auto reaction bot

## How to install

Simply clone the repo and install requirements

### Clone

```bash
git clone https://github.com/viraj-bookanna/auto-react-telethon.git
```

### Installing requirements

```bash
cd auto-react-telethon
```

```bash
pip install -r requirements.txt
```

## Usage

You have to set environment variables with .env file or in yor system

Example .env file

```
API_ID=00000000
API_HASH=00000000000000000000000000000000
STRING_SESSION=base64_session
DELAY=10
TARGET=https://t.me/blah
EMOJI=💩
```

Then run bot with:

```bash
python bot.py
```

Have Fun !
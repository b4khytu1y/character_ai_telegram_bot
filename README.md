# Telegram Bot with Character.AI

This is a simple Telegram bot that uses Character.AI as a conversation partner.

## How to Deploy on Railway

1. Fork this repo to your GitHub.
2. Go to [Railway](https://railway.app).
3. Click "New Project" -> "Deploy from GitHub Repo".
4. Add the following environment variables in Railway:
   - `TELEGRAM_BOT_TOKEN`
   - `CHARACTER_TOKEN`
   - `CHARACTER_ID`
5. Click "Deploy" — and you're done!

> You can find your Character ID in the character's URL:
> `https://beta.character.ai/chat?char=YOUR_CHARACTER_ID_HERE`
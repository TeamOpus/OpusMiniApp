# Opus Mini App 🎧

This is the web frontend + API backend for the Opus Telegram Music Bot.

- Built using Flask
- Plays audio for Mini App users in sync
- Fetches music queue from MongoDB

## 🌐 Deploy on Render

1. Create a new web service on [Render](https://render.com/)
2. Connect this repo
3. Set environment variable: `MONGO_URI`
4. Done!

## Endpoints

- `/group/<chat_id>` — Mini App page
- `/api/queue/<chat_id>` — Get queue
- `/api/pop/<chat_id>` — Skip to next

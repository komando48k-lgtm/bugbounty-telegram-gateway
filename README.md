# BugBounty Telegram Gateway

Telegram-first gateway for organizing **authorized bug-bounty** work. It provides a small agent-style interface for targets, findings, report drafts, and optional LLM analysis of user-supplied in-scope data.

> This is a clean implementation inspired by the gateway concept described in the project brief; it does not copy third-party source code.

## Safety boundary
The bot does not execute unrestricted scanning, exploitation, credential attacks, persistence, or actions against arbitrary hosts. Targets are recorded as program scope, and the assistant works with information the user supplies from authorized testing.

## Quick start

1. Create a Telegram bot with BotFather and keep the token private.
2. Copy `.env.example` to `.env` and set `TELEGRAM_BOT_TOKEN`.
3. Optionally set `TELEGRAM_ALLOWED_USER_IDS` to restrict who can use the bot.
4. Install: `python -m pip install -r requirements.txt`
5. Run: `python -m app.main`

Or with Docker:

```bash
docker compose up --build
```

## Commands

- `/start`, `/help`, `/status`
- `/target add example.com | Program Name`
- `/target list`
- `/target remove example.com`
- `/finding add example.com | Missing security header | low | Evidence and notes`
- `/finding list`
- `/report 1`
- `/ask Summarize the finding and suggest report wording`

All secrets stay in environment variables and are excluded from Git.

#!/usr/bin/env bash
source venv/bin/activate
gunicorn app:app \
    --log-file=production.log \
    --bind=unix:/tmp/bot.socket \
    --workers=1

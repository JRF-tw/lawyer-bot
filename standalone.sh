#!/usr/bin/env bash
gunicorn app:app \
    --log-file=production.log \
    --bind=unix:/tmp/bot.socket \
    --workers=1

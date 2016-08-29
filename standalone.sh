#!/usr/bin/env bash
source venv/bin/activate
gunicorn app:app \
    --log-file=production.log \
    --bind=unix:/var/run/gunicorn/jrf_bot.socket \
    --workers=1 \
    --pidfile=/var/run/gunicorn/jrf_bot.pid \
    --daemon

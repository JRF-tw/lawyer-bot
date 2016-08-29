#!/usr/bin/env bash
source venv/vin/activate
sudo -u www-data gunicorn app:app \
    --log-file=production.log \
    --bind=unix:/tmp/bot.socket \
    --workers=1

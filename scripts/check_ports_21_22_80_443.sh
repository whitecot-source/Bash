#!/bin/bash
for port in {21,22,23,80,443,8080}; do
    nc -z localhost $port 2>/dev/null && echo "[+] Порт $port открыт" || echo "[!] Порт $port закрыт"
done

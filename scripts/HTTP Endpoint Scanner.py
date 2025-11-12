import signal
import requests
import argparse
import sys

parser = argparse.ArgumentParser(description="Утилита для сканирования веб-сервера")
parser.add_argument("-u", "--url", required=True, help="URL адрес цели")
parser.add_argument("-w", "--wordlist", required=True, help="Путь к словарю")
args = parser.parse_args()

def signal_handler(sig, frame):
    print("[!] Сканирование прервано")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print (""" 
HTTP Endpoint Scanner
Утилита для проверки наличия common файлов и директорий на веб-сервере
""")
l_wordlist = []
try:
    with open(args.wordlist, "r", encoding="utf-8") as file:
        l_wordlist = [line.strip() for line in file if line.strip()]
    for i in l_wordlist:
        print (f'{args.url+i}{requests.get(args.url+i)}')
except FileNotFoundError:
    print("Ошибка, файл не найден")


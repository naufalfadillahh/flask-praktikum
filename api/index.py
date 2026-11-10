"""Entry point Vercel: menggabungkan beberapa aplikasi Flask praktikum di bawah satu domain."""
import importlib.util
import os
import sys

from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_app(folder, module_name):
    spec = importlib.util.spec_from_file_location(module_name, os.path.join(ROOT, folder, "app.py"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module  # Flask memakai sys.modules untuk menemukan templates/ dan static/
    spec.loader.exec_module(module)
    return module.app


APPS = [
    ("/biodata", "biodata", "Biodata Naufal", "Halaman profil dan biodata dengan Flask dan Bootstrap.", "Pemrograman Web"),
    ("/tebak-angka", "pemjar-pert7", "Game Tebak Angka", "Tebak angka 1 sampai 100 dengan 5 nyawa, memakai session Flask.", "Pemrograman Jaringan · Pertemuan 7"),
    ("/video-player", "pemjar-pert6", "Video Player", "Pemutar video dengan kontrol JavaScript dan Flask-Bootstrap.", "Pemrograman Jaringan · Pertemuan 6"),
]

mounts = {prefix: load_app(folder, folder.replace("-", "_")) for prefix, folder, *_ in APPS}

home = Flask(__name__)


@home.route("/")
def index():
    cards = "".join(
        f'<a class="card" href="{prefix}/"><b>{title}</b><p>{desc}</p><span>{course}</span></a>'
        for prefix, _, title, desc, course in APPS
    )
    return f"""<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Flask Praktikum — Naufal Fadillah</title>
<style>
:root{{--bg:#F4F5F7;--ink:#0F1A3A;--muted:#646C86;--line:#E1E4EC;--hl:#F7E733}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 "Segoe UI",system-ui,sans-serif}}
header{{background:var(--ink);color:#fff;padding:48px 16px 40px}}
.wrap{{max-width:960px;margin:0 auto}}
h1{{margin:0;font-size:clamp(26px,5vw,40px)}}
header p{{margin:8px 0 0;color:#C9D1E0}} header a{{color:var(--hl)}}
main{{padding:32px 16px 56px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}}
.card{{display:block;background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px;text-decoration:none;color:inherit;transition:transform .15s,box-shadow .15s}}
.card:hover{{transform:translateY(-3px);box-shadow:0 12px 24px -14px rgba(15,26,58,.4)}}
.card b{{font-size:18px}} .card p{{margin:6px 0 10px;color:var(--muted);font-size:14.5px}}
.card span{{font-size:12.5px;font-weight:600;color:#2148D8}}
</style></head><body>
<header><div class="wrap"><h1>Flask Praktikum</h1>
<p>Aplikasi Python Flask dari praktikum kuliah Universitas Gunadarma. <a href="https://naufal-fadillah.vercel.app">← Portofolio</a></p></div></header>
<main class="wrap"><div class="grid">{cards}</div></main>
</body></html>"""


app = DispatcherMiddleware(home, mounts)

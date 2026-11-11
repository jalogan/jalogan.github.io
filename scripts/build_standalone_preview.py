"""Synchronize the standalone preview's V4 custom styles with Astro CSS."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
preview=ROOT/'PREVIEW-standalone.html'
s=preview.read_text()
css=(ROOT/'src/styles/global.css').read_text()
start=s.index('/* V4 — V1 prismatic fade')
end=s.index('</style>',start)
s=s[:start]+css[css.index('/* V4 — V1 prismatic fade'):]+"\n"+s[end:]
import base64
art='data:image/webp;base64,'+base64.b64encode((ROOT/'public/art/prismatic-order.webp').read_bytes()).decode()
s=s.replace("url('/art/prismatic-order.webp')",f"url('{art}')")
preview.write_text(s)
print('Updated standalone preview')

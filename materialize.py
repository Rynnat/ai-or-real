#!/usr/bin/env python3
"""
materialize.py — images.json'daki URL tabanlı entry'leri yerel dosyaya indir.

Kullanım:
  1. curate.html'de İNDİR → indirilen images.json'ı ~/ai-or-not/'a taşı
  2. python3 materialize.py

Script:
  - URL entry'leri (https://...) sıralı yerel dosyalara indirir
  - jpegtran ile EXIF strip eder
  - sıradaki numarayı bulup nötr isim verir
  - 5KB altı (rate-limit hata JSON'u) yakaladıklarını atlar
  - images.json'ı yerel dosya isimleriyle yeniden yazar
"""
import json
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

REPO    = Path(__file__).parent
IMG_DIR = REPO / 'images'
JSON    = REPO / 'images.json'

DELAY_S      = 1.5   # rate-limit dostu fetch arası bekleme
MIN_SIZE     = 5000  # bundan küçük yanıt = hata, atla
FETCH_TIMEOUT= 60


def next_index() -> int:
    nums = []
    for p in IMG_DIR.glob('*.jpg'):
        m = re.match(r'(\d+)\.jpg$', p.name)
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


def strip_exif(src_bytes: bytes) -> bytes:
    """jpegtran stdin → stdout. Fail olursa orijinal byte'ları geri ver."""
    try:
        result = subprocess.run(
            ['jpegtran', '-copy', 'none', '-optimize'],
            input=src_bytes, capture_output=True, check=True, timeout=30
        )
        return result.stdout
    except Exception:
        return src_bytes


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) curate-materialize'
    })
    with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as r:
        return r.read()


def main():
    data = json.loads(JSON.read_text())

    idx          = next_index()
    new_data     = []
    url_entries  = []

    for e in data:
        f = e.get('f') or e.get('file', '')
        if re.match(r'^https?://', f):
            url_entries.append(e)
        else:
            new_data.append(e)  # local file — dokunma

    if not url_entries:
        print('images.json içinde URL tabanlı entry yok — yapacak iş yok')
        return

    print(f'{len(url_entries)} URL entry indirilecek (delay {DELAY_S}s arası)...')
    print()

    success = 0
    for i, e in enumerate(url_entries):
        url = e['f']
        short = url if len(url) <= 80 else url[:78] + '..'
        print(f'  [{i+1:>3}/{len(url_entries)}] {short}')
        try:
            content = fetch(url)
            if len(content) < MIN_SIZE:
                print(f'           ⚠ küçük yanıt ({len(content)}B) — atlandı')
                continue
            content = strip_exif(content)
            dest = IMG_DIR / f'{idx:02d}.jpg'
            dest.write_bytes(content)
            new_data.append({'f': dest.name, 'k': e['k']})
            idx += 1
            success += 1
            print(f'           → {dest.name} ({len(content) // 1024}KB)')
        except KeyboardInterrupt:
            print('\nİPTAL — şu ana kadarki ilerleme kaydediliyor')
            break
        except Exception as ex:
            print(f'           ✗ fail: {ex}')
        time.sleep(DELAY_S)

    JSON.write_text(json.dumps(new_data, indent=2, ensure_ascii=False) + '\n')
    print()
    print(f'✓ {success}/{len(url_entries)} indirildi · {len(url_entries) - success} atlandı')
    print(f'  images.json yeniden yazıldı, toplam: {len(new_data)} entry')
    print()
    print('Push için:')
    print('  cd ~/ai-or-not && git add images/ images.json && git commit -m "+N images" && git push')


if __name__ == '__main__':
    main()

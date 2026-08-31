#!/usr/bin/env python3
"""
add_images.py — drop görselleri sisteme entegre eder.

Kullanım:
  1. images/incoming/ai/   klasörüne AI görsellerini at (.jpg/.jpeg)
  2. images/incoming/real/ klasörüne gerçek görselleri at
  3. python3 add_images.py   çalıştır

Script:
  - jpegtran ile EXIF strip eder
  - sıradaki numarayı bulup nötr isim verir (47.jpg, 48.jpg, ...)
  - images.json'a obfuscated label ile entry ekler
  - incoming klasöründen siler (taşındı sayılır)
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO    = Path(__file__).parent
IMG_DIR = REPO / 'images'
INC     = IMG_DIR / 'incoming'
JSON    = REPO / 'images.json'

# Obfuscated labels (matches index.html _OK key 'Xq3#zT')
K_AI   = 'ORg='
K_REAL = 'KhRSTw=='


def next_index() -> int:
    nums = []
    for p in IMG_DIR.glob('*.jpg'):
        m = re.match(r'(\d+)\.jpg$', p.name)
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


def strip_and_copy(src: Path, dest: Path) -> bool:
    """jpegtran ile EXIF temizle. Fail olursa ham byte kopyala."""
    try:
        out = subprocess.run(
            ['jpegtran', '-copy', 'none', '-optimize', str(src)],
            capture_output=True, check=True, timeout=60
        ).stdout
        dest.write_bytes(out)
        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError) as e:
        # fallback: blind copy
        try:
            dest.write_bytes(src.read_bytes())
            return True
        except Exception as ee:
            print(f'  ✗ kopyalama da fail: {ee}', file=sys.stderr)
            return False


def main():
    (INC / 'ai').mkdir(parents=True, exist_ok=True)
    (INC / 'real').mkdir(parents=True, exist_ok=True)

    idx = next_index()
    new_entries = []

    for label, k in [('ai', K_AI), ('real', K_REAL)]:
        sub = INC / label
        files = sorted(p for p in sub.iterdir()
                       if p.is_file() and p.suffix.lower() in ['.jpg', '.jpeg'])
        for src in files:
            dest = IMG_DIR / f'{idx:02d}.jpg'
            if strip_and_copy(src, dest):
                src.unlink()  # incoming'den siliyoruz
                new_entries.append({'f': dest.name, 'k': k})
                print(f'  {src.name:40s} → {dest.name} [{label}]')
                idx += 1
            else:
                print(f'  ✗ {src.name} işlenemedi', file=sys.stderr)

    if not new_entries:
        ai_count   = len(list((INC / 'ai').glob('*.jp*g')))
        real_count = len(list((INC / 'real').glob('*.jp*g')))
        if ai_count == 0 and real_count == 0:
            print('Drop JPG dosyalarını:')
            print(f'  {INC / "ai"}/')
            print(f'  {INC / "real"}/')
        else:
            print(f'incoming\'de bulundu ama hiçbiri eklenemedi (AI: {ai_count}, REAL: {real_count})')
        return

    # update images.json
    data = json.loads(JSON.read_text())
    data.extend(new_entries)
    JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')

    ai_added   = sum(1 for e in new_entries if e['k'] == K_AI)
    real_added = sum(1 for e in new_entries if e['k'] == K_REAL)
    print()
    print(f'✓ {len(new_entries)} eklendi  ({ai_added} AI · {real_added} REAL)')
    print(f'  images.json toplam: {len(data)}')


if __name__ == '__main__':
    main()

// AI or Real — service worker
// Strateji: stale-while-revalidate; JSONBin çağrıları network-only
const CACHE = 'ai-or-real-v0.2.0';
const APP_SHELL = [
  './',
  './index.html',
  './lab.css?v=0.2.0',
  './manifest.json',
  './icon.svg',
  './images.json',
];

// images.json'daki tüm oyun görsellerini de precache eder; böylece "offline çalışır" iddiası
// yalnızca daha önce görülmüş görsellerle değil, ilk açılıştan itibaren gerçekten geçerli olur.
async function precacheImages(cache) {
  try {
    const res = await fetch('./images.json', { cache: 'no-store' });
    if (!res.ok) return;
    const data = await res.json();
    const paths = (Array.isArray(data) ? data : [])
      .map(e => e.f || e.file)
      .filter(f => f && !/^https?:\/\//.test(f))
      .map(f => `./images/${f}`);
    if (paths.length) {
      await Promise.all(paths.map(p => cache.add(p).catch(err => console.warn('image precache fail:', p, err))));
    }
  } catch (err) {
    console.warn('images.json precache atlandı:', err.message);
  }
}

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE)
      .then(async c => {
        await c.addAll(APP_SHELL).catch(err => console.warn('precache partial:', err));
        await precacheImages(c);
      })
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;

  let url;
  try { url = new URL(req.url); } catch { return; }

  // JSONBin gibi dinamik API'leri pas geç
  if (url.host.includes('jsonbin.io')) return;

  e.respondWith(
    caches.open(CACHE).then(async cache => {
      const cached = await cache.match(req);
      const network = fetch(req).then(res => {
        if (res && (res.status === 200 || res.type === 'opaque')) {
          cache.put(req, res.clone()).catch(() => {});
        }
        return res;
      }).catch(() => cached);
      return cached || network;
    })
  );
});

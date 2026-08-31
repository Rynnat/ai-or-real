// AI or Real — service worker
// Strateji: stale-while-revalidate; JSONBin çağrıları network-only
const CACHE = 'ai-or-real-v1';
const APP_SHELL = [
  './',
  './index.html',
  './manifest.json',
  './icon.svg',
  './images.json',
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE)
      .then(c => c.addAll(APP_SHELL).catch(err => console.warn('precache partial:', err)))
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

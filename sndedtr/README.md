# SNDEDTR

A multitrack audio editor that runs entirely in the browser. Import or record
audio, arrange it on a timeline, clean it up with per-track effects, and export
a mix - with no server, no account, and nothing ever uploaded.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole app: HTML, CSS and JavaScript in one file, no build step |
| `sw.js` | Service worker - makes the app open with no network after one visit |
| `manifest.webmanifest` | Tells the browser how to install it and which files it can open |
| `icon.svg`, `icon-192.png`, `icon-512.png`, `icon-maskable-512.png` | App icons |
| `apple-touch-icon.png`, `favicon-32.png` | Home-screen icon for iOS, tab icon |
| `make-icons.py` | Redraws every PNG icon. Run `python3 make-icons.py` after editing the mark |

## Cleaning up a recording

Two tools, for two different problems. The **noise gate** turns the track down
between words and is quick to set up. **Background noise** removal is the
better one: select a patch that is only room tone, press Learn, then reduce the
clip. It measures each frequency in the noise and subtracts that much
everywhere, so it also works underneath speech. It changes the audio rather
than filtering it during playback, so it can be undone but not switched off.

## Saving your work

`Ctrl+S` writes a `.sndedtr` file holding the arrangement, every setting and the
audio itself, and `Ctrl+O` opens one again. The audio inside is stored as 16-bit
samples rather than the 32-bit floats the browser works in: that halves the file
at a cost you cannot hear on voice, but it is a real conversion, so keep your
original recordings for mastering work.

Exports come out as WAV (16 or 24-bit), MP3, or Opus in an Ogg file. The export
dialog can also match the mix to a loudness target - -16 LUFS is the usual one
for podcasts - by measuring the mix and then rendering it again at the right
level.

## Installing it

Upload all of these to the same folder on an https host and open it. In Chrome
or Edge an install button appears in the top bar (and in the address bar); on
iOS use Share then Add to Home Screen. It then opens in its own window with no
browser furniture, and works with the network switched off.

Once installed, double-clicking a `.wav`, `.mp3`, `.m4a`, `.ogg`, `.opus`,
`.flac` or `.aac` file can open it straight into SNDEDTR - the manifest
registers the app as an audio file handler.

## Deploy ritual

Two version numbers have to move together:

1. `APP_VERSION` near the top of the JavaScript in `index.html`
2. `CACHE_VERSION` at the top of `sw.js`

Bumping `CACHE_VERSION` is what rotates the cache. Skip it and browsers that
already have the app will keep serving the old copy from disk. After uploading,
the next load fetches the new `index.html`, the new worker installs in the
background, and the app shows "A new version of SNDEDTR is ready" rather than
reloading underneath you - reloading would discard unsaved audio.

## A note on file:// versus https

Opened straight off a disk the app still works, but two things do not:

- service workers are not allowed on `file://`, so there is no install and no
  offline caching
- some browsers restrict microphone access outside a secure context

Everything else - import, edit, effects, export - works either way.

# MediaPipe Selfie Segmentation (vendor copy)

These files let TELEDTR blur or replace the background behind you. They find
the person in each camera frame **on this device**: no picture ever leaves it.

- What: MediaPipe Selfie Segmentation, the JavaScript solution, from the npm
  package `@mediapipe/selfie_segmentation` version `0.1.1675465747`, unchanged.
- By: Google. License: Apache License 2.0 (the full text is in `LICENSE.txt`).
- Loaded only when you first turn on a background effect, then kept by the
  browser (and the app's offline copy), so it works without a network after that.

| File | What it is |
|---|---|
| `selfie_segmentation.js` | the loader (it defines `SelfieSegmentation`) |
| `selfie_segmentation_solution_simd_wasm_bin.js` / `.wasm` / `.data` | the engine (WebAssembly, SIMD build) |
| `selfie_segmentation.tflite` | the model for square and upright pictures (256 x 256) |
| `selfie_segmentation_landscape.tflite` | the faster model for wide pictures (144 x 256) |
| `selfie_segmentation.binarypb` | the engine's wiring between model and output |

To update: `npm pack @mediapipe/selfie_segmentation`, and copy the same files
from its `package/` folder. Only the SIMD build is kept: every current browser
runs WebAssembly SIMD (Chrome, Edge, Firefox, Safari 16.4 and later).

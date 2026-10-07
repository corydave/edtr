#!/bin/sh
# Builds engine/addons/mediabunny/mediabunny-3dedtr.min.js: the parts of
# Mediabunny (https://mediabunny.dev, MPL-2.0, by Vanilagy) that 3DEDTR's
# video export uses - writing MP4 and WebM files from a canvas - and nothing
# else, so the file is about 220 KB instead of 690 KB.
# Run it on a computer with Node.js; nothing here is needed on the server.
# The version is pinned, so the same command always gives the same file.
set -e
dir=$(mktemp -d)
cd "$dir"
npm init -y >/dev/null
npm install --silent mediabunny@1.61.0 esbuild@0.28
cat > entry.js <<'JS'
export { Output, Mp4OutputFormat, WebMOutputFormat, BufferTarget, CanvasSource, canEncodeVideo, getFirstEncodableVideoCodec, QUALITY_HIGH, QUALITY_MEDIUM } from 'mediabunny';
JS
# --legal-comments=inline keeps Mediabunny's licence notice in the file.
npx esbuild entry.js --bundle --format=esm --minify --legal-comments=inline --outfile=mediabunny-3dedtr.min.js
cd - >/dev/null
mkdir -p engine/addons/mediabunny
cp "$dir/mediabunny-3dedtr.min.js" engine/addons/mediabunny/
echo "Made engine/addons/mediabunny/mediabunny-3dedtr.min.js"

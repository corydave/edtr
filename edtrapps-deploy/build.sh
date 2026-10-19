#!/usr/bin/env bash
set -euo pipefail
rm -rf dist
mkdir dist
cp -R apps-landing/. dist/
for d in create txtedtr pdfedtr imgedtr sndedtr videdtr scrncstr vctredtr 3dedtr dskedtr animedtr; do
  cp -R "$d" dist/
done
rm -f dist/README.md

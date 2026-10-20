#!/usr/bin/env bash
# ================================================================
# edtrapps.com - build step
# ================================================================
# Gathers what edtrapps.com serves into one folder, "dist", at the top of
# the repo:
#     dist/              <- apps-landing (the home page)
#     dist/create/       <- EDTR Studio, every app in one window
#     dist/imgedtr/      <- each app's folder, so the Studio can open the
#     dist/videdtr/ ...     apps from this same site (Open and Save work)
# Cloudflare runs this from the top of the repo before deploying. To try
# it on a Mac: bash edtrapps-deploy/build.sh   (then look in dist/).
# ================================================================
set -euo pipefail          # stop at the first error, instead of deploying half a site

# Start from an empty dist folder every time, so nothing old is left behind.
rm -rf dist
mkdir -p dist

# 1. The home page and its pictures and fonts (apps-landing in the repo).
cp -R apps-landing/. dist/

# 2. The Studio and the apps. (GAMEDTR is paused, so it isn't here.)
#    A folder that doesn't exist is skipped with a note, rather than
#    failing the whole site.
for app in create txtedtr pdfedtr imgedtr sndedtr videdtr scrncstr vctredtr 3dedtr dskedtr animedtr whtbrdr; do
  if [ -d "$app" ]; then
    cp -R "$app" dist/
  else
    echo "Note: no $app folder, skipped."
  fi
done

# 3. Leave out working files that don't belong on a website: backups,
#    Claude's scratch folders, notes and the macOS clutter files.
find dist -depth -type d \( -name "Claude outputs" -o -name "BKP" -o -name "a-old*" \) -exec rm -rf {} +
#    (Licence files stay, even the ones written as .md, like pdf-lib's.)
find dist -type f \( -name ".DS_Store" -o -name $'Icon\r' -o \( -name "*.md" ! -iname "LICENSE*" \) -o -name "*.py" \) -delete

echo "dist is ready: $(find dist -type f | wc -l) files."

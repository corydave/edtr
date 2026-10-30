#!/usr/bin/env bash
# ================================================================
# edtrapps.com - build step
# ================================================================
# Gathers what edtrapps.com serves into one folder, "dist", at the top of
# the repo:
#     dist/              <- the home page (edtrapps-site, or apps-landing on GitHub)
#     dist/create/       <- EDTR Studio, every app in one window
#     dist/imgedtr/      <- each app's folder, so the Studio can open the
#     dist/videdtr/ ...     apps from this same site (Open and Save work)
#     (The phone remote and its relay wait in staging/ until they go live:
#      see staging/README.md.)
# Cloudflare runs this from the top of the repo before deploying. To try
# it on a Mac: bash edtrapps-deploy/build.sh   (then look in dist/).
# ================================================================
set -euo pipefail          # stop at the first error, instead of deploying half a site

# Start from an empty dist folder every time, so nothing old is left behind.
rm -rf dist
mkdir -p dist

# 1. The home page and its pictures and fonts. On the Mac it lives in
#    edtrapps-site/; on GitHub the same page is in apps-landing/. Use
#    whichever is there (edtrapps-site/ first).
if [ -d edtrapps-site ]; then
  cp -R edtrapps-site/. dist/
  echo "Home page: edtrapps-site"
else
  cp -R apps-landing/. dist/
  echo "Home page: apps-landing"
fi

# 2. The Studio and the apps, found automatically, so a new app is never
#    left off by mistake (TELEDTR was, for a week): every top-level folder
#    with its own index.html AND manifest.webmanifest is an app (the Studio,
#    create/, is one too). Left out on purpose:
#      gamedtr  - paused
SKIP="gamedtr"
for dir in */; do
  app="${dir%/}"                                   # "imgedtr/" -> "imgedtr"
  case " $SKIP " in *" $app "*) echo "Skipped (on purpose): $app"; continue ;; esac
  if [ -f "$app/index.html" ] && [ -f "$app/manifest.webmanifest" ]; then
    cp -R "$app" dist/
    echo "App: $app"
  fi
done

# 3. Leave out working files that don't belong on a website: backups,
#    Claude's scratch folders, notes and the macOS clutter files.
find dist -depth -type d \( -name "Claude outputs" -o -name "BKP" -o -name "a-old*" \) -exec rm -rf {} +
#    (Licence files stay, even the ones written as .md, like pdf-lib's.)
find dist -type f \( -name ".DS_Store" -o -name $'Icon\r' -o \( -name "*.md" ! -iname "LICENSE*" \) -o -name "*.py" \) -delete

echo "dist is ready: $(find dist -type f | wc -l) files."

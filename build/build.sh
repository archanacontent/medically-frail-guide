#!/usr/bin/env bash
# Builds the website and PDF from the DITA source with DITA-OT.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="${SRC:-$HERE/../dita}"
DITA="${DITA:-dita}"
OUT="${OUT:-$HERE/../out}"
rm -rf "$OUT/site" "$OUT/pdf"
python3 "$HERE/make_svgs.py" "$SRC/images"
"$DITA" -i "$SRC/medically-frail.ditamap" -f html5 -o "$OUT/site" \
  --nav-toc=full --args.css=frail.css --args.cssroot="$HERE/html" --args.copycss=yes --args.csspath=css \
  --args.hdr="$HERE/html/header.xml" --args.ftr="$HERE/html/footer.xml" --args.hdf="$HERE/html/head.xml"
python3 "$HERE/postprocess.py" "$OUT/site" "$SRC" "$HERE"
"$DITA" -i "$SRC/medically-frail.ditamap" -f pdf -o "$OUT/pdf" --customization.dir="$HERE/pdf"
cp "$OUT/pdf/medically-frail.pdf" "$OUT/site/medically-frail.pdf"
cp "$SRC/downloads/is-this-member-exempt.pdf" "$OUT/site/is-this-member-exempt.pdf"
echo "Built $OUT/site and $OUT/pdf"

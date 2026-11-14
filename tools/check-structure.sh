#!/usr/bin/env bash
# Structure checks for the units layout (see units/README.md). Run from the repository root.
# Prints MISSING / NO HTML TWIN / NOANCHOR / NO BACKGROUND PAPER lines; no output from 1-3 means all clear.

# 1. relative links in the hub pages resolve
for f in README.md CONTENTS.md units/README.md units/*/README.md; do
  d=$(dirname "$f")
  grep -o '](\([^)#]*\)' "$f" | sed 's/](//' | grep -v '^http' | sort -u | while read -r p; do
    [ -z "$p" ] || [ -e "$d/$p" ] || echo "MISSING in $f: $p"
  done
done

# 2. each lesson has an HTML twin
for m in units/*/lessons/L*.md; do
  [ -e "${m%.md}.html" ] || echo "NO HTML TWIN: $m"
done

# 3. anchors into each background paper exist (GitHub slug rule); units without a paper are only reported
for u in units/*/; do
  [ -f "$u/background-paper.md" ] || { echo "NO BACKGROUND PAPER: $u"; continue; }
  grep '^#' "$u/background-paper.md" | sed 's/^#* //' | tr 'A-Z' 'a-z' | sed 's/[^a-z0-9 _-]//g; s/ /-/g' | sort -u > /tmp/slugs.txt
  grep -o 'background-paper.md#[^)]*' "$u/README.md" | sed 's/.*#//' | sort -u | while read -r a; do
    grep -qx -- "$a" /tmp/slugs.txt || echo "NOANCHOR in $u: $a"
  done
done

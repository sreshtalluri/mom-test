#!/usr/bin/env sh
# Symlink the skills in this repo into ~/.claude/skills so they're available in every project.
# Usage: ./install.sh            install / refresh
#        ./install.sh --uninstall
set -e
SRC="$(cd "$(dirname "$0")" && pwd)/skills"
DST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
mkdir -p "$DST"
for d in "$SRC"/*/; do
  name="$(basename "$d")"
  fm="$(sed -n 's/^name:[[:space:]]*//p' "$d/SKILL.md" | head -1)"
  if [ "$fm" != "$name" ]; then
    echo "ERROR: $d/SKILL.md frontmatter name '$fm' != directory '$name'" >&2; exit 1
  fi
  if [ "$1" = "--uninstall" ]; then
    rm -f "$DST/$name" && echo "removed  $name"
  else
    ln -sfn "$d" "$DST/$name" && echo "linked   $name -> $DST/$name"
  fi
done
[ "$1" = "--uninstall" ] || echo "Done. Restart Claude Code, then type /mom-test."

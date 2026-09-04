#!/usr/bin/env sh
# Symlink the skills in this repo into a skill directory so they're available in every
# project. Defaults to Claude Code's ~/.claude/skills, but works for any agent that reads
# skills from a directory of SKILL.md files.
#
# Usage: ./install.sh                    install into ~/.claude/skills
#        ./install.sh --dir <path>       install into a different directory
#        ./install.sh --uninstall        remove from ~/.claude/skills
#        ./install.sh --uninstall --dir <path>
#
# Agents with no skill-directory convention (Codex CLI, Cursor, others) don't need this
# script at all: just clone the repo and let the agent read AGENTS.md, which points it at
# skills/<name>/SKILL.md directly. See README.md.
set -e
SRC="$(cd "$(dirname "$0")" && pwd)/skills"
DST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
ACTION="install"
while [ $# -gt 0 ]; do
  case "$1" in
    --uninstall) ACTION="uninstall" ;;
    --dir) shift; DST="$1" ;;
    *) echo "Unknown argument: $1" >&2; exit 1 ;;
  esac
  shift
done
mkdir -p "$DST"
for d in "$SRC"/*/; do
  name="$(basename "$d")"
  fm="$(sed -n 's/^name:[[:space:]]*//p' "$d/SKILL.md" | head -1)"
  if [ "$fm" != "$name" ]; then
    echo "ERROR: $d/SKILL.md frontmatter name '$fm' != directory '$name'" >&2; exit 1
  fi
  if [ "$ACTION" = "uninstall" ]; then
    rm -f "$DST/$name" && echo "removed  $name"
  else
    ln -sfn "$d" "$DST/$name" && echo "linked   $name -> $DST/$name"
  fi
done
if [ "$ACTION" = "uninstall" ]; then
  :
else
  echo "Done. Installed to $DST."
  echo "Claude Code: restart, then type /mom-test. Other directory-based agents: point them at $DST."
fi

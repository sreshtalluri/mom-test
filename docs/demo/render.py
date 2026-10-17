#!/usr/bin/env python3
"""Render the scripted README walkthrough. Requires Pillow only for regeneration."""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
SCENES = [
    ("01 / Remember", "/mom-test-memory init --example", [
        "discovery/ created with fictional sample data.",
        "4 interviews / 5 assumptions / 2 practice scores", "",
        "A4  One-click deposits                 WEAKENED",
        "A3  Office manager can approve spend   WEAKENED",
        "A1  No-shows cost at least $300/week    SUPPORTED",
    ]),
    ("02 / Prepare", "/mom-test-prep derm office manager, call Thursday", [
        "Riskiest assumption: A4 - one-click deposits.", "",
        "Scary question:",
        '  "Have you ever charged a no-show fee? What happened?"', "",
        "Use earlier interviews to avoid asking what you already know.",
    ]),
    ("03 / Catch a bad question", "/mom-test-next-question live", [
        'F: "We automate deposits. Would that help?"',
        'C: "Oh yeah, that sounds really useful."', "",
        "Signal: compliment (none)",
        "Why: a pitch plus a would-question invites politeness.",
        'Say next: "When did you last try charging for a missed slot?"',
        'Don\'t say: "Would you enable it if it were one click?"',
    ]),
    ("04 / Separate facts from fluff", "/mom-test-debrief [paste notes]", [
        "Fact: [A4-] rung 13",
        '  "We tried a $25 fee. The owner stopped it after complaints."', "",
        "A4 remains WEAKENED. A compliment is not supporting evidence.", "",
        "Review the debrief before recording anything.",
    ]),
    ("05 / Record and check", "/mom-test-memory record", [
        "After review: save the interview and update its evidence links.", "",
        "> /mom-test-gate build one-click deposit charging", "",
        "A4 is WEAKENED; the sample contains contrary fee experience.",
        "VERDICT: RUN 3 CONVERSATIONS FIRST",
        "The next build decision has to face the evidence.",
    ]),
    ("06 / Practice and repeat", "/mom-test-roleplay random healthcare 3", [
        "Interview a simulated office manager, then request a debrief.",
        "Illustrative score: 48/75 / lowest: pitching, urgency", "",
        "> /mom-test-league",
        "Track your scores and pick the next practice challenge.", "",
        "Practice improves the interviewer. It never becomes evidence.",
    ]),
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--font", type=Path, help="Path to a monospace TTF/TTC font")
    args = parser.parse_args()
    candidates = [args.font, Path("/System/Library/Fonts/Menlo.ttc"),
                  Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")]
    font_path = next((p for p in candidates if p and p.exists()), None)
    if font_path is None:
        parser.error("supply --font with a monospace TTF/TTC font")
    font = ImageFont.truetype(str(font_path), 21)
    small = ImageFont.truetype(str(font_path), 17)
    heading = ImageFont.truetype(str(font_path), 27)
    frames = []
    for title, command, lines in SCENES:
        canvas = Image.new("RGB", (1120, 490), "#0c1320")
        draw = ImageDraw.Draw(canvas)
        draw.rounded_rectangle((16, 16, 1104, 474), radius=14, fill="#141f30")
        for x, color in [(42, "#fb7185"), (66, "#fbbf24"), (90, "#34d399")]:
            draw.ellipse((x, 34, x + 11, 45), fill=color)
        draw.text((122, 30), "mom-test / founder conversation skills", font=small, fill="#a5b7d0")
        draw.text((38, 78), title, font=heading, fill="#f1f5f9")
        draw.text((38, 132), "> " + command, font=font, fill="#5eead4")
        for i, line in enumerate(lines):
            if draw.textlength(line, font=font) > 1040:
                raise ValueError(f"Line too wide: {line}")
            draw.text((38, 185 + i * 31), line, font=font, fill="#dbe5f2")
        draw.text((38, 439), "SCRIPTED WALKTHROUGH / FICTIONAL DATA / NOT A FOUNDER TRIAL", font=small, fill="#a5b7d0")
        frames.append(canvas)
    frames[0].save(ROOT / "walkthrough.png")
    frames[0].save(ROOT / "walkthrough.gif", save_all=True, append_images=frames[1:],
                   duration=10000, loop=0, optimize=True)
    print("Wrote docs/demo/walkthrough.gif and walkthrough.png")


if __name__ == "__main__":
    main()

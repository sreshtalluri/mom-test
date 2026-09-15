# README walkthrough

`walkthrough.gif` is a 60-second, six-screen scripted illustration of the skills
loop. It uses fictional sample data and illustrative responses. It is not a captured
agent session, a benchmark, or a founder acceptance trial. The README also includes
the walkthrough as readable text; `walkthrough.png` is a still preview.

To regenerate (Pillow is a development dependency for this script only):

```sh
python3 -m venv /tmp/mom-test-demo-venv
/tmp/mom-test-demo-venv/bin/pip install Pillow
/tmp/mom-test-demo-venv/bin/python docs/demo/render.py
# On systems without Menlo or DejaVu Sans Mono, supply --font /path/to/mono.ttf.
```

Edit the scenes in `render.py`. Keep invented quotes and scores clearly marked as
illustrative and keep claims consistent with the shipped skills. The generator
checks line widths to catch clipped text.

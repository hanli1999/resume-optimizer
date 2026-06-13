# Contributing

Thanks for your interest.

## How to Contribute

1. Fork the repo
2. Create a branch: `git checkout -b your-feature`
3. Make changes. Add templates, improve the analysis framework, fix bugs
4. Run `python -m py_compile scripts/synthesize.py` to verify
5. Commit and push
6. Open a PR

## What We're Looking For

- **New resume templates** — HTML/CSS in `templates/`. Follow existing naming: `resume-two-page-X.html` / `resume-one-page-X.html`
- **Better prompt engineering** — the AI parse prompt in SKILL.md is the most impactful thing you can improve
- **Truth audit improvements** — better detection of fabricated information
- **Platform support** — make this work on macOS/Linux, not just Windows

## Code Style

- Chinese comments for AI-facing documentation
- MIT license for all new files
- Templates must use system fonts, no external dependencies

## Questions?

Open an issue. We'll respond within 48 hours.

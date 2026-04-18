# Home PC / server setup — 6Phene infrastructure reference

Static **Infrastructure Master Reference** for 6Phene Inc.: homelab hardware (Proxmox, dual RTX 4070), dev server, desktop phases, TrueNAS, 100G-ready network, security, grow automation, CAD pricing (Toronto), and setup/maintenance guides.

**Live site (GitHub Pages):** https://kissmeh02.github.io/home-pc-server-setup/

**Coding standards:** [docs/CODING_STANDARDS.md](docs/CODING_STANDARDS.md) (includes Notion link placeholder for your team wiki).

## Repository layout

```
.
├── .github/
│   └── workflows/
│       ├── ci.yml          # Merge + verify HTML on push/PR
│       └── pages.yml       # Deploy site/ to GitHub Pages
├── docs/
│   └── CODING_STANDARDS.md
├── scripts/
│   └── merge_site.py       # Concatenate src/parts → site/index.html
├── site/
│   └── index.html          # Built output (also produced in CI)
├── src/
│   ├── parts/              # Ordered HTML fragments (part01…part03)
│   └── README.md
├── tests/
│   └── test_merge_site.py
├── LICENSE
└── README.md
```

## Build

```bash
python scripts/merge_site.py
```

Open `site/index.html` locally or use the GitHub Pages URL above.

## Contributing

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) and [docs/CODING_STANDARDS.md](docs/CODING_STANDARDS.md). After editing fragments under `src/parts/`, run the merge script and commit `site/index.html` (CI regenerates on deploy as well). Push updates to `origin main` when changes are ready.

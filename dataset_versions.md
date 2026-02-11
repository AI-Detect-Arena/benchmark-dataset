# Dataset Versions

This document tracks all versions of the AI Detector Arena benchmark dataset.

## Version History

| Version | Release Date | Total Images | AI Images | Real Images | Generators | Changes |
|---------|--------------|--------------|-----------|-------------|------------|---------|
| **0.1** | Feb 2026 | 2,038 | 1,018 | 1,020 | 17 | Initial release |

---

## Version 0.1 (Current)

**Release Date:** February 2026

### Statistics
- **Total Images:** 2,038
- **AI-Generated:** 1,018 (50%)
- **Real Photos:** 1,020 (50%)
- **AI Generators:** 17
- **Categories:** 6

### AI Generators Included

| Generator | Vendor | Count |
|-----------|--------|-------|
| Flux Pro v1.1 | Black Forest Labs | 60 |
| Flux 2 Flex | Black Forest Labs | 60 |
| Flux Schnell | Black Forest Labs | 60 |
| GPT Image 1.5 | OpenAI | 60 |
| Gemini 3 Pro | Google | 60 |
| Grok Aurora | xAI | 60 |
| Stable Diffusion 3.5 Large | Stability AI | 60 |
| Ideogram v3 | Ideogram | 60 |
| Leonardo Phoenix | Leonardo AI | 60 |
| Recraft v3 | Recraft | 60 |
| Hunyuan v3 | Tencent | 60 |
| Seedream v3 | ByteDance | 60 |
| Seedream v4 | ByteDance | 60 |
| Qwen 2512 | Alibaba | 60 |
| GLM Image | Zhipu AI | 60 |
| Wan v2.6 | Alibaba | 60 |
| Z Image | - | 59 |

### Content Categories

| Category | AI Count | Real Count | Total |
|----------|----------|------------|-------|
| Portrait | 170 | 170 | 340 |
| Landscape | 168 | 170 | 338 |
| Art | 170 | 170 | 340 |
| Food | 170 | 170 | 340 |
| Animal | 170 | 170 | 340 |
| Product | 170 | 170 | 340 |

### Real Image Sources
- Unsplash Lite Dataset

### Distortions
- None applied (original quality)

### Integrity

| File | Size | SHA256 |
|------|------|--------|
| `benchmark-v0.1.zip` | 1.39 GiB | `1e62844bba714c2e190792844d4169fa3119fac3c2c143dad1eb8062e20b67e4` |

**Download:** [CDN Link](https://aidetectarena-benchmark.nyc3.cdn.digitaloceanspaces.com/datasets-archive/benchmark-v0.1.zip)

### Notes
- Initial balanced dataset release
- Focus on modern AI generators (late 2025 - early 2026)
- High-quality images without compression artifacts

---

## Planned Future Versions

### Version 0.2 (Planned)
- JPEG compression variants (Q50, Q70, Q90)
- Additional emerging generators
- Possible category expansion

### Version 0.3 (Planned)
- Resize/downscale variants
- Social media compression simulation
- More diverse real image sources

---

## Upgrade Policy

When a new dataset version is released:

1. **Existing results preserved** — Old version results remain valid for that version
2. **Re-evaluation required** — Detectors should be re-tested on new version
3. **Version displayed** — All rankings show dataset version used
4. **No mixing** — Results from different versions are not combined

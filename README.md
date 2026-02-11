# AI Detector Arena Benchmark

A standardized benchmark for evaluating AI-generated image detection tools.

[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Dataset Version](https://img.shields.io/badge/Dataset-v0.1-green.svg)](dataset_versions.md)

**Homepage:** [aidetectarena.com](https://aidetectarena.com)

## Live Leaderboard

**See how AI detectors perform on this benchmark:**

[![Live Leaderboard](https://img.shields.io/badge/Live-Leaderboard-blue?style=for-the-badge)](https://aidetectarena.com)

The leaderboard is updated in real-time as new detectors are evaluated against this dataset.

## Overview

AI Detector Arena provides an objective, reproducible benchmark for comparing AI image detectors. We test detectors against a curated dataset of AI-generated and real images, measuring accuracy across different generators and content categories.

## Key Features

- **Balanced Dataset** — Equal split between AI-generated and real images
- **Diverse Generators** — 17 state-of-the-art AI image generators
- **Multiple Categories** — Portrait, Landscape, Art, Food, Animal, Product
- **Versioned** — Dataset versions ensure reproducible results
- **Transparent** — Open methodology and evaluation criteria

## Current Dataset (v0.1)

| Metric | Value |
|--------|-------|
| Total Images | 2,038 |
| AI-Generated | 1,018 |
| Real Photos | 1,020 |
| AI Generators | 17 |
| Categories | 6 |

See [dataset_versions.md](dataset_versions.md) for full version history.

## Repository Structure

```
benchmark-dataset/
├── README.md                   # This file
├── LICENSE                     # MIT (code) + CC-BY-4.0 (data)
├── dataset_card.md             # HuggingFace-style dataset card
├── methodology.md              # Evaluation methodology
├── dataset_versions.md         # Version history
├── dataset_metadata/
│   ├── images_metadata.csv     # Full image metadata
│   └── schema.md               # Metadata field definitions
├── samples/                    # Sample images (subset)
│   ├── ai/
│   └── real/
└── evaluation/
    ├── evaluate.py             # Benchmark evaluation script
    └── requirements.txt        # Python dependencies
```

## Quick Start

### Evaluate Your Detector

1. Run your detector on the dataset images
2. Create a predictions CSV:
   ```csv
   image_id,prediction,confidence
   ai_flux_portrait_001,ai,0.95
   real_animal_unsplash_042,real,0.87
   ```
3. Run evaluation:
   ```bash
   cd evaluation
   python evaluate.py --predictions your_predictions.csv --metadata ../dataset_metadata/images_metadata.csv
   ```

## Links

| Resource | URL |
|----------|-----|
| **Homepage** | [aidetectarena.com](https://aidetectarena.com) |
| **Leaderboard** | [aidetectarena.com](https://aidetectarena.com) |
| **Dataset Details** | [aidetectarena.com/benchmark-dataset](https://aidetectarena.com/benchmark-dataset) |
| **Methodology** | [aidetectarena.com/methodology](https://aidetectarena.com/methodology) |

## Citation

If you use this benchmark in your research or evaluation, please cite:

```bibtex
@misc{aidetectarena2026,
  title   = {AI Detector Arena Benchmark Dataset},
  author  = {AI Detector Arena},
  year    = {2026},
  url     = {https://aidetectarena.com/benchmark-dataset},
  note    = {Dataset Version 0.1}
}
```

**Plain text:**
> AI Detector Arena. (2026). AI Detector Arena Benchmark Dataset (Version 0.1). https://aidetectarena.com/benchmark-dataset

## License

| Component | License |
|-----------|---------|
| Code & Scripts | [MIT License](LICENSE) |
| Metadata & Documentation | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) |
| AI Images | Generated via official APIs for research |
| Real Photos | [Unsplash License](https://unsplash.com/license) |

## Contributing

We welcome contributions:
- Report issues with the benchmark
- Suggest new detectors to evaluate
- Propose methodology improvements

Open an issue or pull request to get started.

---

Made with care by the [AI Detector Arena](https://aidetectarena.com) team.

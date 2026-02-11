# AI Detector Arena Benchmark

A standardized benchmark for evaluating AI-generated image detection tools.

## Overview

AI Detector Arena provides an objective, reproducible benchmark for comparing AI image detectors. We test detectors against a curated dataset of AI-generated and real images, measuring accuracy across different generators and content categories.

**Website:** [aidetectorarena.com](https://aidetectorarena.com)

## Key Features

- **Balanced Dataset** — Equal split between AI-generated and real images
- **Diverse Generators** — 17 state-of-the-art AI image generators
- **Multiple Categories** — Portrait, Landscape, Art, Food, Animal, Product
- **Versioned** — Dataset versions ensure reproducible results
- **Transparent** — Open methodology and evaluation criteria

## Current Dataset (v0.1)

| Metric | Value |
|--------|-------|
| Total Images | ~2,050 |
| AI-Generated | ~1,018 |
| Real Photos | ~1,032 |
| AI Generators | 17 |
| Categories | 6 |

See [dataset_versions.md](dataset_versions.md) for full version history.

## Repository Structure

```
benchmark-dataset/
├── README.md                 # This file
├── methodology.md            # Evaluation methodology
├── dataset_versions.md       # Version history
├── dataset_metadata/
│   └── images_metadata.csv   # Full image metadata
├── samples/                  # Sample images (subset)
│   ├── ai/
│   └── real/
└── evaluation/               # Benchmark scripts
    └── evaluate.py
```

## Links

- **Leaderboard:** [aidetectorarena.com](https://aidetectorarena.com)
- **Dataset Details:** [aidetectorarena.com/benchmark-dataset](https://aidetectorarena.com/benchmark-dataset)
- **Methodology:** [aidetectorarena.com/methodology](https://aidetectorarena.com/methodology)

## Citation

If you use this benchmark in your research, please cite:

```bibtex
@misc{aidetectorarena2025,
  title={AI Detector Arena Benchmark},
  author={AI Detector Arena},
  year={2025},
  url={https://aidetectorarena.com},
  note={Dataset Version 0.1}
}
```

## License

- **Metadata & Code:** MIT License
- **AI Images:** Generated via official APIs for research purposes
- **Real Images:** [Unsplash License](https://unsplash.com/license)

## Contributing

We welcome contributions:
- Report issues with the benchmark
- Suggest new detectors to evaluate
- Propose methodology improvements

Open an issue or pull request to get started.

#!/usr/bin/env python3
"""
Example evaluation script for AI Detector Arena benchmark.

Usage:
    python evaluate.py --predictions predictions.csv --metadata ../dataset_metadata/images_metadata.csv

predictions.csv format:
    image_id,prediction,confidence
    ai_animal_flux_2_flex_animal_01.png,ai,0.95
    real_animal_photo_001.jpg,real,0.87
"""

import argparse
import csv
from collections import defaultdict


def load_predictions(filepath):
    """Load predictions from CSV."""
    predictions = {}
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            predictions[row['image_id']] = {
                'prediction': row['prediction'].lower(),
                'confidence': float(row.get('confidence', 0.5))
            }
    return predictions


def load_ground_truth(filepath):
    """Load ground truth from metadata CSV."""
    ground_truth = {}
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            image_id = row['id']
            is_ai = row['is_ai'].lower() == 'true'
            ground_truth[image_id] = {
                'is_ai': is_ai,
                'generator': row.get('generator', ''),
                'category': row.get('category', '')
            }
    return ground_truth


def calculate_metrics(predictions, ground_truth):
    """Calculate evaluation metrics."""
    tp = fp = tn = fn = 0

    category_stats = defaultdict(lambda: {'tp': 0, 'fp': 0, 'tn': 0, 'fn': 0})
    generator_stats = defaultdict(lambda: {'correct': 0, 'total': 0})

    for image_id, gt in ground_truth.items():
        if image_id not in predictions:
            continue

        pred = predictions[image_id]['prediction']
        actual_is_ai = gt['is_ai']
        predicted_is_ai = pred == 'ai'

        category = gt['category']
        generator = gt['generator']

        if actual_is_ai and predicted_is_ai:
            tp += 1
            category_stats[category]['tp'] += 1
            generator_stats[generator]['correct'] += 1
        elif actual_is_ai and not predicted_is_ai:
            fn += 1
            category_stats[category]['fn'] += 1
        elif not actual_is_ai and predicted_is_ai:
            fp += 1
            category_stats[category]['fp'] += 1
        else:  # not actual_is_ai and not predicted_is_ai
            tn += 1
            category_stats[category]['tn'] += 1

        if generator:
            generator_stats[generator]['total'] += 1

    total = tp + tn + fp + fn
    accuracy = (tp + tn) / total if total > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    return {
        'total': total,
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'tp': tp,
        'tn': tn,
        'fp': fp,
        'fn': fn,
        'by_category': dict(category_stats),
        'by_generator': dict(generator_stats)
    }


def print_report(metrics):
    """Print evaluation report."""
    print("=" * 60)
    print("AI DETECTOR ARENA BENCHMARK EVALUATION")
    print("=" * 60)
    print()

    print("OVERALL METRICS")
    print("-" * 40)
    print(f"Total images evaluated: {metrics['total']}")
    print(f"Accuracy:  {metrics['accuracy']:.2%}")
    print(f"Precision: {metrics['precision']:.2%}")
    print(f"Recall:    {metrics['recall']:.2%}")
    print(f"F1 Score:  {metrics['f1']:.2%}")
    print()

    print("CONFUSION MATRIX")
    print("-" * 40)
    print(f"True Positives (AI→AI):   {metrics['tp']}")
    print(f"True Negatives (Real→Real): {metrics['tn']}")
    print(f"False Positives (Real→AI): {metrics['fp']}")
    print(f"False Negatives (AI→Real): {metrics['fn']}")
    print()

    print("BY CATEGORY")
    print("-" * 40)
    for cat, stats in metrics['by_category'].items():
        cat_total = stats['tp'] + stats['tn'] + stats['fp'] + stats['fn']
        cat_acc = (stats['tp'] + stats['tn']) / cat_total if cat_total > 0 else 0
        print(f"  {cat}: {cat_acc:.2%} ({cat_total} images)")
    print()

    print("BY GENERATOR (AI images only)")
    print("-" * 40)
    for gen, stats in metrics['by_generator'].items():
        if not gen or stats['total'] == 0:
            continue
        gen_acc = stats['correct'] / stats['total']
        print(f"  {gen}: {gen_acc:.2%} detected ({stats['correct']}/{stats['total']})")
    print()


def main():
    parser = argparse.ArgumentParser(description='Evaluate AI detector predictions')
    parser.add_argument('--predictions', required=True, help='Path to predictions CSV')
    parser.add_argument('--metadata', required=True, help='Path to ground truth metadata CSV')
    args = parser.parse_args()

    print("Loading predictions...")
    predictions = load_predictions(args.predictions)
    print(f"  Loaded {len(predictions)} predictions")

    print("Loading ground truth...")
    ground_truth = load_ground_truth(args.metadata)
    print(f"  Loaded {len(ground_truth)} ground truth labels")

    print("Calculating metrics...")
    metrics = calculate_metrics(predictions, ground_truth)

    print_report(metrics)


if __name__ == "__main__":
    main()

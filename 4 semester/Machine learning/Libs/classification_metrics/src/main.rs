mod metrics;

use metrics::calculate_accuracy;
use metrics::calculate_precision;
use metrics::calculate_recall;
use metrics::calculate_f1_score;

fn main() {
    let true_positives = 10;
    let false_positives = 2;
    let true_negatives = 5;
    let false_negatives = 3;

    let accuracy = calculate_accuracy(true_positives, false_positives, true_negatives, false_negatives);
    println!("Accuracy: {}", accuracy);

    let precision = calculate_precision(true_positives, false_positives);
    println!("Precision: {}", precision);

    let recall = calculate_recall(true_positives, false_negatives);
    println!("Recall: {}", recall);

    let f1_score = calculate_f1_score(precision, recall);
    println!("F1 Score: {}", f1_score);
}

use std::collections::{HashMap, HashSet};

use crate::dataset::Dataset;

fn calc_gini(labels: &[String]) -> f64 {
    let n = labels.len() as f64;
    let mut counts = HashMap::new();
    
    for label in labels.iter() {
        *counts.entry(label).or_insert(0) += 1;
    }

    let impurity = counts.values().fold(0.0, |acc, &count| {
        let p = count as f64 / n;
        acc - p * p
    });

    impurity
}

fn split_data(data: &Dataset, feature: &str, value: f64) -> (Dataset, Dataset) {
    let mut true_objects = vec![];
    let mut false_objects = vec![];
    let mut true_labels = vec![];
    let mut false_labels = vec![];

    let feature_idx = data.features.iter().position(|f| f == feature).unwrap();
    for (obj, label) in data.objects.iter().zip(&data.labels) {
        if obj[feature_idx] >= value {
            true_objects.push(obj.clone());
            true_labels.push(label.clone());
        } else {
            false_objects.push(obj.clone());
            false_labels.push(label.clone());
        }
    }
    
    let true_data = Dataset::new(data.features.clone(), data.labels.clone(), true_objects, data.classes.clone());
    let false_data = Dataset::new(data.features.clone(), data.labels.clone(), false_objects, data.classes.clone());

    (true_data, false_data)
}

pub fn calc_feature_impurity(data: &Dataset, feature: &str) -> f64 {
    let mut impurity = 0.0;
    let feature_idx = data.features.iter().position(|f| f == feature).unwrap();
    let feature_values: HashSet<f64> = data.objects.iter().map(|obj| obj[feature_idx]).collect();

    for value in feature_values {
        let (true_data, false_data) = split_data(data, feature, value);
        let n = true_data.objects.len() + false_data.objects.len();
        let true_impurity = calc_gini(&true_data.labels) * (true_data.objects.len() / n) as f64;
        let false_impurity = calc_gini(&false_data.labels) * (false_data.objects.len() / n) as f64;

        impurity += true_impurity + false_impurity;
    }

    impurity
}

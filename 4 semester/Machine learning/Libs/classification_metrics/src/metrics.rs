pub fn calculate_accuracy(tp: i32, fp: i32, tn: i32, fn_: i32) -> f32 {
    let total = tp + fp + tn + fn_;
    let correct = tp + tn;
    correct as f32 / total as f32
}

pub fn calculate_precision(tp: i32, fp: i32) -> f32 {
    tp as f32 / (tp + fp) as f32
}

pub fn calculate_recall(tp: i32, fn_: i32) -> f32 {
    tp as f32 / (tp + fn_) as f32
}

pub fn calculate_f1_score(precision: f32, recall: f32) -> f32 {
    2.0 * (precision * recall) / (precision + recall)
}

pub fn mean_absolute_error(y_true: &Vec<f64>, y_pred: &Vec<f64>) -> f64 {
    let mut sum_error = 0.0;

    for i in 0..y_true.len() {
        sum_error += (y_true[i] - y_pred[i]).abs();
    }

    sum_error / y_true.len() as f64
}

pub fn mean_squared_error(y_true: &Vec<f64>, y_pred: &Vec<f64>) -> f64 {
    let mut mse = 0.0;

    for i in 0..y_true.len() {
        mse += (y_true[i] - y_pred[i]).powi(2);
    }

    mse / y_true.len() as f64
}

pub fn r2_score(y_true: &Vec<f64>, y_pred: &Vec<f64>) -> f64 {
    let mean_y_true: f64 = y_true.iter().sum::<f64>() / y_true.len() as f64;
    let mut ss_tot = 0.0;
    let mut ss_res = 0.0;

    for i in 0..y_true.len() {
        ss_tot += (y_true[i] - mean_y_true).powi(2);
        ss_res += (y_true[i] - y_pred[i]).powi(2);
    }

    1.0 - ss_res / ss_tot
}

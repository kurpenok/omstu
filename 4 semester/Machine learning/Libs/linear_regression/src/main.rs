mod linear_regression;
mod metrics;

use linear_regression::LinearRegression;
use metrics::mean_absolute_error;
use metrics::mean_squared_error;
use metrics::r2_score;

fn main() {
    let x = vec![
        vec![1.0, 2.0],
        vec![2.0, 3.0],
        vec![3.0, 4.0],
        vec![4.0, 5.0]
    ];
    let y = vec![3.0, 5.0, 7.0, 9.0];

    let x_pred = vec![
        vec![5.0, 6.0],
        vec![6.0, 7.0]
    ];

    let mut lr = LinearRegression::new(0.01, 1000);
    lr.fit(&x, &y);
    let y_pred = lr.predict(&x_pred);

    println!("Weights: {:?}", lr.weights);
    println!("Predictions: {:?}", y_pred);

    let mae = mean_absolute_error(&y, &lr.predict(&x));
    println!("MSE: {}", mae);

    let mse = mean_squared_error(&y, &lr.predict(&x));
    println!("MSE: {}", mse);

    let r2 = r2_score(&y, &lr.predict(&x));
    println!("R2 score: {}", r2);
}

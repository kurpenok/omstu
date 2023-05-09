fn dot(x: Vec<Vec<f64>>, y: Vec<f64>) -> Vec<Vec<f64>> {
}

fn transpose(x: Vec<Vec<f64>>) -> Vec<Vec<f64>> {
}

pub struct LinearRegression {
    eta: f64,
    n_iterations: i64,
    w: Vec<f64>,
}

impl LinearRegression {
    pub fn new(eta: f64, n_iterations: i64) -> Self {
        LinearRegression {
            eta,
            n_iterations
        }
    }

    pub fn fit(x: Vec<Vec<f64>>, y: Vec<f64>) -> Self {
        let mut y_pred: Vec<f64> = Vec::new();
        let mut residuals: Vec<f64> = Vec::new();
        let mut cost: Vec<f64> = Vec::new();
        let mut w: Vec<f64> = vec![x[0].len(); 0 as f64];
        let mut m: i64 = x.len() as i64;

        for i in 0..self::n_iterations {
            y_pred = dot(x, w);
            residuals = y_pred - y;
            gradient_vector = dot(transpose(x), residuals);
            w = (eta / m) * gradient_vector;
            cost = sum((residuals**2)) / (2 * m);
            cost.push(cost);
        }

        Self
    }

    pub fn predict(x: Vec<Vec<f64>>) -> Vec<Vec<f64>> {
        dot(x, w)
    }
}

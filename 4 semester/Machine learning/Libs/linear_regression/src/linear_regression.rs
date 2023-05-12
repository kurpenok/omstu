fn dot(x: &Vec<Vec<f64>>, y: &Vec<Vec<f64>>) -> Vec<f64> {
    Vec::new()
}

fn transpose(x: &Vec<Vec<f64>>) -> Vec<Vec<f64>> {
}

fn difference(x: &Vec<f64>, y: &Vec<f64>) -> Vec<f64> {
}


pub struct LinearRegression {
    eta: f64,
    n_iterations: i64,
}

impl LinearRegression {
    pub fn new(eta: f64, n_iterations: i64) -> Self {
        LinearRegression {
            eta,
            n_iterations,
        }
    }

    pub fn fit(&self, x: Vec<Vec<f64>>, y: Vec<f64>) -> Self {
        let mut cost: Vec<f64> = Vec::new();
        
        let mut w: Vec<Vec<f64>> = Vec::new();
        for i in 0..x[0].len() {
            let mut line: Vec<f64> = Vec::new();
            for j in 0..1 {
                line.push(0 as f64);
            }
            w.push(line);
        }

        let mut m = x.len();

        for i in 0..self.n_iterations {
            let mut y_pred = dot(&x, &w);
            let mut residuals = difference(&y_pred, &y);
            let mut gradient_vector = dot(&transpose(&x), &residuals);
            w = difference(&w, &(self.eta / m) * &gradient_vector);
            cost = sum((residuals**2)) / (2 * m);
            cost.push(cost);
        }

        *self
    }
}

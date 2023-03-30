pub struct LinearRegression {
    step_size: f64,
    num_iterations: usize,
    pub weights: Vec<f64>,
}

impl LinearRegression {
    pub fn new(step_size: f64, num_iterations: usize) -> LinearRegression {
        LinearRegression {
            step_size,
            num_iterations,
            weights: Vec::new(),
        }
    }

    pub fn fit(&mut self, x: &Vec<Vec<f64>>, y: &Vec<f64>) {
        let n_samples = x.len();
        let n_features = x[0].len();

        // Initialize the weights with zeros
        self.weights = vec![0.0; n_features];

        for _ in 0..self.num_iterations {
            // Calculate the gradients
            let mut gradients = vec![0.0; n_features];
            for i in 0..n_samples {
                let prediction = self.predict_single(&x[i]);
                let error = y[i] - prediction;
                for j in 0..n_features {
                    gradients[j] += error * x[i][j];
                }
            }

            // Update the weights
            for j in 0..n_features {
                self.weights[j] += self.step_size * gradients[j];
            }
        }
    }

    fn predict_single(&self, x: &Vec<f64>) -> f64 {
        let mut result = 0.0;
        for i in 0..x.len() {
            result += self.weights[i] * x[i];
        }
        result
    }

    pub fn predict(&self, x: &Vec<Vec<f64>>) -> Vec<f64> {
        let mut y_pred = vec![0.0; x.len()];
        for i in 0..x.len() {
            y_pred[i] = self.predict_single(&x[i]);
        }
        y_pred
    }
}

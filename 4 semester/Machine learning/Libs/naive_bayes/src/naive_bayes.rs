use std::collections::HashMap;

pub struct GaussianNB {
    priors: HashMap<String, f64>,
    means: HashMap<String, Vec<f64>>,
    variances: HashMap<String, Vec<f64>>,
}

impl GaussianNB {
    pub fn new() -> GaussianNB {
        GaussianNB {
            priors: HashMap::new(),
            means: HashMap::new(),
            variances: HashMap::new(),
        }
    }
    
    pub fn fit(&mut self, X: Vec<Vec<f64>>, y: Vec<String>) {
        let n_samples = X.len();
        let n_features = X[0].len();
        
        // Calculate class priors
        for class in y.iter() {
            *self.priors.entry(class.to_string()).or_insert(0.0) += 1.0;
        }
        for count in self.priors.values_mut() {
            *count /= n_samples as f64;
        }
        
        // Calculate mean and variance for each feature and class
        for (class, idx) in self.priors.keys().zip(0..) {
            let mut features = vec![vec![]; n_features];
            for (i, x) in X.iter().enumerate() {
                if y[i] == *class {
                    for (j, &val) in x.iter().enumerate() {
                        features[j].push(val);
                    }
                }
            }
            let mut means = Vec::new();
            let mut variances = Vec::new();
            for feature in features.iter() {
                let mean = feature.iter().sum::<f64>() / feature.len() as f64;
                means.push(mean);
                let variance = feature.iter().map(|x| (x - mean).powi(2)).sum::<f64>() / (feature.len() - 1) as f64;
                variances.push(variance);
            }
            self.means.insert(class.to_string(), means);
            self.variances.insert(class.to_string(), variances);
        }
    }
    
    pub fn predict(&self, X: Vec<Vec<f64>>) -> Vec<String> {
        let mut y_pred = Vec::new();
        for x in X.iter() {
            let mut max_prob = 0.0;
            let mut max_class = String::new();
            for (class, prior) in self.priors.iter() {
                let mut prob = 1.0;
                for (i, &feature) in x.iter().enumerate() {
                    let mean = self.means.get(class).unwrap()[i];
                    let variance = self.variances.get(class).unwrap()[i];
                    let exponent = -(feature - mean).powi(2) / (2.0 * variance);
                    let coef = 1.0 / (2.0 * std::f64::consts::PI * variance).sqrt();
                    prob *= coef * exponent.exp();
                }
                prob *= prior;
                if prob > max_prob {
                    max_prob = prob;
                    max_class = class.to_string();
                }
            }
            y_pred.push(max_class);
        }
        y_pred
    }
}

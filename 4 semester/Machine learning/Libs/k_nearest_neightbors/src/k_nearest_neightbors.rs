fn euclidean_distance(x1: &[f64], x2: &[f64]) -> f64 {
    let sum_of_squares: f64 = x1
        .iter()
        .zip(x2.iter())
        .map(|(&a, &b)| (a - b) * (a - b))
        .sum();
    sum_of_squares.sqrt()
}

pub struct KNearestNeighbors {
    x_train: Vec<Vec<f64>>,
    y_train: Vec<usize>,
    k: usize,
}

impl KNearestNeighbors {
    pub fn new(k: usize) -> KNearestNeighbors {
        KNearestNeighbors {
            x_train: Vec::new(),
            y_train: Vec::new(),
            k,
        }
    }

    pub fn fit(&mut self, x_train: Vec<Vec<f64>>, y_train: Vec<usize>) {
        self.x_train = x_train;
        self.y_train = y_train;
    }

    pub fn predict(&self, x_test: &[f64]) -> usize {
        let mut distances: Vec<(usize, f64)> = Vec::new();
        for (i, x) in self.x_train.iter().enumerate() {
            let distance = euclidean_distance(x_test, x);
            distances.push((i, distance));
        }
        distances.sort_by(|a, b| a.1.partial_cmp(&b.1).unwrap());
        let k_neighbors = if distances.len() > self.k {
            &distances[0..self.k]
        } else {
            &distances
        };
        let mut votes: [usize; 10] = [0; 10];
        for neighbor in k_neighbors {
            let label = self.y_train[neighbor.0];
            votes[label] += 1;
        }
        let mut max_label = 0;
        let mut max_votes = 0;
        for (i, votes) in votes.iter().enumerate() {
            if *votes > max_votes {
                max_label = i;
                max_votes = *votes;
            }
        }
        max_label
    }
}

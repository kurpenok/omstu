fn inverse(matrix: &Vec<Vec<f64>>) -> Option<Vec<Vec<f64>>> {
    let n = matrix.len();
    let mut augmented = matrix.clone();

    for i in 0..n {
        let mut row = vec![0.0; n];
        row[i] = 1.0;
        augmented.push(row);
    }

    for i in 0..n {
        let divisor = augmented[i][i];
        if divisor == 0.0 {
            return None;
        }

        for j in 0..2 * n {
            augmented[i][j] /= divisor;
        }

        for k in 0..n {
            if k != i {
                let factor = augmented[k][i];
                for j in 0..2 * n {
                    augmented[k][j] -= factor * augmented[i][j];
                }
            }
        }
    }

    let mut inverse = vec![vec![0.0; n]; n];
    for i in 0..n {
        for j in 0..n {
            inverse[i][j] = augmented[i][j + n];
        }
    }

    Some(inverse)
}

pub fn solve(matrix: &Vec<Vec<f64>>, constants: &Vec<f64>) -> Option<Vec<f64>> {
    dbg!(inverse(matrix));

    None
}

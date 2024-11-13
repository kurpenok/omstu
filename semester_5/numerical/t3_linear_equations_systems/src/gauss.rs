pub fn solve(matrix: &mut Vec<Vec<f64>>) -> Vec<f64> {
    let n = matrix.len();

    for i in 0..n {
        let divisor = matrix[i][i];
        for j in i..=n {
            matrix[i][j] /= divisor;
        }

        for k in i + 1..n {
            let factor = matrix[k][i];
            for j in i..=n {
                matrix[k][j] -= factor * matrix[i][j];
            }
        }
    }

    let mut solution = vec![0.0; n];
    for i in (0..n).rev() {
        solution[i] = matrix[i][n];
        for j in i + 1..n {
            solution[i] -= matrix[i][j] * solution[j];
        }
    }

    solution
}

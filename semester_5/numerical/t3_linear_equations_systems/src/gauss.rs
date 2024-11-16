pub fn solve(extended_matrix: Vec<Vec<f64>>) -> Vec<f64> {
    let mut extended_matrix = extended_matrix;

    let n = extended_matrix.len();

    for j in 0..n {
        let mut max_row = j;
        for i in j + 1..n {
            if extended_matrix[max_row][j].abs() < extended_matrix[i][j].abs() {
                max_row = i;
            }
        }

        extended_matrix.swap(j, max_row);

        for i in (j..=n).rev() {
            extended_matrix[j][i] /= extended_matrix[j][j];
        }

        for i in 0..n {
            if i != j {
                for k in (j..=n).rev() {
                    extended_matrix[i][k] -= extended_matrix[j][k] * extended_matrix[i][j];
                }
            }
        }
    }

    let mut solution = vec![0.0; n];
    for i in 0..n {
        solution[i] = extended_matrix[i][n];
    }

    solution
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_gauss() {
        let extended_matrix = vec![
            vec![1.0, 2.0, 0.0, -1.0, 0.0],
            vec![2.0, 1.0, 3.0, 1.0, 3.0],
            vec![1.0, 2.0, 3.0, -1.0, 0.0],
            vec![2.0, 2.0, 5.0, -1.0, 1.0],
        ];

        assert_eq!(solve(extended_matrix), [1.0, 0.0, 0.0, 1.0]);
    }
}

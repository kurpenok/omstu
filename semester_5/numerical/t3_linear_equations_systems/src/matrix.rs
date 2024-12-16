pub type Matrix<T> = Vec<Vec<T>>;

pub fn get_submatrix(matrix: &Matrix<f64>, row_index: usize) -> Matrix<f64> {
    let mut submatrix: Matrix<f64> = Vec::new();

    for i in row_index..matrix.len() {
        let mut row: Vec<f64> = Vec::new();
        for j in row_index..matrix.len() {
            row.push(matrix[i][j]);
        }
        submatrix.push(row);
    }

    submatrix
}

pub fn get_pivot_row_index(matrix: &Matrix<f64>) -> usize {
    let mut pivot = matrix[0][0].abs();
    let mut pivot_row_index = 0;

    for j in 0..matrix.len() {
        if pivot < matrix[0][j].abs() {
            pivot = matrix[0][j].abs();
            pivot_row_index = j;
        }
    }

    pivot_row_index
}

pub fn make_triangle(matrix: &Matrix<f64>) -> Matrix<f64> {
    let mut triangle_matrix: Matrix<f64> = matrix.clone();

    for row_index in 0..triangle_matrix.len() {
        let pivot = row_index + get_pivot_row_index(&get_submatrix(&triangle_matrix, row_index));
        if pivot != row_index {
            triangle_matrix.swap(row_index, pivot);
        }

        let divider = triangle_matrix[row_index][row_index];
        if divider.abs() < 1e-10 {
            return vec![];
        }

        for j in row_index..triangle_matrix.len() {
            triangle_matrix[row_index][j] /= divider;
        }

        for j in row_index + 1..triangle_matrix.len() {
            let factor = triangle_matrix[j][row_index];
            for j in row_index..triangle_matrix.len() {
                triangle_matrix[j][row_index] -= factor * triangle_matrix[row_index][j];
            }
        }
    }

    triangle_matrix
}

pub fn make_identity(triangle_matrix: &Matrix<f64>) -> Matrix<f64> {
    let mut identity_matrix: Matrix<f64> = triangle_matrix.clone();

    for row_index in (0..identity_matrix.len()).rev() {
        for upper_row_index in 0..row_index {
            let factor = identity_matrix[upper_row_index][row_index];

            let last_row_index = identity_matrix[row_index].len() - 1;
            let last_upper_row_index = identity_matrix[upper_row_index].len() - 1;

            identity_matrix[upper_row_index][last_upper_row_index] -=
                factor * identity_matrix[row_index][last_row_index];

            identity_matrix[upper_row_index][row_index] = 0.0;
        }
    }

    identity_matrix
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_get_submatrix() {
        let matrix: Matrix<f64> = vec![
            vec![1., 2., 3., 4.],
            vec![2., 3., 4., 5.],
            vec![3., 4., 5., 6.],
            vec![4., 5., 6., 7.],
        ];
        let submatrix: Matrix<f64> = vec![vec![3., 4., 5.], vec![4., 5., 6.], vec![5., 6., 7.]];

        assert_eq!(get_submatrix(&matrix, 1), submatrix);
    }

    #[test]
    fn test_get_pivot_row_index() {
        let matrix: Matrix<f64> = vec![
            vec![1., 2., 3., 4.],
            vec![2., 3., 4., 5.],
            vec![3., 4., 5., 6.],
            vec![4., 5., 6., 7.],
        ];
        let pivot_row_index = 3;

        assert_eq!(get_pivot_row_index(&matrix), pivot_row_index);
    }

    #[test]
    fn test_make_triangle() {
        let matrix: Matrix<f64> = vec![
            vec![1., 0., 0., 1.],
            vec![0., 0., 1., 2.],
            vec![0., 1., 0., 3.],
        ];
        let triangle_matrix: Matrix<f64> = vec![
            vec![1., 0., 0., 1.],
            vec![0., 1., 0., 3.],
            vec![0., 0., 1., 2.],
        ];

        assert_eq!(make_triangle(&matrix), triangle_matrix);
    }

    #[test]
    fn test_make_identity() {
        let triangle_matrix: Matrix<f64> = vec![
            vec![1., 1.76, -0.32, 1.37],
            vec![0., 1., 0.07, 0.5],
            vec![0., 0., 1., 0.09],
        ];
        let identity_matrix: Matrix<f64> = vec![
            vec![1., 0., 0., 0.529888],
            vec![0., 1., 0., 0.4937],
            vec![0., 0., 1., 0.09],
        ];

        assert_eq!(make_identity(&triangle_matrix), identity_matrix);
    }
}

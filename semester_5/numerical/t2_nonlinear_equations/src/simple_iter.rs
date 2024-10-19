pub fn solve<F>(phi: F, x0: f64, tol: f64, max_iter: usize) -> Option<f64>
where
    F: Fn(f64) -> f64,
{
    let mut x = x0;

    for _ in 0..max_iter {
        let x_new = phi(x);
        if (x_new - x).abs() < tol {
            return Some(x_new);
        }
        x = x_new;
    }

    Some(x)
}

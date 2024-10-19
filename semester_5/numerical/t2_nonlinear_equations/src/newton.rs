pub fn solve<F, G>(f: F, df: G, x0: f64, tol: f64, max_iter: usize) -> Option<f64>
where
    F: Fn(f64) -> f64,
    G: Fn(f64) -> f64,
{
    let mut x = x0;

    for _ in 0..max_iter {
        let f_x = f(x);
        let df_x = df(x);

        if df_x.abs() < 1e-10 {
            println!("[-] Derivative is too small, method cannot continue!");
            return None;
        }

        let x_new = x - f_x / df_x;
        if (x_new - x).abs() < tol {
            return Some(x_new);
        }
        x = x_new;
    }

    Some(x)
}

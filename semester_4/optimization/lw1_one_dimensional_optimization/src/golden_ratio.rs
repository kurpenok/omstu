pub fn golden_ratio_search<F>(f: F, a: f64, b: f64, eps: f64) -> (f64, f64)
where
    F: Fn(f64) -> f64,
{
    let mut a = a;
    let mut b = b;

    let tau = 0.618;

    let mut x_1 = b - (b - a) * tau;
    let mut x_2 = a + (b - a) * tau;

    while (a - b).abs() > eps {
        if f(x_1) < f(x_2) {
            b = x_2;
        } else {
            a = x_1;
        }

        x_1 = b - (b - a) * tau;
        x_2 = a + (b - a) * tau;
    }

    ((a + b) / 2.0, f((a + b) / 2.0))
}

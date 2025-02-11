pub fn dichotomy_search<F>(f: F, a: f64, b: f64, eps: f64) -> (f64, f64)
where
    F: Fn(f64) -> f64,
{
    let mut a = a;
    let mut b = b;

    while (a - b).abs() > 2.0 * eps {
        let x = (a + b) / 2.0;
        let x_1 = x - (eps / 2.0);
        let x_2 = x + (eps / 2.0);

        if f(x_1) > f(x_2) {
            a = x_1;
        } else {
            b = x_2;
        }
    }

    ((a + b) / 2.0, f((a + b) / 2.0))
}

pub fn solve<F>(f: F, a: f64, b: f64, tol: f64, max_iter: usize) -> Option<f64>
where
    F: Fn(f64) -> f64,
{
    if f(a) * f(b) >= 0.0 {
        println!("[-] Function must have different signs at ends of interval!");
        return None;
    }

    let mut a = a;
    let mut b = b;
    let mut iter = 0;

    while (b - a).abs() > tol && iter < max_iter {
        let midpoint = (a + b) / 2.0;
        let f_mid = f(midpoint);

        if f_mid == 0.0 {
            return Some(midpoint);
        } else if f(a) * f_mid < 0.0 {
            b = midpoint;
        } else {
            a = midpoint;
        }

        iter += 1;
    }

    Some((a + b) / 2.0)
}

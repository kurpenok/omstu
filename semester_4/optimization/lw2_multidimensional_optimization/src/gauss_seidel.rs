fn optimize<F>(f: F, i: usize, x: [f64; 2], eps: f64) -> f64
where
    F: Fn([f64; 2]) -> f64,
{
    let mut x = x;
    let mut x_left = x;
    let mut x_right = x;

    x_left[i] -= eps;
    x_right[i] += eps;

    while !(f(x_left) > f(x) && f(x) < f(x_right)) {
        if f(x_left) < f(x) && f(x) < f(x_right) {
            x_right = x;
            x = x_left;
            x_left[i] -= eps;
        } else if f(x_left) > f(x) && f(x) > f(x_right) {
            x_left = x;
            x = x_right;
            x_right[i] += eps;
        }
    }

    x[i]
}

pub fn gauss_seidel_search<F>(f: F, x: [f64; 2], eps: f64) -> ([f64; 2], f64)
where
    F: Fn([f64; 2]) -> f64,
{
    let mut x = x;

    for i in 0..x.len() {
        x[i] = optimize(&f, i, x, eps);
    }

    (x, f(x))
}

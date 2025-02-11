pub fn fibonacci(n: usize) -> f64 {
    let mut numbers = [0, 1, 1];
    for _ in 2..n {
        numbers[0] = numbers[1];
        numbers[1] = numbers[2];
        numbers[2] = numbers[0] + numbers[1];
    }
    numbers[2] as f64
}

pub fn fibonacci_search<F>(f: F, a: f64, b: f64, eps: f64) -> (f64, f64)
where
    F: Fn(f64) -> f64,
{
    let mut a = a;
    let mut b = b;

    let mut n = 0;
    while fibonacci(n) < (b - a) / eps {
        n += 1;
    }

    let mut x_1 = a + (fibonacci(n - 2) / fibonacci(n)) * (b - a);
    let mut x_2 = a + (fibonacci(n - 1) / fibonacci(n)) * (b - a);

    let mut f_1 = f(x_1);
    let mut f_2 = f(x_2);

    for i in 2..n {
        if f_1 > f_2 {
            a = x_1;
            x_1 = x_2;
            f_1 = f_2;
            x_2 = a + (fibonacci(n - i + 1) / fibonacci(n - i + 2)) * (b - a);
            f_2 = f(x_2);
        } else {
            b = x_2;
            x_2 = x_1;
            f_2 = f_1;
            x_1 = a + (fibonacci(n - i) / fibonacci(n - i + 2)) * (b - a);
            f_1 = f(x_1);
        }
    }

    ((a + b) / 2.0, f((a + b) / 2.0))
}

mod dichotomy;
mod fibonacci;
mod golden_ratio;

use dichotomy::dichotomy_search;
use fibonacci::fibonacci_search;
use golden_ratio::golden_ratio_search;

fn f(x: f64) -> f64 {
    x.powi(4) / x.ln()
}

fn main() {
    let a: f64 = 1.1;
    let b: f64 = 1.5;
    let eps: f64 = 0.0001;

    let (x, y) = dichotomy_search(f, a, b, eps);
    println!("[+] Dichotomy search: ({:.2}, {:.2})", x, y);

    let (x, y) = fibonacci_search(f, a, b, eps);
    println!("[+] Fibonacci search: ({:.2}, {:.2})", x, y);

    let (x, y) = golden_ratio_search(f, a, b, eps);
    println!("[+] Golden ratio search: ({:.2}, {:.2})", x, y);
}

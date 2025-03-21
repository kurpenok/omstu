mod gauss_seidel;
mod golden_ratio;

use gauss_seidel::gauss_seidel_search;

fn f(x: &[f64]) -> f64 {
    let a: f64 = 3.0;
    let b: f64 = 2.0;
    let c: f64 = 20.0;

    c - ((x[0] - a) * (-x[0] + a).exp()) - ((x[1] - b) * (-x[1] + b).exp())
}

fn main() {
    let eps: f64 = 1e-6;
    let max_iter: usize = 1_000;

    let (x, y) = gauss_seidel_search(f, &vec![0.0, 0.0], eps, max_iter);
    println!("[+] Gauss-Seidel search: ({:.2?}, {:.2})", x, y);
}

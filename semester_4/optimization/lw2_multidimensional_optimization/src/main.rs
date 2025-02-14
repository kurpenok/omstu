mod gauss_seidel;
mod golden_ratio;
mod powell;

use gauss_seidel::gauss_seidel_search;
use powell::powell;

fn f(x: &Vec<f64>) -> f64 {
    let a: f64 = 3.0;
    let b: f64 = 2.0;
    let c: f64 = 20.0;

    let part_1 = (x[0] - a) * (-x[0] + a).exp();
    let part_2 = (x[1] - b) * (-x[1] + b).exp();
    c - part_1 - part_2
}

fn main() {
    let eps: f64 = 0.0001;
    let max_iter: usize = 1000;

    let (x, y) = gauss_seidel_search(f, vec![0.0, 0.0], eps, max_iter);
    println!("[+] Gauss-Seidel search: ({:.2?}, {:.2})", x, y);

    let (x, y) = powell(f, vec![0.0, 0.0], eps, max_iter);
    println!("[+] Powell search: ({:.2?}, {:.2})", x, y);
}

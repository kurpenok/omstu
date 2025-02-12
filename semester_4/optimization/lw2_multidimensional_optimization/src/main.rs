mod gauss_seidel;

use gauss_seidel::gauss_seidel_search;

fn f(x: [f64; 2]) -> f64 {
    let a = 3.0;
    let b = 2.0;
    let c = 20.0;
    c - ((x[0] - a) * (-x[0] + a).exp()) - ((x[1] - b) * (-x[1] + b).exp())
}

fn main() {
    let eps = 0.0001;

    let (x, y) = gauss_seidel_search(f, [0.0, 0.0], eps);
    println!("[+] Gauss-Seidel search: ({:.2?}, {:.2})", x, y);
}

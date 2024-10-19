mod bisection;
mod newton;
mod simple_iter;

fn main() {
    let f = |x: f64| x.powi(3) + 2.0 * x - 4.0;
    let x0 = 0.0;
    let tol = 0.0001;
    let max_iter = 100;

    let separator = "=".repeat(30);

    println!("{}", separator);

    println!("[+] Bisection method");
    let a = 1.0;
    let b = 2.0;
    match bisection::solve(f, a, b, tol, max_iter) {
        Some(root) => println!("[+] Approximate root: {:.4}", root),
        None => println!("[-] Root was not found"),
    }

    println!("{}", separator);

    println!("[+] Newton method");
    let df = |x: f64| 3.0 * x.powi(2) + 2.0;
    match newton::solve(f, df, x0, tol, max_iter) {
        Some(root) => println!("[+] Approximate root: {:.4}", root),
        None => println!("[-] Root was not found"),
    }

    println!("{}", separator);

    println!("[+] Simple iteration method");
    let phi = |x: f64| x - f(x) / 5.0;
    match simple_iter::solve(phi, x0, tol, max_iter) {
        Some(root) => println!("[+] Approximate root: {:.4}", root),
        None => println!("[-] Root was not found"),
    }

    println!("{}", separator);
}

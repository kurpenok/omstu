use crate::{
    cli::console_read,
    modules::{quadratic_sieve_factorization, rho_factorization},
    SEPARATOR,
};

pub fn cli_factorization() {
    let n = console_read("[>] Enter number for factorization: ").parse::<usize>();
    if n.is_err() {
        println!("[-] Incorrect values!");
        println!("{}", SEPARATOR);
        return;
    }

    let n = n.unwrap();

    let d = rho_factorization::factorize(n);
    println!("[+] Factorized by rho-method: [{}, {}]", d, n / d);

    let d = quadratic_sieve_factorization::factorize(n, 3, 5, 7);
    println!("[+] Factorized by quadratic sieve: [{}, {}]", d, n / d);

    println!("{}", SEPARATOR);
}

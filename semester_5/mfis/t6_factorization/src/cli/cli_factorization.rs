use crate::{cli::console_read, modules::rho_factorization, SEPARATOR};

pub fn cli_factorization() {
    let n = console_read("[>] Enter number for factorization: ").parse::<usize>();
    if n.is_err() {
        println!("[-] Incorrect values!");
        println!("{}", SEPARATOR);
        return;
    }

    let n = n.unwrap();

    let rho = rho_factorization::factorize(n);
    println!("[+] Factorized by rho-method: [{}, {}]", rho, n / rho);
    println!("{}", SEPARATOR);
}

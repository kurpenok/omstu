use crate::{
    cli::console_read,
    gcd::{extended_gcd, BezuCoefs},
    SEPARATOR,
};

pub fn cli_gcd() {
    let a = console_read("[>] Enter number a: ").parse::<usize>();
    let b = console_read("[>] Enter number b: ").parse::<usize>();

    if a.is_err() || b.is_err() {
        println!("[-] Incorrect values!");
        return;
    }

    let a = a.unwrap();
    let b = b.unwrap();
    let mut coefs = BezuCoefs::new();

    println!("[+] GCD: {}", extended_gcd(a, b, &mut coefs));
    println!("[+] Bezu coefs: {}, {}", coefs.alpha, coefs.beta);
    println!("{}", SEPARATOR);
}

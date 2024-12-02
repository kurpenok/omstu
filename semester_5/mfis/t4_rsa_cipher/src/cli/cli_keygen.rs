use num_bigint::BigInt;

use bigint::{gcd::gcd, prime::is_prime};

use crate::{cli::console_read, modules::keygen::generate_rsa_keys, SEPARATOR};

pub fn cli_keygen() {
    let p = console_read("[>] Enter number p: ").parse::<usize>();
    let q = console_read("[>] Enter number q: ").parse::<usize>();
    if p.is_err() || q.is_err() {
        println!("[-] Incorrect values!");
        println!("{}", SEPARATOR);
        return;
    }

    let p = BigInt::from(p.unwrap());
    let q = BigInt::from(q.unwrap());
    if !is_prime(&p) || !is_prime(&q) {
        println!("[+] P and Q must be prime!");
        return;
    }

    let e = console_read("[>] Enter number e: ");
    let e = match e.len() {
        0 => None,
        _ => match e.parse::<usize>() {
            Ok(e) => Some(BigInt::from(e)),
            Err(_) => {
                println!("[-] Incorrect values!");
                println!("{}", SEPARATOR);
                return;
            }
        },
    };

    let keys_count = if e.is_none() { 3 } else { 1 };
    for _ in 0..keys_count {
        let rsa_keys = generate_rsa_keys(&p, &q, e.as_ref());

        match rsa_keys {
            Some(rsa_keys) => {
                let e = rsa_keys.e;
                let d = rsa_keys.d;
                let n = rsa_keys.n;

                let phi = (&p - BigInt::from(1)) * (&q - BigInt::from(1));
                if gcd(&e, &phi) != BigInt::from(1) {
                    println!("[-] Failed to generate E!");
                    return;
                }

                println!("[+] Generated keys (e, d, n): {}, {}, {}", e, d, n);
            }
            None => println!("[-] Currect E irreversible!"),
        }
    }
    println!("{}", SEPARATOR);
}

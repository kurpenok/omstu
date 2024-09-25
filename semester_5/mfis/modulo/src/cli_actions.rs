use crate::{
    cli_args::{Gcd, Invert},
    gcd::{extended_gcd, BezuCoefs},
    invert::invert,
};

pub fn cli_gcd(data: &Gcd) {
    let mut coefs = BezuCoefs { alpha: 0, beta: 0 };
    let d = extended_gcd(data.a, data.b, &mut coefs);

    println!("[+] Greater common divisor ({}, {}): {}", data.a, data.b, d);
    println!("[+] Bezu coefficients : {}, {}", coefs.alpha, coefs.beta);
}

pub fn cli_invert(data: &Invert) {
    let result = invert(data.a, data.m);
    if result.is_none() {
        println!("[-] No inverse for given number!");
    } else {
        println!("[+] Inverted number: {}", result.unwrap());
    }
}

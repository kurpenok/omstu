use crate::{
    cli_args::{Gcd, Invert, Solve},
    comparison::solve,
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
    let inverted_a = invert(data.a, data.m);
    if inverted_a.is_none() {
        println!("[-] No inverse for given number!");
    } else {
        println!("[+] Inverted number: {}", inverted_a.unwrap());
    }
}

pub fn cli_solve(data: &Solve) {
    let solutions = solve(data.a, data.b, data.c, data.d, data.m);
    if solutions.is_none() {
        println!("[-] Comparison has no solutions!");
    } else {
        println!("[+] Solutions: {:?}", solutions.unwrap());
    }
}

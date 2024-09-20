use crate::{cli_args::Invert, invert::invert};

pub fn cli_invert(data: &Invert) {
    let result = invert(data.a, data.m);
    if result.is_none() {
        println!("[-] No inverse for given number!");
    } else {
        println!("[+] Inverted number: {}", result.unwrap());
    }
}

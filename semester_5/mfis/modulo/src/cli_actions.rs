use crate::{cli_args::Invert, invert::invert};

pub fn cli_invert(data: &Invert) {
    let a = data.a.parse::<i32>().unwrap();
    let m = data.m.parse::<i32>().unwrap();

    let result = invert(a, m);
    if result.is_none() {
        println!("[-] No inverse for given number!");
    } else {
        println!("[+] Inverted number: {}", result.unwrap());
    }
}

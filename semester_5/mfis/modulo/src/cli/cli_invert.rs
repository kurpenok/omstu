use crate::{cli::console_read, modules::invert::invert, SEPARATOR};

pub fn cli_invert() {
    let a = console_read("[>] Enter number: ").parse::<usize>();
    let m = console_read("[>] Enter modulo: ").parse::<usize>();

    if a.is_err() || m.is_err() {
        println!("[-] Incorrect values!");
        return;
    }

    match invert(a.unwrap(), m.unwrap()) {
        Some(inverted_a) => println!("[+] Inverted number: {}", inverted_a),
        None => println!("[-] No inverse for given number!"),
    }
    println!("{}", SEPARATOR);
}

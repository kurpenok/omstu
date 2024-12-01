use crate::{
    cli::console_read,
    modules::{inverse::get_inverse, ops::mod_add},
    SEPARATOR,
};

pub fn cli_invert() {
    let a = console_read("[>] Enter number: ").parse::<i32>();
    let m = console_read("[>] Enter modulo: ").parse::<usize>();

    if a.is_err() || m.is_err() {
        println!("[-] Incorrect values!");
        println!("{}", SEPARATOR);
        return;
    }

    let m = m.unwrap();
    let a = mod_add(0, a.unwrap(), m);

    match get_inverse(a, m) {
        Some(inverted_a) => println!("[+] Inverse number: {}", inverted_a),
        None => println!("[-] No inverse for given number!"),
    }
    println!("{}", SEPARATOR);
}

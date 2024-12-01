use modulo::ops::mod_add;

use crate::{cli::console_read, modules::encryptor::encrypt, EN_ABC, RU_ABC, SEPARATOR};

pub fn cli_encrypt() {
    let abc = console_read("[>] Enter abc (en/ru): ");
    let text = console_read("[>] Enter text for encryption: ");
    let a = console_read("[>] Enter number a: ").parse::<i32>();
    let b = console_read("[>] Enter number b: ").parse::<i32>();

    if (abc.len() == 0 && text.len() != 0) || a.is_err() || b.is_err() {
        println!("[-] Incorrect values!");
        println!("{}", SEPARATOR);
        return;
    }

    let abc = match abc.as_str() {
        "en" => EN_ABC.chars().collect::<Vec<char>>(),
        "ru" => RU_ABC.chars().collect::<Vec<char>>(),
        _ => abc.chars().collect::<Vec<char>>(),
    };
    let a = mod_add(0, a.unwrap(), abc.len());
    let b = mod_add(0, b.unwrap(), abc.len());
    let encrypted_text = encrypt(&abc, &text, a, b);

    println!("[+] Encrypted text: {}", encrypted_text);
    println!("{}", SEPARATOR);
}

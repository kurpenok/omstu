use modulo::ops::mod_add;

use crate::{cli::console_read, modules::encryptor::encrypt, EN_ABC, RU_ABC, SEPARATOR};

pub fn cli_encrypt() {
    let abc = console_read("[>] Enter abc (en/ru): ");
    let text = console_read("[>] Enter text for encryption: ");
    let key = console_read("[>] Enter key: ").parse::<i32>();

    if (abc.len() == 0 && text.len() != 0) || key.is_err() {
        println!("[-] Incorrect values!");
        println!("{}", SEPARATOR);
        return;
    }

    let abc = match abc.as_str() {
        "en" => EN_ABC.chars().collect::<Vec<char>>(),
        "ru" => RU_ABC.chars().collect::<Vec<char>>(),
        _ => abc.chars().collect::<Vec<char>>(),
    };
    let key = mod_add(0, key.unwrap(), abc.len());
    let encrypted_text = encrypt(&abc, &text, key);

    println!("[+] Encrypted text: {}", encrypted_text);
    println!("{}", SEPARATOR);
}

use modulo::ops::mod_add;

use crate::{cli::console_read, modules::decryptor::decrypt, EN_ABC, RU_ABC, SEPARATOR};

pub fn cli_decrypt() {
    let abc = console_read("[>] Enter abc (en/ru): ");
    let encrypted_text = console_read("[>] Enter encrypted text: ");
    let key = console_read("[>] Enter key: ").parse::<i32>();

    if (abc.len() == 0 && encrypted_text.len() != 0) || key.is_err() {
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
    let decrypted_text = decrypt(&abc, &encrypted_text, key);

    println!("[+] Decrypted text: {}", decrypted_text);
    println!("{}", SEPARATOR);
}

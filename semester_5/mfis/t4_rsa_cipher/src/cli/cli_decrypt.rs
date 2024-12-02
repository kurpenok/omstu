use std::collections::HashMap;

use num_bigint::BigInt;

use crate::{
    cli::console_read,
    modules::{decoder::decode, decryptor::decrypt},
    EN_ABC, RU_ABC, SEPARATOR,
};

pub fn cli_decrypt() {
    let abc = console_read("[>] Enter abc (en/ru): ");
    let encrypted_text = console_read("[>] Enter encrypted text: ");
    let d = console_read("[>] Enter number d: ").parse::<usize>();
    let n = console_read("[>] Enter number n: ").parse::<usize>();

    if (abc.len() == 0 && encrypted_text.len() != 0) || d.is_err() || n.is_err() {
        println!("[-] Incorrect values!");
        println!("{}", SEPARATOR);
        return;
    }

    let mut decode_abc: HashMap<BigInt, char> = HashMap::new();
    match abc.as_str() {
        "en" => {
            for (i, c) in EN_ABC.chars().enumerate() {
                decode_abc.insert(BigInt::from(i + 10), c);
            }
        }
        "ru" => {
            for (i, c) in RU_ABC.chars().enumerate() {
                decode_abc.insert(BigInt::from(i + 10), c);
            }
        }
        _ => {
            for (i, c) in abc.chars().enumerate() {
                decode_abc.insert(BigInt::from(i + 10), c);
            }
        }
    };
    decode_abc.insert(BigInt::from(99), ' ');

    let d = BigInt::from(d.unwrap());
    let n = BigInt::from(n.unwrap());
    let encrypted_message = encrypted_text
        .split_whitespace()
        .filter_map(|code| code.parse::<BigInt>().ok())
        .collect::<Vec<BigInt>>();

    let decrypted_message = decrypt(&encrypted_message, &d, &n);
    let message = decode(&decode_abc, &decrypted_message);

    println!("[+] Decrypted message: {}", message);
    println!("{}", SEPARATOR);
}

use std::collections::HashMap;

use num_bigint::BigInt;
use t4_rsa_cipher::{decoder::decode, decryptor::decrypt};

use crate::{cli::console_read, modules::crack::crack, EN_ABC, RU_ABC, SEPARATOR};

pub fn cli_crack() {
    let abc = console_read("[>] Enter abc (en/ru): ");
    let encrypted_text = console_read("[>] Enter encrypted text: ");
    let e = console_read("[>] Enter number e: ").parse::<usize>();
    let n = console_read("[>] Enter number n: ").parse::<usize>();

    if (abc.len() == 0 && encrypted_text.len() != 0) || e.is_err() || n.is_err() {
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

    let e = BigInt::from(e.unwrap());
    let n = BigInt::from(n.unwrap());
    let rsa_keys = crack(&e, &n);

    let encrypted_message = encrypted_text
        .split_whitespace()
        .filter_map(|code| code.parse::<BigInt>().ok())
        .collect::<Vec<BigInt>>();

    let decrypted_message = decrypt(&encrypted_message, &rsa_keys.d, &n);
    let message = decode(&decode_abc, &decrypted_message);

    println!("[+] Decrypted message: {}", message);
    println!("{}", SEPARATOR);
}

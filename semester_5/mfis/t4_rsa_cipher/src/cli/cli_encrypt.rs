use std::collections::HashMap;

use num_bigint::BigInt;

use crate::{
    cli::console_read,
    modules::{blocks::to_blocks, encoder::encode, encryptor::encrypt},
    EN_ABC, RU_ABC, SEPARATOR,
};

pub fn cli_encrypt() {
    let abc = console_read("[>] Enter abc (en/ru): ");
    let text = console_read("[>] Enter text for encryption: ");
    let e = console_read("[>] Enter number e: ").parse::<usize>();
    let n = console_read("[>] Enter number n: ").parse::<usize>();

    if (abc.len() == 0 && text.len() != 0) || e.is_err() || n.is_err() {
        println!("[-] Incorrect values!");
        println!("{}", SEPARATOR);
        return;
    }

    let mut encode_abc: HashMap<char, BigInt> = HashMap::new();
    match abc.as_str() {
        "en" => {
            for (i, c) in EN_ABC.chars().enumerate() {
                encode_abc.insert(c, BigInt::from(i + 10));
            }
        }
        "ru" => {
            for (i, c) in RU_ABC.chars().enumerate() {
                encode_abc.insert(c, BigInt::from(i + 10));
            }
        }
        _ => {
            for (i, c) in abc.chars().enumerate() {
                encode_abc.insert(c, BigInt::from(i + 10));
            }
        }
    };
    encode_abc.insert(' ', BigInt::from(99));

    let encoded_message = encode(&encode_abc, &text);
    let blocks = to_blocks(&encoded_message, 4);

    let e = BigInt::from(e.unwrap());
    let n = BigInt::from(n.unwrap());
    let encrypted_message = encrypt(&blocks, &e, &n);

    println!("[+] Encrypted string: {:?}", encrypted_message);
    println!("{}", SEPARATOR);
}

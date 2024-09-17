use modicum::AddMod;

use crate::{
    cli_args::{Decrypt, Encrypt},
    decryptor::decrypt,
    encryptor::encrypt,
};

pub fn cli_encrypt(data: &Encrypt) {
    let abc = data.abc.clone().chars().collect::<Vec<char>>();

    let m = data.abc.len() as u32;
    let key = 0.add_mod(data.key, m) as usize;

    println!(
        "[+] Encrypted string: {}",
        encrypt(&abc, &data.message, key)
    );
}

pub fn cli_decrypt(data: &Decrypt) {
    let abc = data.abc.clone().chars().collect::<Vec<char>>();

    if data.key.is_some() {
        let m = data.abc.len() as u32;
        let key = 0.add_mod(data.key.unwrap(), m) as usize;

        println!(
            "[+] Decrypted string: {}",
            decrypt(&abc, &data.message, key)
        );
    } else {
        for k in 1..abc.len() {
            let m = data.abc.len() as u32;
            let key = 0.add_mod(k, m) as usize;

            println!(
                "[+] Decrypted string: {}",
                decrypt(&abc, &data.message, key)
            );
        }
    }
}

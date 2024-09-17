use crate::{
    cli_args::{Decrypt, Encrypt},
    decryptor::decrypt,
    encryptor::encrypt,
};

pub fn cli_encrypt(data: &Encrypt) {
    let abc = data.abc.clone().chars().collect::<Vec<char>>();

    println!(
        "[+] Encrypted string: {}",
        encrypt(&abc, &data.message, data.key)
    );
}

pub fn cli_decrypt(data: &Decrypt) {
    let abc = data.abc.clone().chars().collect::<Vec<char>>();

    if data.key.is_some() {
        println!(
            "[+] Decrypted string: {}",
            decrypt(&abc, &data.message, data.key.unwrap())
        );
    } else {
        for k in 1..abc.len() {
            println!("[+] Decrypted string: {}", decrypt(&abc, &data.message, k));
        }
    }
}

use crate::{
    analysis::{get_frequency, get_most_common_chars},
    cli_args::{Analysis, Decrypt, Encrypt},
    decryptor::decrypt,
    encryptor::encrypt,
};

pub fn cli_encrypt(data: &Encrypt) {
    let abc = data.abc.clone().chars().collect::<Vec<char>>();
    println!(
        "[+] Encrypted string: {}",
        encrypt(&abc, &data.message, data.a, data.b)
    );
}

pub fn cli_decrypt(data: &Decrypt) {
    let abc = data.abc.clone().chars().collect::<Vec<char>>();

    let decrypted_results = decrypt(&abc, &data.message);
    for decrypted_result in &decrypted_results {
        if decrypted_result.s.len() != 0 {
            println!(
                "[+] Decrypted result ({}, {}): {}",
                decrypted_result.a, decrypted_result.b, decrypted_result.s
            );
        }
    }
}

pub fn cli_analysis(data: &Analysis) {
    println!(
        "[+] Most common char: {:?}",
        get_most_common_chars(&get_frequency(&data.message), 2)
    );
}

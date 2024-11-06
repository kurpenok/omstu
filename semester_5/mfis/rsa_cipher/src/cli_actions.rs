use std::collections::HashMap;

use num_bigint::BigInt;

use crate::{
    blocks::to_blocks,
    cli_args::{Crack, Decrypt, Encrypt, Generate},
    crack::crack,
    decoder::decode,
    decryptor::decrypt,
    encoder::encode,
    encryptor::encrypt,
    keygen::generate_rsa_keys,
};

pub fn cli_generate(data: &Generate) {
    let p = BigInt::from(data.p);
    let q = BigInt::from(data.q);
    let e = match data.e {
        Some(e) => Some(BigInt::from(e)),
        None => None,
    };
    let rsa_keys = generate_rsa_keys(&p, &q, e.as_ref());

    let e = rsa_keys.e;
    let d = rsa_keys.d;
    let n = rsa_keys.n;
    println!("[+] Generated keys (e, d, n): {}, {}, {}", e, d, n);
}

pub fn cli_encrypt(data: &Encrypt) {
    let mut encode_abc: HashMap<char, BigInt> = HashMap::new();
    for (i, c) in data.abc.chars().enumerate() {
        encode_abc.insert(c, BigInt::from(i + 10));
    }
    encode_abc.insert(' ', BigInt::from(99));

    let encoded_message = encode(&encode_abc, &data.message);
    let blocks = to_blocks(&encoded_message, 4);

    let e = BigInt::from(data.e);
    let n = BigInt::from(data.n);
    let encrypted_message = encrypt(&blocks, &e, &n);

    println!("[+] Encrypted string: {:?}", encrypted_message);
}

pub fn cli_decrypt(data: &Decrypt) {
    let mut decode_abc: HashMap<BigInt, char> = HashMap::new();
    for (i, c) in data.abc.chars().enumerate() {
        decode_abc.insert(BigInt::from(i + 10), c);
    }
    decode_abc.insert(BigInt::from(99), ' ');

    let d = BigInt::from(data.d);
    let n = BigInt::from(data.n);
    let encrypted_message = data
        .message
        .split_whitespace()
        .filter_map(|code| code.parse::<BigInt>().ok())
        .collect::<Vec<BigInt>>();

    let decrypted_message = decrypt(&encrypted_message, &d, &n);
    let message = decode(&decode_abc, &decrypted_message);

    println!("[+] Decrypted message: {}", message);
}

pub fn cli_crack(data: &Crack) {
    let mut decode_abc: HashMap<BigInt, char> = HashMap::new();
    for (i, c) in data.abc.chars().enumerate() {
        decode_abc.insert(BigInt::from(i + 10), c);
    }
    decode_abc.insert(BigInt::from(99), ' ');

    let e = BigInt::from(data.e);
    let n = BigInt::from(data.n);
    let rsa_keys = crack(&e, &n);

    let encrypted_message = data
        .message
        .split_whitespace()
        .filter_map(|code| code.parse::<BigInt>().ok())
        .collect::<Vec<BigInt>>();

    let decrypted_message = decrypt(&encrypted_message, &rsa_keys.d, &n);
    let message = decode(&decode_abc, &decrypted_message);

    println!("[+] Decrypted message: {}", message);
}

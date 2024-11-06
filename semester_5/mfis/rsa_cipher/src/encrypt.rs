use num_bigint::BigInt;

fn encrypt_block(message: &BigInt, e: &BigInt, n: &BigInt) -> BigInt {
    message.modpow(e, n)
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_encrypt_block() {
        let message = BigInt::from(89);
        let e = BigInt::from(3);
        let n = BigInt::from(3127);
        let encrypted_message = BigInt::from(1394);
        assert_eq!(encrypt_block(&message, &e, &n), encrypted_message);
    }
}

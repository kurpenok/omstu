use num_bigint::BigInt;

fn encrypt_block(block: &BigInt, e: &BigInt, n: &BigInt) -> BigInt {
    block.modpow(e, n)
}

pub fn encrypt(message_blocks: &Vec<BigInt>, e: &BigInt, n: &BigInt) -> Vec<BigInt> {
    message_blocks
        .iter()
        .map(|block| encrypt_block(&block, e, n))
        .collect()
}

#[cfg(test)]
mod test {
    use num_bigint::ToBigInt;

    use super::*;

    #[test]
    fn test_encrypt_block() {
        let message = BigInt::from(89);
        let e = BigInt::from(3);
        let n = BigInt::from(3127);
        let encrypted_message = BigInt::from(1394);
        assert_eq!(encrypt_block(&message, &e, &n), encrypted_message);
    }

    #[test]
    fn test_encrypt() {
        let message_blocks = vec![10119.to_bigint().unwrap(), 91110.to_bigint().unwrap()];
        let e = 3.to_bigint().unwrap();
        let n = 3127.to_bigint().unwrap();
        let encrypted_message_blocks = vec![2692.to_bigint().unwrap(), 1564.to_bigint().unwrap()];
        assert_eq!(encrypt(&message_blocks, &e, &n), encrypted_message_blocks);
    }
}

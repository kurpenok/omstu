use num_bigint::BigInt;

pub fn encrypt(blocks: &[BigInt], e: &BigInt, n: &BigInt) -> Vec<BigInt> {
    blocks.iter().map(|block| block.modpow(e, n)).collect()
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_encrypt() {
        let blocks = vec![BigInt::from(1011), BigInt::from(2945)];
        let e = BigInt::from(3);
        let n = BigInt::from(3127);
        let encrypted_blocks = vec![BigInt::from(276), BigInt::from(288)];

        assert_eq!(encrypt(&blocks, &e, &n), encrypted_blocks);
    }
}

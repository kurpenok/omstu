use num_bigint::BigInt;

pub fn decrypt(blocks: &[BigInt], d: &BigInt, n: &BigInt) -> Vec<BigInt> {
    blocks.iter().map(|block| block.modpow(d, n)).collect()
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_decrypt() {
        let encrypted_blocks = vec![BigInt::from(276), BigInt::from(288)];
        let d = BigInt::from(2011);
        let n = BigInt::from(3127);
        let blocks = vec![BigInt::from(1011), BigInt::from(2945)];
        assert_eq!(decrypt(&encrypted_blocks, &d, &n), blocks);
    }
}

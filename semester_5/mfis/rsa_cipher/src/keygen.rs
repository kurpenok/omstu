use num_bigint::BigInt;
use num_bigint::ToBigInt;
use num_traits::One;

use crate::gcd::gcd;
use crate::invert::invert;

#[derive(Debug, PartialEq)]
pub struct RSAKeys {
    pub e: BigInt,
    pub d: BigInt,
    pub n: BigInt,
}

pub fn generate_rsa_keys(p: &BigInt, q: &BigInt) -> RSAKeys {
    let n = p * q;
    let phi = (p - 1.to_bigint().unwrap()) * (q - 1.to_bigint().unwrap());

    let mut e = 3.to_bigint().unwrap(); // Usually 65537
    while gcd(&e, &phi) != BigInt::one() {
        e += 2.to_bigint().unwrap();
    }

    let d = invert(&e, &phi).unwrap();

    RSAKeys { e, d, n }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_generate_rsa_keys() {
        let p = 53.to_bigint().unwrap();
        let q = 59.to_bigint().unwrap();
        let rsa_keys = RSAKeys {
            e: 3.to_bigint().unwrap(),
            d: 2011.to_bigint().unwrap(),
            n: 3127.to_bigint().unwrap(),
        };
        assert_eq!(generate_rsa_keys(&p, &q), rsa_keys);
    }
}

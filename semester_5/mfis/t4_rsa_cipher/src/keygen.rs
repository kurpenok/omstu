use num_bigint::BigInt;

use crate::invert::invert;
use crate::prime::generate_prime;

#[derive(Debug, PartialEq)]
pub struct RSAKeys {
    pub e: BigInt,
    pub d: BigInt,
    pub n: BigInt,
}

pub fn generate_rsa_keys(p: &BigInt, q: &BigInt, e: Option<&BigInt>) -> Option<RSAKeys> {
    let n = p * q;
    let phi = (p - BigInt::from(1)) * (q - BigInt::from(1));

    let e = match e {
        Some(e) => e.clone(),
        None => generate_prime(16),
    };

    match invert(&e, &phi) {
        Some(d) => return Some(RSAKeys { e, d, n }),
        None => None,
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_generate_rsa_keys() {
        let p = BigInt::from(53);
        let q = BigInt::from(59);
        let rsa_keys = RSAKeys {
            e: BigInt::from(3),
            d: BigInt::from(2011),
            n: BigInt::from(3127),
        };
        assert_eq!(
            generate_rsa_keys(&p, &q, Some(&BigInt::from(3))),
            Some(rsa_keys)
        );
    }
}

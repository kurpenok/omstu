use num_bigint::BigInt;
use num_traits::One;

use crate::{invert::invert, keygen::RSAKeys, prime::is_prime};

pub fn crack(e: &BigInt, n: &BigInt) -> RSAKeys {
    for p in 0..1000 {
        for q in 0..1000 {
            let p = BigInt::from(p);
            let q = BigInt::from(q);
            if n == &(&p * &q) && is_prime(&p) && is_prime(&q) {
                let phi = (p - BigInt::one()) * (q - BigInt::one());
                let d = invert(e, &phi).unwrap();

                return RSAKeys {
                    e: e.clone(),
                    d: d.clone(),
                    n: n.clone(),
                };
            }
        }
    }

    RSAKeys {
        e: BigInt::from(0),
        d: BigInt::from(0),
        n: BigInt::from(0),
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_rsa_crack() {
        let rsa_keys = RSAKeys {
            e: BigInt::from(3),
            d: BigInt::from(2011),
            n: BigInt::from(3127),
        };

        let e = BigInt::from(3);
        let n = BigInt::from(3127);

        assert_eq!(crack(&e, &n), rsa_keys);
    }
}

use num_bigint::BigInt;
use num_traits::{One, Zero};

use crate::gcd::{extended_gcd, BezuCoefs};

pub fn invert(a: &BigInt, m: &BigInt) -> Option<BigInt> {
    let mut coefs = BezuCoefs {
        alpha: BigInt::zero(),
        beta: BigInt::zero(),
    };
    let divider = extended_gcd(a, m, &mut coefs);

    if !divider.is_one() {
        return None;
    }

    Some((coefs.alpha % m + m) % m)
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_bigint_invert() {
        let a = BigInt::from(2);
        let b = BigInt::from(6);
        assert_eq!(invert(&a, &b), None);

        let a = BigInt::from(8);
        let b = BigInt::from(64);
        assert_eq!(invert(&a, &b), None);

        let a = BigInt::from(3);
        let b = BigInt::from(7);
        let c = BigInt::from(5);
        assert_eq!(invert(&a, &b), Some(c));

        let a = BigInt::from(3);
        let b = BigInt::from(26);
        let c = BigInt::from(9);
        assert_eq!(invert(&a, &b), Some(c));
    }
}

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
    use num_bigint::ToBigInt;

    use super::*;

    #[test]
    fn test_bigint_invert() {
        assert_eq!(
            invert(&2.to_bigint().unwrap(), &6.to_bigint().unwrap()),
            None
        );
        assert_eq!(
            invert(&8.to_bigint().unwrap(), &64.to_bigint().unwrap()),
            None
        );

        assert_eq!(
            invert(&3.to_bigint().unwrap(), &7.to_bigint().unwrap()),
            Some(5.to_bigint().unwrap())
        );
        assert_eq!(
            invert(&3.to_bigint().unwrap(), &26.to_bigint().unwrap()),
            Some(9.to_bigint().unwrap())
        );
    }
}

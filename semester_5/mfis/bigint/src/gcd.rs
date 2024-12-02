use num_bigint::BigInt;
use num_traits::{One, Zero};

pub struct BezuCoefs {
    pub alpha: BigInt,
    pub beta: BigInt,
}

pub fn gcd(a: &BigInt, b: &BigInt) -> BigInt {
    if b.is_zero() {
        return a.clone();
    }

    gcd(b, &(a % b))
}

pub fn extended_gcd(a: &BigInt, b: &BigInt, coefs: &mut BezuCoefs) -> BigInt {
    if a.is_zero() {
        coefs.alpha = BigInt::zero();
        coefs.beta = BigInt::one();
        return b.clone();
    }

    let mut temp_coefs = BezuCoefs {
        alpha: BigInt::zero(),
        beta: BigInt::zero(),
    };
    let divider = extended_gcd(&(b % a), a, &mut temp_coefs);

    coefs.alpha = temp_coefs.beta - (b / a) * &temp_coefs.alpha;
    coefs.beta = temp_coefs.alpha;

    divider
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_bigint_gcd() {
        let a = BigInt::from(6);
        let b = BigInt::from(4);
        let c = BigInt::from(2);

        let d = BigInt::from(13);
        let e = BigInt::from(19);

        assert_eq!(gcd(&a, &b), c);
        assert_eq!(gcd(&c, &c), c);
        assert_eq!(gcd(&d, &e), BigInt::one());
    }

    #[test]
    fn test_bigint_extended_gcd() {
        let a = BigInt::from(3);
        let b = BigInt::from(7);
        let mut coefs = BezuCoefs {
            alpha: BigInt::zero(),
            beta: BigInt::zero(),
        };

        assert_eq!(extended_gcd(&a, &b, &mut coefs), BigInt::one());
        assert_eq!(coefs.alpha, BigInt::from(-2));
        assert_eq!(coefs.beta, BigInt::from(1));
    }
}

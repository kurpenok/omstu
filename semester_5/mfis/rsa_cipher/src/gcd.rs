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
    use num_bigint::ToBigInt;

    use super::*;

    #[test]
    fn test_bigint_gcd() {
        assert_eq!(
            gcd(&6.to_bigint().unwrap(), &4.to_bigint().unwrap()),
            2.to_bigint().unwrap()
        );
        assert_eq!(
            gcd(&10.to_bigint().unwrap(), &5.to_bigint().unwrap()),
            5.to_bigint().unwrap()
        );
        assert_eq!(
            gcd(&19.to_bigint().unwrap(), &17.to_bigint().unwrap()),
            1.to_bigint().unwrap()
        );
        assert_eq!(
            gcd(&20.to_bigint().unwrap(), &20.to_bigint().unwrap()),
            20.to_bigint().unwrap()
        );
    }

    #[test]
    fn test_bigint_extended_gcd() {
        let mut coefs = BezuCoefs {
            alpha: 0.to_bigint().unwrap(),
            beta: 0.to_bigint().unwrap(),
        };

        assert_eq!(
            extended_gcd(&3.to_bigint().unwrap(), &7.to_bigint().unwrap(), &mut coefs),
            1.to_bigint().unwrap()
        );
        assert_eq!(coefs.alpha, -2.to_bigint().unwrap());
        assert_eq!(coefs.beta, 1.to_bigint().unwrap());
    }
}

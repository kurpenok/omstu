use num_bigint::{BigInt, ToBigInt};
use num_traits::{One, Zero};

fn is_prime(n: &BigInt) -> bool {
    if n <= &BigInt::one() {
        return false;
    } else if n == &BigInt::from(2) {
        return true;
    } else if (n % 2.to_bigint().unwrap()).is_zero() {
        return false;
    }

    let mut i = BigInt::from(3);
    while &i <= &n.sqrt() {
        if n % &i == BigInt::zero() {
            return false;
        }
        i += BigInt::from(2);
    }

    true
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_bigint_is_prime() {
        assert_eq!(is_prime(&BigInt::from(0)), false);
        assert_eq!(is_prime(&BigInt::from(1)), false);
        assert_eq!(is_prime(&BigInt::from(2)), true);
        assert_eq!(is_prime(&BigInt::from(3)), true);
        assert_eq!(is_prime(&BigInt::from(4)), false);
    }
}

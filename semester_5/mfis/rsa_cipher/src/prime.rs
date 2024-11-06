use num_bigint::{BigInt, RandBigInt, ToBigInt};
use num_traits::{One, Zero};
use rand::thread_rng;

pub fn is_prime(n: &BigInt) -> bool {
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

pub fn generate_prime(bits: usize) -> BigInt {
    let mut rng = thread_rng();
    loop {
        let number = rng.gen_bigint(bits as u64);
        if is_prime(&number) {
            break number;
        }
    }
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

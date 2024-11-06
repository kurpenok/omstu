use num_bigint::BigInt;
use num_traits::Zero;

pub fn gcd(a: &BigInt, b: &BigInt) -> BigInt {
    if b.is_zero() {
        return a.clone();
    }

    gcd(b, &(a % b))
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
}

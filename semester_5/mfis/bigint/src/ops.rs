use num_bigint::BigInt;
use num_traits::{One, Zero};

pub fn mod_pow(a: &BigInt, p: &BigInt, m: &BigInt) -> BigInt {
    if p == &BigInt::zero() {
        return BigInt::one();
    }

    let prod = mod_pow(&(a % m), &(p / BigInt::from(2)), m) % m;

    if p % 2 == BigInt::zero() {
        (&prod * &prod) % m
    } else {
        ((a % m) * ((&prod * &prod) % m)) % m
    }
}

use crate::invert::invert;

pub fn mod_add(a: i32, b: i32, m: i32) -> i32 {
    let mut sum = a + b;

    while sum < 0 {
        sum += m;
    }

    sum % m
}

pub fn mod_sub(a: i32, b: i32, m: i32) -> i32 {
    let mut diff = a - b;

    while diff < 0 {
        diff += m;
    }

    diff % m
}

pub fn mod_mul(a: i32, b: i32, m: i32) -> i32 {
    let mut prod = a * b;

    while prod < 0 {
        prod += m;
    }

    prod % m
}

pub fn mod_div(a: i32, b: i32, m: i32) -> Option<i32> {
    let inverted_b = invert(b, m);
    if inverted_b.is_none() {
        return None;
    }

    let mut quot = a * inverted_b.unwrap();

    while quot < 0 {
        quot += m;
    }

    Some(quot % m)
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_modulo_addition() {
        assert_eq!(mod_add(1, 2, 10), 3);
        assert_eq!(mod_add(6, 8, 12), 2);
        assert_eq!(mod_add(-47, 17, 8), 2);
    }

    #[test]
    fn test_modulo_subtraction() {
        assert_eq!(mod_sub(1, 2, 10), 9);
        assert_eq!(mod_sub(6, 8, 12), 10);
        assert_eq!(mod_sub(-47, 17, 8), 0);
    }

    #[test]
    fn test_modulo_multiplication() {
        assert_eq!(mod_mul(1, 2, 10), 2);
        assert_eq!(mod_mul(6, 8, 12), 0);
        assert_eq!(mod_mul(-47, 17, 8), 1);
    }

    #[test]
    fn test_modulo_division() {
        assert_eq!(mod_div(1, 2, 7), Some(4));
        assert_eq!(mod_div(6, 8, 17), Some(5));
        assert_eq!(mod_div(-47, 17, 19), Some(14));
    }
}

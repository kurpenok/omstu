use super::invert::invert;

pub fn mod_add(a: i32, b: i32, m: usize) -> usize {
    let mut sum = a + b;

    while sum < 0 {
        sum += m as i32;
    }

    sum as usize % m
}

pub fn mod_sub(a: i32, b: i32, m: usize) -> usize {
    let mut diff = a - b;

    while diff < 0 {
        diff += m as i32;
    }

    diff as usize % m
}

pub fn mod_mul(a: i32, b: i32, m: usize) -> usize {
    let mut prod = a * b;

    while prod < 0 {
        prod += m as i32;
    }

    prod as usize % m
}

pub fn mod_div(a: usize, b: usize, m: usize) -> Option<usize> {
    match invert(b, m) {
        Some(inverted_b) => Some(a * inverted_b % m),
        None => None,
    }
}

pub fn mod_pow(a: i32, p: u32, m: usize) -> usize {
    let mut prod = a.pow(p);

    while prod < 0 {
        prod += m as i32;
    }

    prod as usize % m
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
        assert_eq!(mod_div(10, 17, 19), Some(14));
    }

    #[test]
    fn test_modulo_exponentiation() {
        assert_eq!(mod_pow(1, 2, 10), 1);
        assert_eq!(mod_pow(6, 8, 12), 0);
        assert_eq!(mod_pow(-7, 7, 8), 1);
    }
}
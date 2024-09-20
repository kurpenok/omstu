pub fn add(a: i32, b: i32, m: i32) -> i32 {
    let mut sum = a + b;

    while sum < 0 {
        sum += m;
    }

    sum % m
}

pub fn sub(a: i32, b: i32, m: i32) -> i32 {
    let mut sum = a - b;

    while sum < 0 {
        sum += m;
    }

    sum % m
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_modulo_addition() {
        assert_eq!(add(1, 2, 10), 3);
        assert_eq!(add(6, 8, 12), 2);
        assert_eq!(add(-47, 17, 8), 2);
    }

    #[test]
    fn test_modulo_subtraction() {
        assert_eq!(sub(1, 2, 10), 9);
        assert_eq!(sub(6, 8, 12), 10);
        assert_eq!(sub(-47, 17, 8), 0);
    }
}

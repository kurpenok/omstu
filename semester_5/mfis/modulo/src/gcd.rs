pub fn gcd(a: usize, b: usize) -> usize {
    let mut a = a;
    let mut b = b;

    while b != 0 {
        let t = b;
        b = a % b;
        a = t;
    }

    a
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_gcd() {
        assert_eq!(gcd(6, 4), 2);
        assert_eq!(gcd(10, 5), 5);
        assert_eq!(gcd(19, 17), 1);
        assert_eq!(gcd(20, 20), 20);
    }
}

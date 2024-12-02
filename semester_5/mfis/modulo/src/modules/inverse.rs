use super::gcd::{extended_gcd, BezuCoefs};

pub fn get_inverse(a: usize, m: usize) -> Option<usize> {
    let mut coefs = BezuCoefs::new();
    let divider = extended_gcd(a, m, &mut coefs);

    if divider != 1 {
        return None;
    }

    Some((coefs.alpha % m as i32 + m as i32) as usize % m)
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_inverse() {
        assert_eq!(get_inverse(2, 6), None);
        assert_eq!(get_inverse(8, 64), None);

        assert_eq!(get_inverse(3, 7), Some(5));
        assert_eq!(get_inverse(3, 26), Some(9));
    }
}

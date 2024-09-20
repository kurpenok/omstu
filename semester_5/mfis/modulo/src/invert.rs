use crate::gcd::{extended_gcd, BezuCoefs};

pub fn invert(a: i32, m: i32) -> Option<i32> {
    let mut coefs = BezuCoefs { alpha: 0, beta: 0 };
    let divider = extended_gcd(a, m, &mut coefs);

    if divider != 1 {
        return None;
    }

    Some((coefs.alpha % m + m) % m)
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_invert() {
        assert_eq!(invert(2, 6), None);
        assert_eq!(invert(8, 64), None);

        assert_eq!(invert(3, 7), Some(5));
        assert_eq!(invert(3, 26), Some(9));
    }
}

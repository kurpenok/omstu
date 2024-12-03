use std::collections::HashMap;

use modulo::ops::mod_pow;

pub fn find_logarithm(a: usize, b: usize, p: usize) -> usize {
    let k = (p as f64).sqrt().ceil() as usize;

    let mut ys: HashMap<usize, usize> = HashMap::new();
    let mut zs: HashMap<usize, usize> = HashMap::new();

    for i in 1..=10 {
        let y = mod_pow(a, i * k, p);
        ys.insert(y, i);
    }

    for i in 1..=10 {
        let z = (b * mod_pow(a, i, p)) % p;
        zs.insert(z, i);
    }

    for (y, i) in &ys {
        if zs.contains_key(y) {
            let j = zs[y];
            return i * k - j;
        }
    }

    0
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_find_logarithm() {
        assert_eq!(find_logarithm(6, 15, 109), 20);
    }
}

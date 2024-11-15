use std::collections::HashMap;

use num_bigint::BigInt;

pub fn encode(abc: &HashMap<char, BigInt>, message: &String) -> Vec<BigInt> {
    message
        .chars()
        .filter_map(|c| abc.get(&c).cloned())
        .collect()
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_encode() {
        let abc = HashMap::from([
            ('a', BigInt::from(10)),
            ('b', BigInt::from(11)),
            (' ', BigInt::from(99)),
        ]);
        let message = "ab ba".to_string();

        assert_eq!(
            encode(&abc, &message),
            vec![
                BigInt::from(10),
                BigInt::from(11),
                BigInt::from(99),
                BigInt::from(11),
                BigInt::from(10),
            ]
        );
    }
}

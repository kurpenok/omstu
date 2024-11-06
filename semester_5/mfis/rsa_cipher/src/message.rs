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
    use num_bigint::ToBigInt;

    use super::*;

    #[test]
    fn test_encode_message() {
        let abc = HashMap::from([
            ('a', 10.to_bigint().unwrap()),
            ('b', 11.to_bigint().unwrap()),
            (' ', 99.to_bigint().unwrap()),
        ]);
        let message = "ab ba".to_string();

        assert_eq!(
            encode(&abc, &message),
            vec![
                10.to_bigint().unwrap(),
                11.to_bigint().unwrap(),
                99.to_bigint().unwrap(),
                11.to_bigint().unwrap(),
                10.to_bigint().unwrap()
            ]
        );
    }
}

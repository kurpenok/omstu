use std::collections::HashMap;

use num_bigint::BigInt;

pub fn decode(abc: &HashMap<BigInt, char>, encoded_message: &[BigInt]) -> String {
    let encoded_message: String = encoded_message
        .iter()
        .map(|block| block.to_string())
        .collect();

    let mut message = String::new();
    for i in (2..=encoded_message.len()).step_by(2) {
        message.push(abc[&BigInt::parse_bytes(&encoded_message[i - 2..i].as_bytes(), 10).unwrap()]);
    }

    message
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_decode() {
        let abc = HashMap::from([
            (BigInt::from(10), 'a'),
            (BigInt::from(11), 'b'),
            (BigInt::from(99), ' '),
        ]);
        let encoded_message = vec![
            BigInt::from(10),
            BigInt::from(11),
            BigInt::from(99),
            BigInt::from(11),
            BigInt::from(10),
        ];

        assert_eq!(decode(&abc, &encoded_message), "ab ba");
    }
}

use std::collections::HashMap;

use num_bigint::BigInt;

pub fn encode_message(abc: &HashMap<char, BigInt>, message: &String) -> Vec<BigInt> {
    message
        .chars()
        .filter_map(|c| abc.get(&c).cloned())
        .collect()
}

fn validate_and_convert_blocks(message_blocks: Vec<String>) -> Vec<BigInt> {
    let mut message_blocks = message_blocks;

    for i in 1..message_blocks.len() {
        let mut block_digits: Vec<char> = message_blocks[i].chars().collect();
        if block_digits[0] == '0' {
            message_blocks[i - 1].push('0');
            block_digits.remove(0);
            message_blocks[i] = block_digits.into_iter().collect();
        }
    }

    message_blocks
        .iter()
        .map(|block| BigInt::parse_bytes(block.as_bytes(), 10).unwrap())
        .collect()
}

pub fn message_to_blocks(encoded_message: &[BigInt], block_size: usize) -> Vec<BigInt> {
    let mut message_blocks: Vec<String> = Vec::new();

    let message_codes: String = encoded_message.iter().map(|c| c.to_string()).collect();
    let message_digits: Vec<char> = message_codes.chars().collect();

    let mut block = String::new();
    for i in 0..message_digits.len() {
        if i != 0 && i % block_size == 0 {
            message_blocks.push(block.clone());
            block.clear();
        }
        block.push(message_digits[i]);
    }

    if !block.is_empty() {
        message_blocks.push(block);
    }

    validate_and_convert_blocks(message_blocks)
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
            encode_message(&abc, &message),
            vec![
                10.to_bigint().unwrap(),
                11.to_bigint().unwrap(),
                99.to_bigint().unwrap(),
                11.to_bigint().unwrap(),
                10.to_bigint().unwrap()
            ]
        );
    }

    #[test]
    fn test_message_to_blocks() {
        let encoded_message = vec![
            11.to_bigint().unwrap(),
            10.to_bigint().unwrap(),
            99.to_bigint().unwrap(),
            10.to_bigint().unwrap(),
            11.to_bigint().unwrap(),
        ];

        assert_eq!(
            message_to_blocks(&encoded_message, 3),
            vec![
                1110.to_bigint().unwrap(),
                99.to_bigint().unwrap(),
                101.to_bigint().unwrap(),
                1.to_bigint().unwrap()
            ]
        );
    }
}

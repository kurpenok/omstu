use num_bigint::BigInt;

fn validate_blocks(blocks: Vec<String>) -> Vec<String> {
    let mut validated_blocks: Vec<String> = vec![blocks[0].clone()];

    for i in 1..blocks.len() {
        let mut block_digits: Vec<char> = blocks[i].chars().collect();
        if block_digits[0] == '0' {
            validated_blocks[i - 1].push('0');
            block_digits.remove(0);
        }
        validated_blocks.push(block_digits.into_iter().collect());
    }

    validated_blocks
}

pub fn to_blocks(encoded_message: &[BigInt], block_size: usize) -> Vec<BigInt> {
    let mut blocks: Vec<String> = Vec::new();

    let codes: String = encoded_message.iter().map(|c| c.to_string()).collect();
    let digits: Vec<char> = codes.chars().collect();

    let mut block = String::new();
    for i in 0..digits.len() {
        if i != 0 && i % block_size == 0 {
            blocks.push(block.clone());
            block.clear();
        }
        block.push(digits[i]);
    }

    if !block.is_empty() {
        blocks.push(block);
    }

    validate_blocks(blocks)
        .iter()
        .map(|block| BigInt::parse_bytes(block.as_bytes(), 10).unwrap())
        .collect()
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_validate_blocks() {
        let blocks = vec!["111".to_string(), "099".to_string(), "047".to_string()];

        assert_eq!(validate_blocks(blocks), ["1110", "990", "47"]);
    }

    #[test]
    fn test_message_to_blocks() {
        let encoded_message = vec![
            BigInt::from(11),
            BigInt::from(10),
            BigInt::from(99),
            BigInt::from(10),
            BigInt::from(11),
        ];
        let block_size = 3;

        assert_eq!(
            to_blocks(&encoded_message, block_size),
            vec![
                BigInt::from(1110),
                BigInt::from(99),
                BigInt::from(101),
                BigInt::from(1),
            ]
        );
    }
}

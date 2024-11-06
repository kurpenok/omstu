use std::collections::HashMap;

pub fn encode(abc: &HashMap<char, usize>, message: &String) -> Vec<usize> {
    message
        .chars()
        .filter_map(|c| abc.get(&c).copied())
        .collect()
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_encode_message() {
        let abc = HashMap::from([('a', 10), ('b', 11), (' ', 99)]);
        let message = "ab ba".to_string();
        assert_eq!(encode(&abc, &message), vec![10, 11, 99, 11, 10]);
    }
}

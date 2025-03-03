use std::collections::HashMap;

pub fn get_k_grams(s_chars: &Vec<char>, k: usize) -> HashMap<String, f64> {
    let mut k_gram_frequency: HashMap<String, f64> = HashMap::new();

    if k == 0 || s_chars.len() < k {
        return k_gram_frequency;
    }

    for i in 0..=s_chars.len() - k {
        let k_gram = &s_chars[i..i + k];
        k_gram_frequency
            .entry(k_gram.iter().collect())
            .and_modify(|count| *count += 1.0)
            .or_insert(1.0);
    }

    for count in k_gram_frequency.values_mut() {
        *count /= (s_chars.len() - k + 1) as f64;
    }

    k_gram_frequency
}

pub fn get_k_grams_entropy(s: &str, k: usize) -> f64 {
    let s_chars: Vec<char> = s.chars().collect();
    let mut k_gram_entropy: f64 = 0.0;

    for (_, &frequency) in &get_k_grams(&s_chars, k) {
        let p = frequency as f64;
        k_gram_entropy += p * p.log2();
    }

    -k_gram_entropy / k as f64
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_get_k_grams() {
        let k_gram_frequency: HashMap<String, f64> = HashMap::new();
        assert_eq!(get_k_grams(&vec!['a', 'b', 'c'], 0), k_gram_frequency);

        let k_gram_frequency: HashMap<String, f64> = HashMap::new();
        assert_eq!(get_k_grams(&vec!['a', 'b', 'c'], 4), k_gram_frequency);

        let mut k_gram_frequency: HashMap<String, f64> = HashMap::new();
        k_gram_frequency.insert("a".to_string(), 1.0 / 3.0);
        k_gram_frequency.insert("b".to_string(), 1.0 / 3.0);
        k_gram_frequency.insert("c".to_string(), 1.0 / 3.0);
        assert_eq!(get_k_grams(&vec!['a', 'b', 'c'], 1), k_gram_frequency);

        let mut k_gram_frequency: HashMap<String, f64> = HashMap::new();
        k_gram_frequency.insert("ab".to_string(), 1.0 / 2.0);
        k_gram_frequency.insert("bc".to_string(), 1.0 / 2.0);
        assert_eq!(get_k_grams(&vec!['a', 'b', 'c'], 2), k_gram_frequency);
    }
}

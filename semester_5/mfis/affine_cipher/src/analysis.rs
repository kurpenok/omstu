use std::collections::HashMap;

pub fn get_frequency(s: &String) -> HashMap<char, usize> {
    let mut frequency = HashMap::new();

    s.chars().for_each(|c| {
        frequency
            .entry(c)
            .and_modify(|count| *count += 1)
            .or_insert(1);
    });

    frequency
}

pub fn get_most_common_chars(frequency: &HashMap<char, usize>, n: usize) -> Vec<char> {
    let mut values: Vec<(char, usize)> = frequency.iter().map(|(k, v)| (*k, *v)).collect();
    values.sort_by(|a, b| b.1.cmp(&a.1));
    values.into_iter().take(n).map(|(k, _)| k).collect()
}

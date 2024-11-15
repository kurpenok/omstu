use crate::{cli_args::Entropy, k_gram::get_k_grams_entropy, plot::show_entropy};

pub fn cli_entropy(data: &Entropy) {
    let abc: Vec<char> = data.abc.chars().collect();
    let mut new_message = String::new();

    for c in data.message.to_lowercase().chars() {
        if abc.contains(&c) {
            new_message.push(c);
        }
    }

    let mut entropies: Vec<f64> = Vec::new();
    for i in 1..10 {
        let k_grams_entropy = get_k_grams_entropy(&new_message, i);
        println!("[+] Entropy for {}-gram: {}", i, k_grams_entropy);

        entropies.push(k_grams_entropy);
    }

    show_entropy(&entropies, &data.path);
}

use crate::{
    modules::{k_gram::get_k_grams_entropy, plot::show_entropy},
    EN_ABC, RU_ABC, SEPARATOR,
};

use super::console_read;

pub fn cli_entropy() {
    let abc = console_read("[>] Enter abc (en/ru): ");
    let text = console_read("[>] Enter text for get entropy: ");
    let path = console_read("[>] Enter path for save plot (empty for default): ");

    if abc.len() == 0 && text.len() != 0 {
        println!("[-] Incorrect values!");
        println!("{}", SEPARATOR);
        return;
    }

    let abc = match abc.as_str() {
        "en" => EN_ABC.chars().collect::<Vec<char>>(),
        "ru" => RU_ABC.chars().collect::<Vec<char>>(),
        _ => abc.chars().collect::<Vec<char>>(),
    };

    let mut new_text = String::new();
    for c in text.to_lowercase().chars() {
        if abc.contains(&c) {
            new_text.push(c);
        }
    }

    let mut entropies: Vec<f64> = Vec::new();
    for i in 1..10 {
        let k_grams_entropy = get_k_grams_entropy(&new_text, i);
        println!("[+] Entropy for {}-gram: {}", i, k_grams_entropy);

        entropies.push(k_grams_entropy);
    }

    if path.len() == 0 {
        show_entropy(entropies, None);
    } else {
        show_entropy(entropies, Some(path));
    }
    println!("{}", SEPARATOR);
}

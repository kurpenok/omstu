use modulo::solve::solve_comparisons_system;

use crate::{
    modules::{
        analysis::{get_frequency, get_most_common_chars},
        decryptor::decrypt,
    },
    EN_ABC, RU_ABC, SEPARATOR,
};

use super::console_read;

fn get_optimal_decrypt_combinations(abc: &Vec<char>, b: usize, d: usize) -> Vec<Vec<usize>> {
    let mut optimal_combinations = Vec::new();

    let optimal_ru_abc = "оеёаитнсрвлкмдпуяызьъбгчйхжюшцщэф"
        .chars()
        .collect::<Vec<char>>();

    for i in 0..optimal_ru_abc.len() {
        for j in 0..i {
            let a = abc
                .iter()
                .position(|&symbol| symbol == optimal_ru_abc[j])
                .unwrap();
            let c = abc
                .iter()
                .position(|&symbol| symbol == optimal_ru_abc[i])
                .unwrap();

            match solve_comparisons_system(a, b, c, d, abc.len()) {
                Some(solutions) => optimal_combinations.push(solutions[0].clone()),
                None => continue,
            }

            let a = abc
                .iter()
                .position(|&symbol| symbol == optimal_ru_abc[i])
                .unwrap();
            let c = abc
                .iter()
                .position(|&symbol| symbol == optimal_ru_abc[j])
                .unwrap();
            match solve_comparisons_system(a, b, c, d, abc.len()) {
                Some(solutions) => optimal_combinations.push(solutions[0].clone()),
                None => continue,
            }
        }
    }

    optimal_combinations
}

pub fn cli_decrypt() {
    let abc = console_read("[>] Enter abc (en/ru): ");
    let text = console_read("[>] Enter text for encryption: ");

    if abc.len() == 0 && text.len() != 0 {
        println!("[-] Incorrect values!");
        println!("{}", SEPARATOR);
        return;
    }

    let optimal_flag = if abc == "ru" { true } else { false };

    let abc = match abc.as_str() {
        "en" => EN_ABC.chars().collect::<Vec<char>>(),
        "ru" => RU_ABC.chars().collect::<Vec<char>>(),
        _ => abc.chars().collect::<Vec<char>>(),
    };

    if optimal_flag {
        let two_most_common_chars = get_most_common_chars(&get_frequency(&text), 2);
        let b = abc
            .iter()
            .position(|&symbol| symbol == two_most_common_chars[0])
            .unwrap();
        let d = abc
            .iter()
            .position(|&symbol| symbol == two_most_common_chars[1])
            .unwrap();

        println!("[+] Enter y if message has been decrypted");
        for combination in get_optimal_decrypt_combinations(&abc, b, d) {
            let decrypted_text = decrypt(&abc, &text, combination[0], combination[1]);
            if decrypted_text.len() == 0 {
                continue;
            }

            let check = format!(
                "[{}, {}] {}: ",
                combination[0], combination[1], decrypted_text
            );
            match console_read(&check).as_str() {
                "y" => {
                    println!("{}", SEPARATOR);
                    return;
                }
                _ => continue,
            }
        }
    }

    for a in 0..abc.len() {
        for b in 0..abc.len() {
            let decrypted_text = decrypt(&abc, &text, a, b);
            if decrypted_text.len() == 0 {
                continue;
            }
            println!("[{}, {}] {}", a, b, decrypted_text);
        }
    }

    println!("{}", SEPARATOR);
}

pub mod cli_entropy;

use std::io::Write;

pub fn console_read(prompt: &str) -> String {
    let mut value = String::new();

    print!("{}", prompt);
    let _ = std::io::stdout().flush();
    std::io::stdin()
        .read_line(&mut value)
        .ok()
        .expect("[-] Failed to read value!");

    value.trim().to_lowercase().to_string()
}

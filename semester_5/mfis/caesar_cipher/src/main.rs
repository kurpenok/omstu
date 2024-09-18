use clap::Parser;
use cli_actions::{cli_decrypt, cli_encrypt};
use cli_args::{Cli, Commands};

mod cli_actions;
mod cli_args;
mod decryptor;
mod encryptor;

fn main() {
    // Usage:
    // cargo run -- encrypt --abc <abc> --message <message> --key <key>
    // cargo run -- decrypt --abc <abc> --message <message> --key <key>
    // cargo run -- decrypt --abc <abc> --message <message>

    let cli = Cli::parse();

    match &cli.command {
        Some(Commands::Encrypt(data)) => cli_encrypt(data),
        Some(Commands::Decrypt(data)) => cli_decrypt(data),
        None => {
            println!("[-] Error reading parameters!");
        }
    }
}

mod analysis;
mod cli_actions;
mod cli_args;
mod decryptor;
mod encryptor;

use clap::Parser;
use cli_actions::{cli_analysis, cli_decrypt, cli_encrypt};
use cli_args::{Cli, Commands};

fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Some(Commands::Encrypt(data)) => cli_encrypt(data),
        Some(Commands::Decrypt(data)) => cli_decrypt(data),
        Some(Commands::Analysis(data)) => cli_analysis(data),
        None => {
            println!("[-] Error reading parameters!");
        }
    }
}
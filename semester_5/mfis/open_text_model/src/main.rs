mod cli_actions;
mod cli_args;
mod k_gram;

use clap::Parser;
use cli_actions::cli_entropy;
use cli_args::{Cli, Commands};

fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Some(Commands::Entropy(data)) => cli_entropy(data),
        None => {
            println!("[-] Error reading parameters!");
        }
    }
}

pub mod comparison;
pub mod gcd;
pub mod invert;
pub mod ops;

mod cli_actions;
mod cli_args;

use clap::Parser;
use cli_actions::{cli_gcd, cli_invert, cli_solve};
use cli_args::{Cli, Commands};

fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Some(Commands::Gcd(data)) => cli_gcd(data),
        Some(Commands::Invert(data)) => cli_invert(data),
        Some(Commands::Solve(data)) => cli_solve(data),
        None => {
            println!("[-] Error reading parameters!");
        }
    }
}

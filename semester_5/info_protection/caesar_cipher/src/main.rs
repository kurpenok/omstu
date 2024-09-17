use clap::Parser;
use cli_args::Cli;

mod cli_args;
mod decryptor;
mod encryptor;

fn main() {
    // Usage:
    // cargo run -- encrypt --abc <abc> --message <message> --key <key>
    // cargo run -- decrypt --abc <abc> --message <message> --key <key>
    // cargo run -- decrypt --abc <abc> --message <message>

    let cli = Cli::parse();
}

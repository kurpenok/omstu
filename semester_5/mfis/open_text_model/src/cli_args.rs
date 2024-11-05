use clap::Args;
use clap::Parser;
use clap::Subcommand;

#[derive(Args)]
pub struct Entropy {
    #[arg(long)]
    pub abc: String,

    #[arg(long)]
    pub message: String,

    #[arg(long)]
    pub path: Option<String>,
}

#[derive(Subcommand)]
pub enum Commands {
    Entropy(Entropy),
}

#[derive(Parser)]
pub struct Cli {
    #[command(subcommand)]
    pub command: Option<Commands>,
}

use clap::Args;
use clap::Parser;
use clap::Subcommand;

#[derive(Args)]
pub struct Encrypt {
    #[arg(long)]
    pub abc: String,

    #[arg(long)]
    pub message: String,

    #[arg(long)]
    pub a: i32,

    #[arg(long)]
    pub b: i32,
}

#[derive(Args)]
pub struct Decrypt {
    #[arg(long)]
    pub abc: String,

    #[arg(long)]
    pub message: String,
}

#[derive(Subcommand)]
pub enum Commands {
    Encrypt(Encrypt),
    Decrypt(Decrypt),
}

#[derive(Parser)]
pub struct Cli {
    #[command(subcommand)]
    pub command: Option<Commands>,
}

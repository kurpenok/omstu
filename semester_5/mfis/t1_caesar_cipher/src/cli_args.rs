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
    pub key: i32,
}

#[derive(Args)]
pub struct Decrypt {
    #[arg(long)]
    pub abc: String,

    #[arg(long)]
    pub message: String,

    #[arg(long)]
    pub key: Option<i32>,
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

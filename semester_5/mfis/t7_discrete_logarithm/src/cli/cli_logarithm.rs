use crate::{cli::console_read, modules::logarithm::find_logarithm, SEPARATOR};

pub fn cli_logarithm() {
    //let a = console_read("[>] Enter number a: ").parse::<usize>();
    //let b = console_read("[>] Enter number b: ").parse::<usize>();
    //let p = console_read("[>] Enter number p: ").parse::<usize>();
    //
    //if a.is_err() || b.is_err() || p.is_err() {
    //    println!("[-] Incorrect values!");
    //    println!("{}", SEPARATOR);
    //    return;
    //}

    //let discrete_logarithm = find_logarithm(a.unwrap(), b.unwrap(), p.unwrap());
    //println!("[+] Discrete logarithm: {}", discrete_logarithm);

    println!("[+] Discrete logarithm: {}", find_logarithm(6, 15, 109));
    println!("{}", SEPARATOR);
}

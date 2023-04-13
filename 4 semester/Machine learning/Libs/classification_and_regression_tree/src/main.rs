mod dataset;
mod criteries;

use dataset::load_data;
use criteries::calc_feature_impurity;

fn main() {
    println!("Hello, world!");

    let data = load_data();
    println!("[+] Loaded data: {:?}", data);

    let impurities: Vec<_> = data.features.iter().map(|feature| calc_feature_impurity(&data, feature)).collect();
    println!("[+] Impurities: {:?}", impurities);
}

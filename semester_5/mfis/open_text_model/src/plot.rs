use plotly::{Plot, Scatter};

pub fn show_entropy(entropies: &Vec<f64>, path: &Option<String>) {
    let mut plot = Plot::new();

    let trace = Scatter::new((1..=entropies.len()).collect(), entropies.to_vec());
    plot.add_trace(trace);

    match path {
        Some(path) => plot.write_html(path),
        None => plot.write_html("entropies.html"),
    }
}

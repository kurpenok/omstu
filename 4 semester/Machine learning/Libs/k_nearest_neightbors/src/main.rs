mod k_nearest_neightbors;

use k_nearest_neightbors::KNearestNeighbors;

fn main() {
    let mut model = KNearestNeighbors::new(5);
    let x_train = vec![
        vec![1.0, 2.0, 3.0],
        vec![4.0, 5.0, 6.0],
        vec![7.0, 8.0, 9.0],
        vec![10.0, 11.0, 12.0],
    ];
    let y_train = vec![0, 1, 2, 3];

    model.fit(x_train, y_train);

    let x_test = vec![0.0, 1.0, 2.0];
    let predicted_label = model.predict(&x_test);
    println!("Predicted label: {}", predicted_label);
}

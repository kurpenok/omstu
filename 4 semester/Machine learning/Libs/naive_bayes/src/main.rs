mod naive_bayes;

use naive_bayes::GaussianNB;

fn main() {
    // Create a GaussianNB classifier
    let mut clf = GaussianNB::new();
    
    // Training data
    let X_train = vec![
        vec![1.0, 2.0],
        vec![2.0, 1.0],
        vec![3.0, 4.0],
        vec![4.0, 3.0],
    ];
    let y_train = vec![
        "A".to_string(),
        "A".to_string(),
        "B".to_string(),
        "B".to_string(),
    ];
    
    // Fit the classifier to the training data
    clf.fit(X_train, y_train);
    
    // Predict the class of new observations
    let X_test = vec![
        vec![1.5, 2.5],
        vec![3.5, 3.5],
    ];
    let y_pred = clf.predict(X_test);
    
    // Print the predicted classes
    for class in y_pred {
        println!("{}", class);
    }
}

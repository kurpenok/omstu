#[derive(Debug)]
pub struct Dataset {
    pub features: Vec<String>,
    pub labels: Vec<String>,
    pub objects: Vec<Vec<f64>>,
    pub classes: Vec<String>,
}

impl Dataset {
    pub fn new(features: Vec<String>, labels: Vec<String>, objects: Vec<Vec<f64>>, classes: Vec<String>) -> Self {
        Dataset {features, labels, objects, classes}
    }
}

pub fn load_data() -> Dataset {
    let features = vec!["Feature1".to_string(), "Feature2".to_string(), "Feature3".to_string()];
    let labels = vec!["Label".to_string()];
    let objects = vec![
        vec![1.0, 2.0, 3.0],
        vec![2.0, 3.0, 4.0],
        vec![3.0, 4.0, 5.0],
        vec![4.0, 5.0, 6.0],
    ];
    let classes = vec!["Class1".to_string(), "Class2".to_string(), "Class3".to_string()];

    Dataset::new(features, labels, objects, classes)
}

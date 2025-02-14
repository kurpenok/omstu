pub fn numerical_gradient<F>(f: F, x: &Vec<f64>, h: f64) -> Vec<f64>
where
    F: Fn(&Vec<f64>) -> f64,
{
    // Определяем размерность вектора x
    let n = x.len();

    // Инициализируем вектор градиента нулями
    let mut grad = vec![0.0; n];

    // Для каждой координаты вычисляем частную производную
    for i in 0..n {
        // Клонируем точку x для вычисления x+h
        let mut x_forward = x.clone();

        // Клонируем точку x для вычисления x-h
        let mut x_backward = x.clone();

        // Прибавляем малый шаг h к i-й координате
        x_forward[i] += h;

        // Вычитаем малый шаг h от i-й координаты
        x_backward[i] -= h;

        // Вычисляем центральную разность для компоненты i
        grad[i] = (f(&x_forward) - f(&x_backward)) / (2.0 * h);
    }

    // Возвращаем вычисленный градиент
    grad
}

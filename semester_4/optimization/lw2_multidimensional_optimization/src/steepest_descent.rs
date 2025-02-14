use crate::{golden_ratio::golden_ratio_search, gradient::numerical_gradient};

pub fn steepest_descent<F>(
    f: F,
    x_0: Vec<f64>,
    eps: f64,
    max_iter: usize,
    grad_h: f64,
) -> (Vec<f64>, f64)
where
    F: Fn(&Vec<f64>) -> f64,
{
    // Инициализируем текущую точку начальным приближением
    let mut x = x_0;

    // Основной цикл метода, выполняющий не более max_iter итераций
    for _ in 0..max_iter {
        // Вычисляем градиент функции в текущей точке x
        let grad = numerical_gradient(&f, &x, grad_h);

        // Вычисляем евклидову норму градиента
        let norm_grad = grad.iter().map(|&val| val * val).sum::<f64>().sqrt();

        // Если норма градиента меньше заданного порога eps, считаем,
        // что достигли точки минимума и прерываем цикл
        if norm_grad < eps {
            break;
        }

        // Определяем направление спуска как противоположное градиенту
        let direction: Vec<f64> = grad.iter().map(|&val| -val).collect();

        // Определяем одномерную функцию для линийного поиска:
        // f1d(alpha) = f(x + alpha * direction)
        let f1d = |alpha: f64| {
            // Для каждого элемента x вычисляем x_new = x + alpha * direction
            let x_new: Vec<f64> = x
                .iter()
                .zip(direction.iter())
                .map(|(&xi, &di)| xi + alpha * di)
                .collect();

            // Возвращаем значение функции в новой точке
            f(&x_new)
        };

        // Проводим одномерный поиск минимума вдоль направления спуска с помощью метода золотого сечения
        // Интервал поиска выбран произвольно, например, от -1 до 1
        let (alpha_min, _) = golden_ratio_search(f1d, -1.0, 1.0, eps);

        // Обновляем текущую точку: x = x + alpha_min * direction
        x = x
            .iter()
            .zip(direction.iter())
            .map(|(&xi, &di)| xi + alpha_min * di)
            .collect();
    }

    // Возвращаем найденное приближение минимума
    (x.clone(), f(&x))
}

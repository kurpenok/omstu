def flow_shop(jobs):
    """
    Вызовите функцию flow_shop(jobs), и она вернет время завершения на последней машине для последней задачи,
    а также списки времени начала и окончания работы каждой задачи на каждой машине.
    """

    num_jobs = len(jobs)
    num_machines = len(jobs[0])
    start_times = [[0] * num_machines for _ in range(num_jobs)]
    end_times = [[0] * num_machines for _ in range(num_jobs)]

    # Вычисляем время начала и окончания работы на каждой машине для каждой задачи
    for j in range(num_jobs):
        for m in range(num_machines):
            if j == 0 and m == 0:
                start_times[j][m] = 0
            elif j == 0:
                start_times[j][m] = end_times[j][m - 1]
            elif m == 0:
                start_times[j][m] = end_times[j - 1][m]
            else:
                start_times[j][m] = max(end_times[j][m - 1], end_times[j - 1][m])

            end_times[j][m] = start_times[j][m] + jobs[j][m]

    # Вычисляем время завершения на последней машине для последней задачи
    makespan = end_times[num_jobs - 1][num_machines - 1]

    return makespan, start_times, end_times

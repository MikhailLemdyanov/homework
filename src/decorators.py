import time
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """
    Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки
    """

    def my_decorator(func: Callable) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()

            try:
                result = func(*args, **kwargs)
                stop_time = time.time()
                work_time = stop_time - start_time

                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"The result of working {func.__name__}: {result} - ОК\n")
                        file.write(f"Working time is: {work_time:.10f}\n")

                else:
                    print(f"The result of working {func.__name__}: {result} - ОК\n")
                    print(f"Working time is: {work_time:.10f}\n")

            except Exception as error:
                stop_time = time.time()
                work_time = stop_time - start_time
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"Function: {func.__name__} - ERROR: {error} with inputs: {args}, {kwargs}\n")
                        file.write(f"Working time is: {work_time:.10f}\n")

                else:
                    print(f"Function: {func.__name__} - ERROR: {error} with inputs: {args}, {kwargs}\n")

                result = "Error occurred\n"

            return result

        return wrapper

    return my_decorator


# @log(filename="../logs/mylog.txt")
# def my_function(x: int, y: int) -> int:
#     return x + y
#
#
# my_function("3", 2)

from functools import wraps
from time import time
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки"""

    def my_decorator(func: Callable) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time()
                work_time = end_time - start_time
                log_message = f"Result of {func.__name__}: {result} - OK. Working time is {work_time:.10f}\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)

                return result
            except Exception as error:
                error_message = f"{func.__name__} error: {error.__class__.__name__}. Inputs {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(error_message)
                else:
                    print(error_message)
                raise error

        return wrapper

    return my_decorator


# @log(filename="../logs/mylog.txt")
# def my_function(x: int, y: int) -> int:
#     return x + y
#
#
# my_function(3, 2)

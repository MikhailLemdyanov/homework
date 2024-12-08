from typing import Callable

from src.decorators import log


def test_log() -> None:
    @log(None)
    def my_test_func(a: int, b: int) -> int:
        return a + b

    assert my_test_func(1, 2) == 3
    assert my_test_func("a", 2) == "Error occurred\n"


def test_log_capsys(capsys: Callable) -> None:
    @log()
    def my_test_func(a: int, b: int) -> int:
        return a + b

    my_test_func(1, 2)

    captured = capsys.readouterr()
    assert "The result of working my_test_func: 3 - ОК" in captured.out
    assert "Working time is:" in captured.out


def test_log_invalid(capsys: Callable) -> None:
    @log()
    def my_test_func(a: int, b: int) -> int:
        return a + b

    my_test_func("a", 2)

    captured = capsys.readouterr()
    assert (
        captured.out
        == """my_test_func - ERROR: can only concatenate str (not "int") to str with inputs: ('a', 2), {}\n\n"""
    )

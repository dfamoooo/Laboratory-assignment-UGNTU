"""Интеграционные тесты CLI через subprocess."""
import subprocess
import sys
from pathlib import Path
import pytest

# Корень проекта — папка, где лежит main.py
ROOT = Path(__file__).resolve().parent.parent
MAIN = ROOT / "main.py"


def run_cli(*args: str) -> subprocess.CompletedProcess:
    """Запустить main.py с аргументами и вернуть результат."""
    return subprocess.run(
        [sys.executable, str(MAIN), *args],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )


class TestCLIGenerate:
    def test_generate_prints_numbers(self):
        res = run_cli("--kind", "random", "--n", "10", "--seed", "42")
        assert res.returncode == 0
        assert len(res.stdout.strip().splitlines()) >= 10

    def test_invalid_n_returns_error(self):
        res = run_cli("--kind", "random", "--n", "0")
        assert res.returncode != 0
        assert "положительным целым" in res.stderr


class TestCLIIO:
    def test_save_and_load_roundtrip(self, tmp_path):
        path = tmp_path / "series.json"
        res1 = run_cli("--kind", "sine", "--n", "20", "--seed", "1", "--save", str(path))
        assert res1.returncode == 0
        assert path.exists()

        res2 = run_cli("--load", str(path))
        assert res2.returncode == 0


class TestCLIBenchmark:
    def test_benchmark_flag(self):
        res = run_cli("--kind", "random", "--n", "100", "--benchmark")
        assert res.returncode == 0
        assert "list" in res.stdout or "deque" in res.stdout
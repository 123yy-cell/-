import sys

import pytest

from greetlab.cli import main


def test_normal_name(capsys):
    sys.argv = ["sdt-greet", "--name", "test"]
    main()
    captured = capsys.readouterr()
    assert "Hello, test!" in captured.out


def test_blank_name_exit_code():
    sys.argv = ["sdt-greet", "--name", "   "]
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 2

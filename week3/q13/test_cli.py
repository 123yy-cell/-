import pytest
from greetlab.cli import main
import sys

def test_normal_name(capsys):
    # 正常名称测试
    sys.argv = ["sdt-greet", "--name", "test"]
    main()
    captured = capsys.readouterr()
    assert "Hello, test!" in captured.out

def test_blank_name_exit_code():
    # 全空白名称测试：应抛出SystemExit且退出码为2
    sys.argv = ["sdt-greet", "--name", "   "]
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 2

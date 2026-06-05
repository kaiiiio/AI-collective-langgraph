from tools.lab_runner import LabCommandError, build_docker_command, module_table


def test_builds_short_module_command() -> None:
    command = build_docker_command(["module", "1"])

    assert command == [
        "docker",
        "compose",
        "run",
        "--rm",
        "lab",
        "python",
        "modules/01_hello_graph/main.py",
    ]


def test_accepts_bare_module_number() -> None:
    command = build_docker_command(["10"])

    assert command[-1] == "modules/10_capstone_project/main.py"


def test_builds_test_command() -> None:
    command = build_docker_command(["test"])

    assert command == ["docker", "compose", "run", "--rm", "test"]


def test_rejects_unknown_module() -> None:
    try:
        build_docker_command(["module", "99"])
    except LabCommandError as error:
        assert "Unknown module: 99" in str(error)
    else:
        raise AssertionError("Expected LabCommandError")


def test_module_table_marks_inductive_status() -> None:
    rows = module_table()

    assert rows[0]["number"] == "1"
    assert rows[0]["inductive"] == "Yes"
    assert rows[-1]["number"] == "10"
    assert rows[-1]["inductive"] == "Partly"

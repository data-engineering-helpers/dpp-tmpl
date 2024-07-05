
import pytest

def test_bake_project(cookies):
    result = cookies.bake(extra_context={"repo_name": "my-team-my-project"})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "my-team-my-project-depl"
    assert result.project_path.is_dir()



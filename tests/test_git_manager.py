import unittest
from unittest.mock import patch, Mock

from src.git_manager import get_current_commit


class TestGitManager(unittest.TestCase):

    @patch("src.git_manager.subprocess.run")
    def test_get_current_commit(self, mock_run):
        mock_run.return_value = Mock(stdout="658abc5\n")

        commit_id = get_current_commit()

        self.assertEqual(commit_id, "658abc5")


if __name__ == "__main__":
    unittest.main()
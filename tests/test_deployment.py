import unittest
from unittest.mock import patch, MagicMock

from src.deployment import record_deployment


class TestDeployment(unittest.TestCase):

    @patch("src.deployment.get_db_connection")
    @patch("src.deployment.get_current_commit")
    def test_record_deployment(self, mock_commit, mock_db):

        mock_commit.return_value = "658abc5"

        mock_connection = MagicMock()
        mock_cursor = MagicMock()

        mock_db.return_value = mock_connection
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        record_deployment("Worker-Finder", "1.0.2", "SUCCESS")

        mock_cursor.execute.assert_called_once()

        mock_connection.commit.assert_called_once()
        mock_connection.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
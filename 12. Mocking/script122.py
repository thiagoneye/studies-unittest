import random
from unittest.mock import Mock, patch


if __name__ == "__main__":
    techs = ["python", "sql", "java", "aws", "c++"]

    with patch("random.choice", return_value="aws"):
        print(random.choice())

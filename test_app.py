import subprocess
import sys

result = subprocess.run(
    [sys.executable, "app.py"],
    capture_output=True,
    text=True
)

assert result.stdout.strip() == "hello devops!"

print("test passed")

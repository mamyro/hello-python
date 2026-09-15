import subprocess

result = subprocess.run(
    ["python3", "app.py"],
    capture_output=True,
    text=True
)

assert result.stdout.strip() == "hello devops!"

print("test passed")

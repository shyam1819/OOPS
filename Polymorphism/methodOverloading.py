import os
class SmartPath:
    def __init__(self, path):
        self.path = path

    def __truediv__(self, other):
        """Overloads the / operator to join paths"""
        import os
        # Logic: Join the current path with the next string
        new_path = os.path.join(self.path, other)
        return SmartPath(new_path)

    def __repr__(self):
        return f"Path: {self.path}"

# Usage:
root = SmartPath("/home/user")
config_file = root / "projects" / "app" / "config.yaml"

print(config_file) 
# Output: Path: /home/user/projects/app/config.yaml

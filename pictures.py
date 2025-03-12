#!/usr/bin/python3
class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = {}

    def add_directory(self, path, name):
        node = self._traverse(path)
        if node is not None and name not in node.subdirectories:
            node.subdirectories[name] = Directory(name)
        else:
            print(f"Cannot add directory: Path '{'/'.join(path)}' not found or directory '{name}' already exists.")

    def delete_directory(self, path, name):
        node = self._traverse(path)
        if node is not None and name in node.subdirectories:
            del node.subdirectories[name]
        else:
            print(f"Cannot delete directory: Path '{'/'.join(path)}' not found or directory '{name}' does not exist.")

    def _traverse(self, path):
        node = self
        for dir_name in path:
            if dir_name in node.subdirectories:
                node = node.subdirectories[dir_name]
            else:
                return None
        return node

    def display(self, level=0):
        print("  " * level + self.name)
        for subdir in sorted(self.subdirectories):
            self.subdirectories[subdir].display(level + 1)

# Example usage
tree = Directory("Pictures")
tree.add_directory([], "Saved Pictures")
tree.add_directory(["Saved Pictures"], "Web Images")
tree.add_directory(["Saved Pictures", "Web Images"], "Chrome")
tree.add_directory(["Saved Pictures", "Web Images"], "Opera")
tree.add_directory(["Saved Pictures", "Web Images"], "Firefox")
tree.add_directory([], "Screenshots")
tree.add_directory([], "Camera Roll")
tree.add_directory(["Camera Roll"], "2025")
tree.add_directory(["Camera Roll"], "2024")
tree.add_directory(["Camera Roll"], "2023")

tree.display()

print("\nDeleting 'Web Images'...")
tree.delete_directory(["Saved Pictures"], "Web Images")
tree.display()

# TODO: Add code here
class TODO:
    def __init__(self, code_id: int, title: str, description: str, completed: bool = False, tags: list[str] = None):
        self.code_id = code_id
        self.title = title
        self.description = description
        self.completed = completed
        self.tags = tags if tags is not None else []

    def __str__(self):
        return f"TODO(code_id={self.code_id}, title='{self.title}', description='{self.description}', completed={self.completed}, tags={self.tags})"

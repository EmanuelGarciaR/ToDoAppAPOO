# TODO: Add code here
class TODO:
    def __init__(self, code_id: int, title: str, description: str, completed: bool = False, tags: list[str] = None):
        self.code_id = code_id
        self.title = title
        self.description = description
        self.completed = completed
        self.tags = tags if tags is not None else []

    def __str__(self):
        return f"{self.code_id}-{self.title}"

    def mark_completed(self):
        self.completed = True

    def add_tag(self, new_tag: str):
        if new_tag not in self.tags:
            self.tags.append(new_tag)
            # [new_tag if != tag for tag in self.tags]


class TodoBook:
    def __init__(self, todos: dict[int, TODO] = None):
        self.todos = todos if todos is not None else {}

    def add_todo(self, title: str, description: str) -> int:
        new_id = len(self.todos) + 1

        new_todo = TODO(code_id=new_id, title=title, description=description)

        # Agregar el objeto TODO al diccionario 'todos' usando el ID como clave
        self.todos[new_id] = new_todo

        return new_id

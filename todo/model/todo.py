# TODO: Add code here
class Todo:
    def __init__(self, code_id: int, title: str, description: str, completed: bool = False, tags: list[str] = None):
        self.code_id = code_id
        self.title = title
        self.description = description
        self.completed = completed
        self.tags = tags if tags is not None else []

    def __str__(self):
        return f"{self.code_id} - {self.title}"

    def mark_completed(self):
        self.completed = True

    def add_tag(self, new_tag: str):
        if new_tag not in self.tags:
            self.tags.append(new_tag)
            # [new_tag if != tag for tag in self.tags]


class TodoBook:
    def __init__(self, todos: dict[int, Todo] = None):
        self.todos = todos if todos is not None else {}

    def add_todo(self, title: str, description: str) -> int:
        new_id = len(self.todos) + 1

        new_todo = Todo(code_id=new_id, title=title, description=description)

        # Agregar el objeto TODO al diccionario 'todos' usando el ID como clave
        self.todos[new_id] = new_todo

        return new_id

    def pending_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if not todo.completed]

    def completed_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if todo.completed]

    def tags_todo_count(self) -> dict[str, int]:
        tag_count = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag in tag_count:
                    tag_count[tag] += 1
                else:
                    tag_count[tag] = 1
        return tag_count

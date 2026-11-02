from fastapi import APIRouter, HTTPException, Path, status

from model import Todo, TodoItem, TodoItems


todo_router = APIRouter()
todo_list: list[Todo] = []


def find_todo(todo_id: int) -> Todo:
    for todo in todo_list:
        if todo.id == todo_id:
            return todo

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача с ID {todo_id} не найдена."
    )


@todo_router.post("/todo", status_code=status.HTTP_201_CREATED)
async def add_todo(todo: Todo) -> dict:
    if any(existing.id == todo.id for existing in todo_list):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Задача с ID {todo.id} уже существует."
        )

    todo_list.append(todo)

    return {
        "message": "Задача успешно добавлена."
    }


@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    todo_id: int = Path(..., gt=0, title="Идентификатор задачи")
) -> dict:
    todo = find_todo(todo_id)

    return {
        "todo": todo
    }


@todo_router.put("/todo/{todo_id}")
async def update_todo(
    todo_data: TodoItem,
    todo_id: int = Path(..., gt=0, title="Идентификатор задачи")
) -> dict:
    todo = find_todo(todo_id)
    todo.item = todo_data.item

    return {
        "message": "Задача успешно обновлена."
    }


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(
    todo_id: int = Path(..., gt=0, title="Идентификатор задачи")
) -> dict:
    todo = find_todo(todo_id)
    todo_list.remove(todo)

    return {
        "message": "Задача успешно удалена."
    }


@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()

    return {
        "message": "Все задачи успешно удалены."
    }

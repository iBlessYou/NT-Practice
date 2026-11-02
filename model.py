from pydantic import BaseModel, ConfigDict, Field


class Todo(BaseModel):
    id: int = Field(gt=0)
    item: str = Field(min_length=1)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "item": "Проверить сетевое оборудование"
            }
        }
    )


class TodoItem(BaseModel):
    item: str = Field(min_length=1)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "item": "Обновить сведения о коммутаторе"
            }
        }
    )


class TodoItems(BaseModel):
    todos: list[TodoItem]

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "todos": [
                    {"item": "Проверить сетевое оборудование"},
                    {"item": "Обновить сведения о коммутаторе"}
                ]
            }
        }
    )

type ToDoListProps={
    tdItems:string[]
}

export default function ToDoList({tdItems}:ToDoListProps):JSX.Element{
    return (
        <>
        <p>{tdItems}</p>
        </>
    )
}
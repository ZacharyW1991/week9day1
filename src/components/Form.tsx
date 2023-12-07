type ToDoProps={
    todo:string
}

    export default function ToDo({todo}:ToDoProps):JSX.Element{
        return (
            <>
            <p>{todo}</p>
            </>
        )
    }
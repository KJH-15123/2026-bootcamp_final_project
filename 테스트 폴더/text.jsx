const text = () => {

    //등록기능 
    const onSubmit = (e) => {
        e.preventDefault();
    };

    //삭제기능
    const onDelete = (e) => {
        e.preventDefault();
    };

    return (
        <div>
            <h1>text</h1>
            <form onSubmit={onSubmit}>
                <input type="text" />
                <button type="submit">등록</button>
            </form>
            <button onClick={onDelete}>삭제</button>
        </div>
    );
};
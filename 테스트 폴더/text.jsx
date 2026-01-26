const text = () => {

    //등록기능 
    const onSubmit = (e) => {
        e.preventDefault();
    };

    //삭제기능
    const onDelete = (e) => {
        e.preventDefault();
    };

    //버튼 테스트
    const onTest = (e) => {
        e.preventDefault();
    };

    //수정 기능
    const onUpdate = (e) => {
        e.preventDefault();
    };

    return (
        <div>
            <h1>text</h1>
            <form onSubmit={onSubmit}>
                <input type="text" />
                <button type="submit">등록</button>
            </form>
            <button onClick={onUpdate}>수정</button>
            <button onClick={onDelete}>삭제</button>
            <button onClick={onTest}>버튼 테스트</button>
        </div>
    );
};
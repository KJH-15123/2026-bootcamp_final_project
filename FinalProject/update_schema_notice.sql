-- [추가 패치] CHAT_ROOM 테이블에 공지사항 관련 컬럼 추가
-- 공지 기능을 사용하기 위해 누락된 컬럼들을 추가합니다.

-- 1. 공지 내용 (긴 텍스트 가능)
ALTER TABLE CHAT_ROOM ADD NOTICE_CONTENT CLOB;

-- 2. 공지로 등록된 원본 메시지 ID
ALTER TABLE CHAT_ROOM ADD NOTICE_MESSAGE_ID NUMBER;

-- 3. 공지를 등록한 사람 ID
ALTER TABLE CHAT_ROOM ADD NOTICE_SENDER_ID NUMBER;

-- 4. (선택사항) 채팅방 기본 이미지 컬럼이 없다면 추가
ALTER TABLE CHAT_ROOM ADD DEFAULT_ROOM_IMAGE VARCHAR2(255);

COMMIT;

-- 확인용 조회
-- SELECT * FROM CHAT_ROOM;

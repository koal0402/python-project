import anthropic

# 1단계에서 발급받은 본인의 실제 sk-ant-... 키를 아래 따옴표 안에 넣으세요!
ANTHROPIC_API_KEY = "여기에_발급받은_API_키를_넣으세요"

# 클로드 연결 시작
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

# 클로드에게 질문 던지기
message = client.messages.create(
    model="claude-3-5-sonnet-20240620", # 사용할 클로드 모델
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "파이썬과 클로드 연결에 성공했어! 축하 메시지 한 줄만 보내줘."}
    ]
)

# 클로드의 답변을 화면에 출력
print(message.content[0].text)
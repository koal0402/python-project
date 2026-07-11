import os
import anthropic
from dotenv import load_dotenv

# 1. 이 코드가 실행되면서 방금 만든 .env 파일의 키를 컴퓨터 시스템에 등록합니다.
load_dotenv()

# 2. os.environ.get 기능으로 안전하게 키를 가져옵니다.
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# 아래에 기존 대화 내용 코드(messages=[...])를 이어서 쓰시면 됩니다!
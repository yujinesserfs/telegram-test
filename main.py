import os
import requests

# Telegram Bot 토큰과 챗 ID
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID_1 = os.getenv("TELEGRAM_CHAT_ID_1")
CHAT_ID_2 = os.getenv("TELEGRAM_CHAT_ID_2")

# 디버그: 환경변수 값 확인
print("DEBUG: BOT_TOKEN =", BOT_TOKEN)
print("DEBUG: CHAT_ID_1 =", CHAT_ID_1)
print("DEBUG: CHAT_ID_2 =", CHAT_ID_2)

CHAT_IDS = [cid for cid in [CHAT_ID_1, CHAT_ID_2] if cid]

if not CHAT_IDS:
    print("❌ 전송할 CHAT_ID 없음. 시크릿 확인 필요.")
else:
    for cid in CHAT_IDS:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        try:
            res = requests.post(url, data={"chat_id": cid, "text": "💡 테스트 메시지: GitHub Actions Telegram 확인"})
            print(f"📨 전송 → {cid} / status {res.status_code} / response: {res.text}")
        except Exception as e:
            print(f"❌ 전송 실패 → {cid}: {e}")

import streamlit as st
from PIL import Image
import pytesseract
import requests
import json

# Google Apps Script WebアプリケーションのエンドポイントURL
google_apps_script_url = "https://script.google.com/macros/s/AKfycbwxroUDSkrRGYzWUGfL_CelHM8Wc04S4CqmO-1le-5F2u-_u5HsGvYRQzMNp7QxXLVB/exec"

def perform_ocr(image):
    # 画像から英語テキストを抽出する関数
    english_text = pytesseract.image_to_string(image, lang='eng')
    return english_text

def translate_text_with_google_apps_script(text, source_lang='en', target_lang='ja'):
    # Google Apps Script Webアプリケーションにテキストと言語情報を送信して翻訳されたテキストを取得
    payload = {'text': text, 'source': source_lang, 'target': target_lang}
    response2 = requests.get(google_apps_script_url, params=payload)
    print(response2.text())
    response_json = response2.text()
    # 翻訳されたテキストの取得
    translated_text = response_json['text']

    # 翻訳されたテキストを表示
    print("Translated Text:", translated_text)

    return translated_text


"""
    # JSON形式のレスポンスを解析
    try:
        data = json.loads(response.text)
        translated_text = data.get('translatedText', '')
    except json.JSONDecodeError:
        translated_text = 'Error decoding JSON response'
"""

#    return translated_text

def main():
    st.title("画像文字認識＆翻訳アプリ")

    # 画像のアップロード
    uploaded_image = st.file_uploader("画像をアップロードしてください", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # アップロードされた画像を表示
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # OCRの実行
        english_text = perform_ocr(image)

        # 認識された英語のテキストを表示
        st.subheader("認識された英語のテキスト:")
        st.write(english_text)

        #翻訳元言語と翻訳後の言語を指定してGoogle Apps Script Webアプリケーションを使用して翻訳
        source_lang = 'en'
        target_lang = 'ja'
        japanese_text = translate_text_with_google_apps_script(english_text, source_lang, target_lang)

        # 翻訳された日本語のテキストを表示
        st.subheader("翻訳された日本語のテキスト:")
        st.write(japanese_text)

if __name__ == "__main__":
    main()

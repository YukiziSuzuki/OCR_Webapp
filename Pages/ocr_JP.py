import streamlit as st
from PIL import Image
import pytesseract

def perform_ocr(image):
    # 画像から日本語テキストを抽出する関数
    text = pytesseract.image_to_string(image, lang='jpn')
    return text

def main():
    st.title("画像文字認識アプリ＿日本語")

    # 画像のアップロード
    uploaded_image = st.file_uploader("画像をアップロードしてください", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # アップロードされた画像を表示
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # OCRの実行
        text = perform_ocr(image)

        # 認識されたテキストを表示
        st.subheader("認識されたテキスト:")
        st.write(text)

if __name__ == "__main__":
    main()

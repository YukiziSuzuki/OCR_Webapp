import streamlit as st

def main():
    st.title("画像文字認識アプリ")

    # ここにホーム画面のコンテンツを追加
    st.write("ようこそ！このアプリは画像文字認識アプリです")
    st.write("アップロードされた画像から文字を読み取り表示することが出来ます")
    st.write("日本語と英語の二言語を読み取ることが出来ます")
    st.write("左のサイドバーからどの言語を読み取りたいのか選択してください")

if __name__ == "__main__":
    main()
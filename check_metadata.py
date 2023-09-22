import streamlit as st
from PIL import Image

def check_metadata(uploaded_images):
    results = {}
    for img_name, img_file in uploaded_images.items():
        with Image.open(img_file) as img:
            if img.info:
                results[img_name] = "メタデータが存在します。"
            else:
                results[img_name] = "メタデータが存在しません。"
    return results

def main():
    st.title("PNGメタデータチェッカー")
    
    uploaded_files = st.file_uploader("複数のPNG画像をアップロードしてください", type="png", accept_multiple_files=True)
    
    if uploaded_files:
        results = check_metadata({file.name: file for file in uploaded_files})
        for img_name, result in results.items():
            st.write(f"{img_name}: {result}")

if __name__ == "__main__":
    main()

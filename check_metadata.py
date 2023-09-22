import streamlit as st
from PIL import Image

def check_metadata(uploaded_images):
    results = {}
    all_without_metadata = True
    for img_name, img_file in uploaded_images.items():
        with Image.open(img_file) as img:
            if img.info:
                results[img_name] = "**メタデータが存在します。**"
                all_without_metadata = False
            else:
                results[img_name] = "メタデータが存在しません。"
    return results, all_without_metadata

def main():
    st.title("PNGメタデータチェッカー")
    
    uploaded_files = st.file_uploader("複数のPNG画像をアップロードしてください", type="png", accept_multiple_files=True)
    
    if uploaded_files:
        results, all_without_metadata = check_metadata({file.name: file for file in uploaded_files})
        
        if all_without_metadata:
            st.write("すべての画像にメタデータが存在しません")
        else:
            st.markdown("**一部の画像にメタデータが存在します！**")
        
        for img_name, result in results.items():
            st.markdown(f"{img_name}: {result}")

if __name__ == "__main__":
    main()

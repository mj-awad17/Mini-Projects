# libraries
import streamlit as st
from rembg import remove
from PIL import Image
import io

# title-app
st.title("Background Remover App using StreamLit")
# upload-file
upload = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])

if upload is not None:
    try:
        # open `upload-file` where open is the rembg weidget
        image = Image.open(upload)
        # captioning the uploaded-image
        st.image(image, caption="Original Image", width=300)
        
        # remove the BG by using remove()``
        image_removeBG = remove(image)
        
        # resizing the image
        resize_image = image_removeBG.resize((500, 500))
        
        # captioning the resizing image which is display on the screen
        st.image(resize_image, caption="Background remove Image", width=300)
        
        # BytesIO class from the io module which creates a in-memory file-like object.
        image_bt_arry =io.BytesIO() 
        
        # saves the resized image with the background removed to the in-memory file-like object
        resize_image.save(image_bt_arry, format='PNG')
        
        # retrieves the actual byte data of the saved image from the in-memory file-like object.
        image_bt_arry = image_bt_arry.getvalue()
        
        # download-button removebg-image to local machine
        st.download_button(
            label="Download Image",
            data=image_bt_arry,
            file_name='bg-remover-image.png',
            mime='image/png'
        )
        
    except Exception as e:
        st.error(f"Something went wrong! {e}")
        
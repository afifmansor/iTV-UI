import streamlit as st
import time

def main():
    # Set a background image
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url('loading_image-min.jpg');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Display the enter button
    enter_button = st.button("Enter")
    
    if enter_button:
        # Show loading interface
        loading_placeholder = st.empty()
        loading_text = loading_placeholder.text("Loading...")
        loading_progress = loading_placeholder.progress(0)
        
        for percent_complete in range(101):
            loading_text.text(f"Loading... {percent_complete}%")
            loading_progress.progress(percent_complete)
            
            # Gradually brighten the background image
            st.markdown(
                f"""
                <style>
                .reportview-container {{
                    filter: brightness({percent_complete}%);
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
            
            # Sleep for a short duration to simulate loading time
            time.sleep(0.01)
        
        # Clear loading interface
        loading_placeholder.empty()
        
        # Display the loaded content
        st.write("Loading complete! Here's the content.")
        st.image("loading_image-min.jpg", caption="Loaded Image")
        

if __name__ == "__main__":
    main()

import streamlit as st
import os, urllib
import numpy as np
import pandas as pd
import altair as alt

def main() :
    readme_text = st.markdown(get_file_content_as_string("instructions.md"))

    st.sidebar.title("What to do")
    # app_mode = st.sidebar.selectbox("Choose the app mode",
    #     ["Show instructions", "Run the app", "Show the source code"])
    # if app_mode == "Show instructions":
    #     st.sidebar.success('To continue select "Run the app".')
    # elif app_mode == "Show the source code":
    #     readme_text.empty()
    #     st.code(get_file_content_as_string("streamlit_app.py"))
    # elif app_mode == "Run the app":
    #     readme_text.empty()
    #     run_the_app()    

def get_file_content_as_string(path):
    url = 'https://raw.githubusercontent.com/MunSunouk/demo_streamlit/master' + path
    response = urllib.request.urlopen(url)

    return response.read().decode("utf-8")

# def run_the_app():
#     # To make Streamlit fast, st.cache allows us to reuse computation across runs.
#     # In this common pattern, we download data from an endpoint only once.

#     # Uncomment these lines to peek at these DataFrames.
#     # st.write('## Metadata', metadata[:1000], '## Summary', summary[:1000])



#     # Load the image from colab
#     image_url = os.path.join(DATA_URL_ROOT, selected_frame)
#     image = load_image(image_url)

#     # Add boxes for objects on the image. These are the boxes for the ground image.
#     boxes = metadata[metadata.frame == selected_frame].drop(columns=["frame"])
#     draw_image_with_boxes(image, boxes, "Ground Truth",
#         "**Human-annotated data** (frame `%i`)" % selected_frame_index)

#     # Get the boxes for the objects detected by YOLO by running the YOLO model.
#     yolo_boxes = yolo_v3(image, confidence_threshold, overlap_threshold)
#     draw_image_with_boxes(image, yolo_boxes, "Real-time Computer Vision",
#         "**YOLO v3 Model** (overlap `%3.1f`) (confidence `%3.1f`)" % (overlap_threshold, confidence_threshold))

# def frame_selector_ui(summary):
#     st.sidebar.markdown("# Frame")

#     # The user can pick which type of object to search for.
#     object_type = st.sidebar.selectbox("Search for which objects?", summary.columns, 2)

#     # The user can select a range for how many of the selected objecgt should be present.
#     min_elts, max_elts = st.sidebar.slider("How many %ss (select a range)?" % object_type, 0, 25, [10, 20])
#     selected_frames = get_selected_frames(summary, object_type, min_elts, max_elts)
#     if len(selected_frames) < 1:
#         return None, None

#     # Choose a frame out of the selected frames.
#     selected_frame_index = st.sidebar.slider("Choose a frame (index)", 0, len(selected_frames) - 1, 0)

#     # Draw an altair chart in the sidebar with information on the frame.
#     objects_per_frame = summary.loc[selected_frames, object_type].reset_index(drop=True).reset_index()
#     chart = alt.Chart(objects_per_frame, height=120).mark_area().encode(
#         alt.X("index:Q", scale=alt.Scale(nice=False)),
#         alt.Y("%s:Q" % object_type))
#     selected_frame_df = pd.DataFrame({"selected_frame": [selected_frame_index]})
#     vline = alt.Chart(selected_frame_df).mark_rule(color="red").encode(x = "selected_frame")
#     st.sidebar.altair_chart(alt.layer(chart, vline))

#     selected_frame = selected_frames[selected_frame_index]
#     return selected_frame_index, selected_frame

# DATA_URL_ROOT = "https://drive.google.com/drive/folders/1u8YIkluNB2V8_UzbfY0KrI6FCnH8xB9f?usp=sharing"


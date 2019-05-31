from moviepy.editor import VideoClip
from PIL import Image
import numpy as np

def generate_animation():

def make_frame(t):
    """ returns an image of the frame at time t """
    # ... create the frame with any library
    return ani[t]# (Height x Width x 3) Numpy array

def numpy2pil(np_array: np.ndarray) -> Image:
    """
    Convert an HxWx3 numpy array into an RGB Image
    """

    assert_msg = 'Input shall be a HxWx3 ndarray'
    assert isinstance(np_array, np.ndarray), assert_msg
    assert len(np_array.shape) == 3, assert_msg
    assert np_array.shape[2] == 3, assert_msg

    img = Image.fromarray(np_array, 'RGB')
    return img

animation = VideoClip(make_frame, duration=3) # 3-second clip

# For the export, many options/formats/optimizations are supported
animation.write_videofile("my_animation.mp4", fps=24) # export as video
animation.write_gif("my_animation.gif", fps=24) # export as GIF (slow)
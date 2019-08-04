import imageio
import os

clip = os.path.abspath('NAME OF FILE')


def gif_converter(input_path):
    """Takes in a file path of video and converts it to gif

    Arguments:
        input_path {string} -- path of video file
    """

    # Take the file path, add file extension, create output path
    output_path = os.path.splitext(input_path)[0] + '.gif'

    print(f'Converting {input_path}')

    reader = imageio.get_reader(input_path)
    writer = imageio.get_writer(output_path, fps=60)

    for frames in reader:
        writer.append_data(frames)

    print('Conversion Successful')
    writer.close()


gif_converter(clip)

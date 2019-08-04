import imageio
import os

clip = os.path.abspath('NAME OF FILE')


def gif_converter(input_path, target_format):
    output_path = os.path.splitext(input_path)[0] + target_format

    print(f'Converting {input_path}')

    reader = imageio.get_reader(input_path)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(output_path, fps=fps)

    for frames in reader:
        writer.append_data(frames)

    print('Conversion Successful')
    writer.close()


gif_converter(clip, '.gif')

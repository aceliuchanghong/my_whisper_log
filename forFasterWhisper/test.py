from mp3_utils.converters.audio_format_converter import AudioFormatConverter
from mp3_utils.core.mp3_handler import MP3Handler


def main(converter_type, file_path='../testfile/out/output.mp3') -> MP3Handler:
    """
    Convert MP4 each frame.
    :param converter_type:
    :param file_path:
    """
    Converter = {
        "format": AudioFormatConverter,
    }
    converter = Converter.get(converter_type)(file_path)
    return converter


if __name__ == "__main__":
    mp3_path = '../testfile/out/2.mp3'
    wav_path = '../testfile/2.wav'

    converter_type = "format"
    ans_path = mp3_path

    converter = main(converter_type, wav_path)
    converter.process(ans_path, 'mp3')

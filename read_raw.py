from pathlib import Path
import rawpy


def main():
    data_folder = Path(__file__).parent
    raw_file_path = data_folder / "data/DSC05422.ARW"
    with rawpy.imread(str(raw_file_path)) as raw:
        print()

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import os, sys, shutil

EXT_MAP = {
    ".jpg": "Images", ".png": "Images", ".gif": "Images", ".webp": "Images",
    ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents",
    ".mp3": "Audio", ".wav": "Audio", ".flac": "Audio",
    ".mp4": "Video", ".mkv": "Video", ".avi": "Video",
    ".zip": "Archives", ".tar": "Archives", ".rar": "Archives",
}

def sort_files(directory):
    for f in os.listdir(directory):
        fp = os.path.join(directory, f)
        if os.path.isfile(fp):
            ext = os.path.splitext(f)[1].lower()
            folder = EXT_MAP.get(ext, "Other")
            dest = os.path.join(directory, folder)
            os.makedirs(dest, exist_ok=True)
            shutil.move(fp, os.path.join(dest, f))
            print(f"  {f} -> {folder}/")

if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else "."
    sort_files(d)

"""
SolPNG — A simple CLI tool for managing PNG metadata

Features:
  - Add custom metadata (single or multiple key-value pairs)
  - Read metadata from one or more PNG files
  - Erase metadata from PNGs
  - Supports processing entire folders recursively

Usage Examples:

  # Add metadata
  python solpng.py -w "Author: Sol, License: MIT" image.png

  # Read metadata
  python solpng.py -r image.png

  # Erase metadata
  python solpng.py -e image.png

  # Process an entire folder
  python solpng.py -w "Batch: True" ./images/
"""

import os
import argparse
from PIL import Image, PngImagePlugin



def parse_metadata(metadata_string: str) -> dict:
    """Convert 'Key: Value, Key2: Value2' into a dictionary."""
    metadata = {}
    entries = [entry.strip() for entry in metadata_string.split(",")]
    for entry in entries:
        if ":" in entry:
            key, value = entry.split(":", 1)
            metadata[key.strip()] = value.strip()
    return metadata



def add_metadata_to_png(image_path: str, metadata_string: str) -> None:
    """Add metadata to a PNG file."""
    metadata = parse_metadata(metadata_string)
    try:
        img = Image.open(image_path)
        png_info = PngImagePlugin.PngInfo()

        # Preserve existing metadata
        for k, v in img.info.items():
            png_info.add_text(k, str(v))

        # Add new metadata
        for k, v in metadata.items():
            png_info.add_text(k, v)

        img.save(image_path, pnginfo=png_info)
        print(f"[+] Metadata added to '{image_path}': {metadata}")
    except Exception as e:
        print(f"[!] Error adding metadata to '{image_path}': {e}")



def read_metadata_from_png(image_path: str) -> None:
    """Read and print metadata from a PNG file."""
    try:
        img = Image.open(image_path)
        metadata = img.info

        if metadata:
            print(f"\n--- Metadata in '{image_path}' ---")
            for key, value in metadata.items():
                print(f"{key}: {value}")
        else:
            print(f"[i] No metadata found in '{image_path}'")
    except Exception as e:
        print(f"[!] Error reading metadata from '{image_path}': {e}")



def erase_metadata_from_png(image_path: str) -> None:
    """Erase all metadata from a PNG file."""
    try:
        img = Image.open(image_path)
        img.save(image_path, pnginfo=PngImagePlugin.PngInfo())  # Save with empty metadata
        print(f"[-] Metadata erased from '{image_path}'")
    except Exception as e:
        print(f"[!] Error erasing metadata from '{image_path}': {e}")



def process_paths(paths, operation, metadata=None):
    """Handle files and folders (recursively for folders)."""
    for path in paths:
        if os.path.isfile(path) and path.lower().endswith(".png"):
            operation(path, metadata) if metadata else operation(path)

        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for filename in files:
                    if filename.lower().endswith(".png"):
                        full_path = os.path.join(root, filename)
                        operation(full_path, metadata) if metadata else operation(full_path)

        else:
            print(f"[!] Skipped unsupported or non-PNG file: {path}")



def main():
    parser = argparse.ArgumentParser(
        description="SolPNG — A tool to add, read, or erase PNG metadata."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-w", "--write", help="Add metadata: 'Key1: Value1, Key2: Value2'")
    group.add_argument("-r", "--read", action="store_true", help="Read metadata")
    group.add_argument("-e", "--erase", action="store_true", help="Erase all metadata")

    parser.add_argument("paths", nargs="+", help="PNG file(s) or folder(s) to process")

    args = parser.parse_args()

    if args.write:
        process_paths(args.paths, add_metadata_to_png, args.write)
    elif args.read:
        process_paths(args.paths, read_metadata_from_png)
    elif args.erase:
        process_paths(args.paths, erase_metadata_from_png)


if __name__ == "__main__":
    main()

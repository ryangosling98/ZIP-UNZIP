import gzip
import os

def frequency_analysis(text):
    """Calculates the frequency of each character in the given text.

    Args:
        text: The input text string.

    Returns:
        A dictionary containing character frequencies.
    """

    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def bitarray_conversion(text, pairs):
    """Converts the text to a bitarray based on given letter pairs.

    Args:
        text: The input text string.
        pairs: A tuple of letter pairs, e.g., (('A', 'B'), ('C', 'D')).

    Returns:
        A list of bits representing the text.
    """

    bitarray = []
    for char in text:
        if char in pairs[0]:
            bitarray.append(1)
        else:
            bitarray.append(0)
    return bitarray

def compress_file(data, filename):
    """Compresses the given data using gzip and writes it to a file.

    Args:
        data: The data to be compressed.
        filename: The filename for the compressed file.
    """

    with gzip.open(filename, 'wb') as f:
        f.write(data)

def decompress_file(filename):
    """Decompresses the given gzip file and returns the decompressed data.

    Args:
        filename: The filename of the compressed file.

    Returns:
        The decompressed data.
    """

    with gzip.open(filename, 'rb') as f:
        return f.read()


def verify_file_sizes(input_file, compressed_file, decompressed_file):
    """Verifies the file sizes of input, compressed, and decompressed files.

    Args:
        input_file: The path to the input file.
        compressed_file: The path to the compressed file.
        decompressed_file: The path to the decompressed file.
    """

    input_size = os.path.getsize(input_file)
    compressed_size = os.path.getsize(compressed_file)
    decompressed_size = os.path.getsize(decompressed_file)

    print("Input file size:", input_size, "bytes")
    print("Compressed file size:", compressed_size, "bytes")
    print("Decompressed file size:", decompressed_size, "bytes")

    if decompressed_size == input_size:
        print("Decompression successful: Decompressed file size matches input file size.")
    else:
        print("Decompression failed: Decompressed file size does not match input file size.")

# Main function
def main():
    # Read the input text
    with open('input.txt', 'r') as f:
        text = f.read()

    # Perform frequency analysis
    freq_dict = frequency_analysis(text)
    print(freq_dict)

    # Define letter pairs
    pairs = (('A', 'B'), ('C', 'D'))

    # Convert to bitarray
    bitarray = bitarray_conversion(text, pairs)
    print(bitarray)

    # Compress the bitarray
    compress_file(bytes(bitarray), 'compressed.gz')

    # Decompress the compressed file
    decompressed_data = decompress_file('compressed.gz')
    print(decompressed_data)

    # Write decompressed data to a file (optional)
    with open('decompressed.txt', 'wb') as f:
        f.write(decompressed_data)

    # Verify file sizes
    verify_file_sizes('input.txt', 'compressed.gz', 'decompressed.txt')

if __name__ == "__main__":
    main()
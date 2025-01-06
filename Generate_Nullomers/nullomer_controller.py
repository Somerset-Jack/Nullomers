import argparse
import os
import index_kmers
import generate_nullomers
import firstorder_nullomers



def file_finder(path, length):
    directory = path
    no_of_file = len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])
    print("Number of files found in directory: " + str(no_of_file))
    # Iterates over each file in the selected directory and passes this information to the controller.
    for filename in os.listdir(path):
        # Checking if the file is of FASTA format.
        if filename.endswith(".fa"):
            print(filename + " Is now being processed")
            controller(filename, directory, length)
        elif filename.endswith(".fasta"):
            print(filename + " Is now being processed")
            controller(filename, directory, length)
        elif filename.endswith(".fna"):
            print(filename + " Is now being processed")
            controller(filename, directory, length)
        else: print(filename + " Is not a FASTA file and will not be processed")


def controller(filename, path, length):
    # Calls the correct functions and send the correct the arguments.
    indexed_kmers = index_kmers.run_jellyfish(filename, path, length)
    nullomers = generate_nullomers.nullomer_generation(length, indexed_kmers, filename, path)
    first_order_nullomers = firstorder_nullomers.fo_controller(nullomers, filename, path, length)


if __name__ == '__main__':
    


    parser = argparse.ArgumentParser()
    parser.add_argument("kmer_length", type=int)
    parser.add_argument("path")
    args = parser.parse_args()

    kmer_length = args.kmer_length
    filepath = args.path

    file_finder(filepath, kmer_length)


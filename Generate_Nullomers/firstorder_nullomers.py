import os

def all_possible_mutations(nullomer):
    possible_mutations = {}
    for i, N in enumerate(nullomer):
        if N == "A":
            m1 = nullomer[:i] + 'C' + nullomer[i + 1:]
            m2 = nullomer[:i] + 'G' + nullomer[i + 1:]
            m3 = nullomer[:i] + 'T' + nullomer[i + 1:]
            possible_mutations[m1] = 1
            possible_mutations[m2] = 1
            possible_mutations[m3] = 1
        elif N == "C":
            m1 = nullomer[:i] + 'A' + nullomer[i + 1:]
            m2 = nullomer[:i] + 'G' + nullomer[i + 1:]
            m3 = nullomer[:i] + 'T' + nullomer[i + 1:]
            possible_mutations[m1] = 1
            possible_mutations[m2] = 1
            possible_mutations[m3] = 1
        elif N == "G":
            m1 = nullomer[:i] + 'A' + nullomer[i + 1:]
            m2 = nullomer[:i] + 'C' + nullomer[i + 1:]
            m3 = nullomer[:i] + 'T' + nullomer[i + 1:]
            possible_mutations[m1] = 1
            possible_mutations[m2] = 1
            possible_mutations[m3] = 1

        elif N == "T":
            m1 = nullomer[:i] + 'A' + nullomer[i + 1:]
            m2 = nullomer[:i] + 'C' + nullomer[i + 1:]
            m3 = nullomer[:i] + 'G' + nullomer[i + 1:]
            possible_mutations[m1] = 1
            possible_mutations[m2] = 1
            possible_mutations[m3] = 1
    return possible_mutations

def first_order_check(nullomer_dict, mutation_dict):
    for m in mutation_dict:
        if m not in nullomer_dict:
            return False
    return True

def fo_nullomers_to_file(filename, first_order_nullomers, path, length):
    if not os.path.isdir(path + "/" + str(length) + '_FO_Nullomers'):
        # Creates and runs the command to create a temporary directory that store the files output from jellyfish.
        make_cmd = ("mkdir " + path + "/" + str(length) + "_FO_Nullomers")
        os.system(make_cmd)
    os.chdir(path + "/" + str(length) + "_FO_Nullomers")
    fname = (filename.rsplit(".",1)[0] + "_fo_nullomers.txt")
    f = open(fname, "w")
    for n in first_order_nullomers.keys():  # Iterates through the keys of the dictionary and writes them to a new line in the file
        f.write(n + '\n')
    f.close()


def fo_controller(nullomer_dict, filename, path, length):
    nullomers = nullomer_dict
    first_order_nullomers = {}
    for n in nullomers:
        #is_first_order = False
        all_mutations = all_possible_mutations(n)
        is_first_order = first_order_check(nullomers, all_mutations)
        if is_first_order:
            first_order_nullomers[n] = 1
    fo_nullomers_to_file(filename, first_order_nullomers, path, length)
    print("First Order Nullomers found Successfully")
    return first_order_nullomers
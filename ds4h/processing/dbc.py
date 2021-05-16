import os
from subprocess import Popen, PIPE


def dbc_to_csv(input_folder, output_folder, from_colab=True):
    if (not from_colab) or (os.platform == "win32"):
        raise Exception("Only calling from Colab is being supported")
    args = [
        "/usr/bin/Rscript",
        input_folder,
        output_folder
    ]
    p = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode
    return output.decode(), err, rc
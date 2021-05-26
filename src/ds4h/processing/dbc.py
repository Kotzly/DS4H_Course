import os, sys
from subprocess import Popen, PIPE
from pathlib import Path
from simpledbf import Dbf5

CURRENT_PATH = Path(__file__).absolute().parent
RSCRIPT_PATH = "/usr/bin/Rscript"

def dbc_to_csv(input_folder, output_folder):

    input_folder, output_folder = Path(input_folder), Path(output_folder)

    output_folder.mkdir(exist_ok=True, parents=True)

    if sys.platform == "win32":
        raise Exception("Only calling from Colab or Linux is being supported")

    assert Path(RSCRIPT_PATH).exists(), "Did not find R installation in {}.".format(RSCRIPT_PATH)

    args = [
        RSCRIPT_PATH,
        str(CURRENT_PATH / "dbc_to_csv.r"),
        str(input_folder) + "/",
        str(output_folder) + "/"
    ]
    p = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode

    print(output.decode())
    print(err.decode())

    if rc != 0:
        raise Exception("Error in {}.\nTry running as sudo".format(" ".join(args)))

    return output.decode(), err, rc

def dbf_to_csv(dbf_filepath, output_folder):
    output_folder = Path(output_folder)
    dbf = Dbf5(dbf_filepath)
    dbf.to_csv(
        output_folder / dbf_filepath.with_suffix(".csv").name
    )
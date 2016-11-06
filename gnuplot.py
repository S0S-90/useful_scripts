import subprocess

PATH_TO_GNUPLOT = r"C:\Program Files (x86)\gnuplot\bin\gnuplot.exe"

list_of_lines = []           # read inputfile
with open("input_for_gnuplot.txt") as inp:
    for line in inp:
        list_of_lines.append(line)

end_general_input = list_of_lines.index("PLOT_INPUT\n")-1        # determine where sections begin and end
start_plot_functions = list_of_lines.index("PLOT_FUNCTIONS\n")+1

string = "".join(list_of_lines[1:end_general_input]) + "plot "                          # general input
for f in list_of_lines[start_plot_functions:]:                                          # functions and plot_input
    func = f.split(",")  # before "," -> before plotinput; after "," -> after plotinput
    string = string + func[0] + " " + list_of_lines[end_general_input+2].replace("\n","") + func[1].replace("\n", ", ")

with open("gnuinp.plt","w") as gnuinp:  #write inputfile for gnuplot
    gnuinp.write(string)

subprocess.call([PATH_TO_GNUPLOT, "gnuinp.plt"]) # call gnuplot (output-type and name of the output-file have to be specified in the inputfile)





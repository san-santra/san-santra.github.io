import os.path

filename_prefix = ["canon", "castle", "cityscape", "cones",
                   "flags", "forest1", "mountain", "ny12",
                   "ny17", "Oberfallenberg4", "Pluie_Alsacienne",
                   "pumpkins", "stadium1", "swan", "tiananmen",
                   "toys", "train", "yellowmountain"]


if __name__ == '__main__':
    r_f = open("results.md", "w")

    # Write preamble
    preamble = "---"+"\n" + \
               "layout: default"+"\n" + \
               "title: Result Comparison"+"\n"+ \
               "---"+"\n"

    r_f.write(preamble)
    

    # add content to r_f
    for image in filename_prefix:
        html_tags = "### "+image+"\n"+ \
                    "<div class=\"row\">"+"\n"+ \
                    "<div class=\"col-md-6\">"+"\n"+ \
                    "Original"+"\n"+ \
	            "<img src=\"varlight_dehaze_results/"+image+"_input.jpg\" />"+"\n"+ \
                    "</div>"+"\n"+ \
                    "<div class=\"col-md-6\">"+"\n"+ \
                    "Our method"+"\n"+ \
                    "<img src=\"varlight_dehaze_results/"+image+"_our.jpg\" />"+"\n"+ \
                    "</div>"+"\n"

        ## test file existance - cl
        if os.path.exists("varlight_dehaze_results/"+image+"_cl.jpg"):
            html_tags += "<div class=\"col-md-6\">"+"\n"+ \
                         "Fattal color line"+"\n"+ \
	                 "<img src=\"varlight_dehaze_results/"+image+"_cl.jpg\" />"+"\n"+ \
	                 "</div>"+"\n"


        # # test file existance
        if os.path.exists("varlight_dehaze_results/"+image+"_dc.jpg"):
            html_tags += "<div class=\"col-md-6\">"+"\n"+ \
                         "He et al."+"\n"+ \
	                 "<img src=\"varlight_dehaze_results/"+image+"_dc.jpg\" />"+"\n"+ \
	                 "</div>"+"\n"

        # this needs to be added to complete the first div
        html_tags += "</div>"+"\n"

        r_f.write(html_tags)
        r_f.write("\n")
        

    r_f.close()

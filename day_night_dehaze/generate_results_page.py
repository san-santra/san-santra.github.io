import os.path

filename_prefix = ["aerial", "canon", "castle", "cityscape", 
		   "cologne_cathedral", "cones", "flags", 
		   "fog_on_the_bay", "forest", "harbin_smog", "house",
		   "miri_haze", "mountain", "newyork", "newyork2", 
		   "night_road", "ny12", "ny17", "Oberfallenberg", 
		   "pumpkins", "stadium", "swan", "sweden", 
		   "tiananmen", "toys", "train", "yellowmountain"]

basepath_results = '/home/sanchayans/lab/san-santra.github.io/public'
site_basepath_res = "{{ site.baseurl }}/public"


if __name__ == '__main__':
    result_file = open("results.md", "w")

    # Write preamble
    preamble = "---"+"\n" + \
               "layout: default"+"\n" + \
               "title: Result Comparison"+"\n"+ \
               "---"+"\n\n"
    
    references = "The image are scaled in the page for display puropse. Use 'Right Click -> View Image' to get full size image.\n\n" + \
                 "### References" + "\n" + \
                 "[He et al.](http://kaiminghe.com/cvpr09/index.html) - Single Image Haze Removal using Dark Channel Prior, in TPAMI 2011 <br/>" + "\n" + \
                "[Fattal](http://www.cs.huji.ac.il/~raananf/projects/dehaze_cl/) - Dehazing using color lines, in ACM ToG 2014 <br/>" + "\n" + \
                "[Li et al.](http://yu-li.github.io/) - Nighttime Haze Removal with Glow and Multiple Light Colors, in ICCV 2015 <br/>" + "\n" + "<hr /> \n"

    result_file.write(preamble)
    result_file.write(references)
    

    # add content to result_file
    for image in filename_prefix:
        html_tags = "\n### "+image+"\n"+ \
                    "<div class=\"row\">"+"\n"+ \
                    "<div class=\"col-md-6\">"+"\n"+ \
                    "Original"+"\n"+ \
	            "<img src=\""+site_basepath_res+"/haze_image/"+image+"_input.jpg\" />"+"\n"+ \
                    "</div>"+"\n"+ \
                    "<div class=\"col-md-6\">"+"\n"+ \
                    "Computed Airlight"+"\n"+ \
                    "<img src=\"results/"+image+"_airlight.jpg\" />"+"\n"+ \
                    "</div>"+"\n" + \
                    "<div class=\"col-md-6\">"+"\n"+ \
                    "Our method"+"\n"+ \
                    "<img src=\"results/"+image+"_our.jpg\" />"+"\n"+ \
                    "</div>"+"\n"

        ## test file existance - cl
        if os.path.exists(basepath_results+"/output_cl/"+image+"_output_cl.jpg"):
            html_tags += "<div class=\"col-md-6\">"+"\n"+ \
                         "Fattal color line"+"\n"+ \
	                 "<img src=\""+site_basepath_res+"/output_cl/"+image+"_output_cl.jpg\" />"+"\n"+ \
	                 "</div>"+"\n"


        # # test file existance - dc
        if os.path.exists(basepath_results+"/output_dc/"+image+"_dc.jpg"):
            html_tags += "<div class=\"col-md-6\">"+"\n"+ \
                         "He et al."+"\n"+ \
	                 "<img src=\""+site_basepath_res+"/output_dc/"+image+"_dc.jpg\" />"+"\n"+ \
	                 "</div>"+"\n"

	# # test file existance - li
        if os.path.exists(basepath_results+"/output_li/"+image+"_li.jpg"):
            html_tags += "<div class=\"col-md-6\">"+"\n"+ \
                         "Li et al."+"\n"+ \
	                 "<img src=\""+site_basepath_res+"/output_li/"+image+"_li.jpg\" />"+"\n"+ \
	                 "</div>"+"\n"
		

        # this needs to be added to complete the first div
        html_tags += "</div>"+"\n"

        result_file.write(html_tags)
        result_file.write("\n")
        

    result_file.close()

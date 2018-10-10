import os.path

filename_prefix = ["aerial", "buildings", "canon", "castle", "cityscape",
                   "cones", "dubai", "flags",
                   "florence", "forest", "herzeliya",
                   "hongkong", "house", "lviv", 
                   "mountain", "newyork", "newyork2",
                   "ny12", "ny17",
                   "pumpkins", "snow", "stadium", "swan", "sweden",
                   "tiananmen", "toys", "train", "tree", "y01",
                   "y16", "yellowmountain"]

basepath_results = '/home/sanchayans/lab/san-santra.github.io/public'
site_basepath_res = "{{ site.baseurl }}/public"


if __name__ == '__main__':
    result_file = open("results.md", "w")

    # Write preamble
    preamble = "---"+"\n" + \
               "layout: default"+"\n" + \
               "title: Result Comparison"+"\n" + \
               "---"+"\n\n"

    references = "The image are scaled in the page for viewing." + \
        "Use 'Right Click -> View Image' to get full size image.\n\n" + \
        "### References" + "\n" + \
        "[He et al.](http://kaiminghe.com/cvpr09/index.html)" + \
        "- Single Image Haze Removal using Dark Channel Prior, in TPAMI 2011 <br/>" + "\n" + \
        "[Fattal](http://www.cs.huji.ac.il/~raananf/projects/dehaze_cl/)" + \
        "- Dehazing using color lines, in ACM ToG 2014 <br/>" + "\n" + \
        "[Ren et al.](https://sites.google.com/site/renwenqi888/research/dehazing/mscnndehazing)" + \
        "- Single Image Dehazing via Multi-Scale Convolutional Neural Networks, in ECCV 2016 <br/>" + "\n" + "<hr /> \n"

    result_file.write(preamble)
    result_file.write(references)

    # add content to result_file
    for image in filename_prefix:
        html_tags = "\n### "+image+"\n" + \
                    "<div class=\"row\">"+"\n" + \
                    "<div class=\"col-md-6\">"+"\n" + \
                    "Original"+"\n" + \
                    "<img src=\""+site_basepath_res+"/haze_image/"+image+"_input.jpg\" />"+"\n" + \
                    "</div>"+"\n" + \
                    "<div class=\"col-md-6\">"+"\n" + \
                    "Our method"+"\n" + \
                    "<img src=\"results/"+image+"_our.jpg\" />"+"\n" + \
                    "</div>"+"\n"

        # test file existance - cl
        if os.path.exists(basepath_results+"/output_cl/"+image+"_output_cl.jpg"):
            html_tags += "<div class=\"col-md-6\">"+"\n" + \
                         "Fattal color line"+"\n" + \
                         "<img src=\""+site_basepath_res+"/output_cl/"+image+"_output_cl.jpg\" />"+"\n" + \
                         "</div>"+"\n"

        #  test file existance - dc
        if os.path.exists(basepath_results+"/output_dc/"+image+"_dc.jpg"):
            html_tags += "<div class=\"col-md-6\">"+"\n" + \
                         "He et al."+"\n" + \
                         "<img src=\""+site_basepath_res+"/output_dc/"+image+"_dc.jpg\" />"+"\n" + \
                         "</div>"+"\n"

        # test file existance - mscnn
        if os.path.exists(basepath_results+"/output_mscnn/"+image+"_mscnn.jpg"):
            html_tags += "<div class=\"col-md-6\">"+"\n" + \
                         "Ren et al."+"\n" + \
                         "<img src=\""+site_basepath_res+"/output_mscnn/"+image+"_mscnn.jpg\" />"+"\n" + \
                         "</div>"+"\n"

        # this needs to be added to complete the first div
        html_tags += "</div>"+"\n"

        result_file.write(html_tags)
        result_file.write("\n")

    result_file.close()

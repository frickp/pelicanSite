Title: Measuring cancer cell dynamics in response to therapy
Date: 2015-10-09 10:20
Modified: 2015-10-02 19:30
Category: blog
Tags: R, research, systems
Slug: r-phd-code
Authors: Peter Frick
Summary: Example R code to process highly-multiplexed cancer drug responses. Formatted so that *you* should be able to run it on a mac.

###Purpose
The goal of this post is to allow *you* to run some of the code I used during my PhD. 
I don't want to assume that you know how to use R, or how to use git. So, follow the steps to see a flavor of what I did.

If you are curious, the research goal here is to quantify the dynamic response of many
cancer cell clones in response to drugs. Clones just means a group of cells with common
behavior and ancestry. You could think of them like a tribe, where tumor is composed of many clones, or tribes. Evolution works by 
selecting more fit individuals (clones in this case) amongst a diverse population.

Easy right? Well, if you could quantify the diversity of a population, and could understand
 what each individual was doing, you should be able to predict the long-term behavior of the
 whole population. This code is about quantifying the diversity of drug responses amongst thousands of clones. If you want to learn more, the code was used in [this paper](http://www.ncbi.nlm.nih.gov/pubmed/25600161).

Digression over. Here's how to run the code. I have this optimized for use on mac computers (n=2).

###Instructions

1. Install [R](https://www.r-project.org).
    - note, that this is optimized for version 3.2.
2. Follow this [link](https://raw.githubusercontent.com/frickp/cFPpaper-Rcode/master/copyPaste_rawDataAndPreprocessingScripts/LibraryLoader.R), copy the code and paste it in the R console. Run the code by pressing return.
    - This makes sure you have everything that you need installed.
3. Follow this [link](https://raw.githubusercontent.com/frickp/cFPpaper-Rcode/master/copyPaste_scripts/Fig3-BoxplotsAndLinearModels.r).
4. Copy and paste the code into the R console and hit return
5. That's it! If you liked it you can try [this link](https://raw.githubusercontent.com/frickp/cFPpaper-Rcode/master/copyPaste_scripts/Fig4-Drug-conc-cFP.R), which I like, or any of the other .R files in [this directory](https://github.com/frickp/cFPpaper-Rcode/tree/master/copyPaste_scripts).

### Commentary

Ok, so what is the code doing? Usually you have to point R to where the data are stored locally, but I don't want to assume you know how to do that or to clone a git directory.
So, using the `RCurl` package, I am telling R to pull all the needed data and functions directly from my online GitHub directory. You can see these in the code as `source` commands. I've found this helpful in increasing the readability and modularity of the code.

If you followed my suggestion in step 3, the code will do some pre-processing using functions read from the indicated `source`.
First is `cFP_norm72.r`. This code reads in a pre-organized dataset containing the timecourse dynamics of thousands of clones across different drugs. After reading in the data, each clone is assigned a unique ID and is log normalized.
Next, the code reads in `cFP-comboEstimateSlopes.r`. This script approximates the drug response of each each clone as a growth rate, computed as the slope derived from the linear model best fit.
Lastly is `HGmodel.r`, which is developed for another paper, but useful here for computing the best fit for a [skew-normal distribution](https://en.wikipedia.org/wiki/Skew_normal_distribution).

That's a taste of it. I hope you liked what you saw. A lot more of the scientifically interesting/math modeling stuff I'm much more proud of, but is not yet online (unpublished). Let me know if you like to talk about it offline.


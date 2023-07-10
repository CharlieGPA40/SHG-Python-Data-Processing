# SHG-Python-Data-Processing
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

The purpose of this program is to process the lab RA-SHG data:
1. Auto signal selection and process the corresponding data
2. Data fitting program to fir the lab results

For our equipment lists, check our website: [Link](https://jinlab.auburn.edu/our-lab/)
	
Note: You can modify this program to fit your experimental setup.

## Requirements
1. This package requires Python and/or Python IDE
2. The size of the data should be 512x512
3. It must be RA measurement (not fixed anylzer measurement)
4. Format of all the file need to be txt (but you can modify the code to fit your applications)
5. We use `Experimental_Parameters.txt` to log our experimental requirement (You can find the example under Example/)
6. Temperature depemdence and imaging mode still in a preliminary development phase 

## Running
1. Run from the Python IDE using code `main.py`.

## About us
Our group focuses on studying novel phases of matter in low-dimensional quantum systems. We exploit a variety of experimental techniques, such as femtosecond laser-based nonlinear optical spectroscopy and synchrotron-based photoemission spectroscopy/microscopy, to investigate the electronic and magnetic structure at the surface and interface.

## Contact
This project is contributed by:
* Chunli Tang (Auburn University – Electrical and Computer Engineering: chunli.tang@auburn.edu)

Advisor:
* [Dr. Masoud Mahjouri-Samani](http://wp.auburn.edu/Mahjouri/) (Auburn University – Electrical and Computer Engineering: mzm0185@auburn.edu)
* [Dr. Wencan Jin](http://wp.auburn.edu/JinLab/) (Auburn University – Physics Department: wjin@auburn.edu)

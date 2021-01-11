# Duplicate Images
using the image hashing identifies the similar images and moves the duplicate images to another folder
<h1> dependencies</h1>
<p>
  <ul>
    <li> pillow </li>
    <li> os </li>
    <li> imagehash </li>
    <li> shutil </li>
  </ul>
  </p>
  <p>
    <h1>install the dependencies using pip</h1>
      <ul>
        <li>pip3 install Pillow</li>
         <li>pip3 install os-sys</li>
         <li>pip3 install ImageHash</li>
         <li>pip3 install pytest-shutil </li>
      </ul>
  </p>
  
<h1>**Remember**</h1>
<p> Add prefix of r to the source and destination folder
 It will be something like this
source=r"C:\Users\Rajesh\Desktop\miniProjectPython\Images"<br>
  destination = r'C:\Users\Rajesh\Desktop\miniProjectPython\duplicate'</p>
 
<h3> remember to take a backup, before running the program <h3>

<h1>How it works</h1>
<p>
  The image is converted into a unique hash which will be a string. Each image has a unique fingerprint,
  which can be used for identifing the duplicate images. Perceptual hash is the best and ideal hashing algoritms for image processing.  
</p>
  

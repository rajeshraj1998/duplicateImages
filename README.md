# duplicateImages
using the image hashing identifies the similar images and moves the duplicate images to another folder
<h1> dependencies<h1>
<p>
  <ul>
    <li> pillow </li>
    <li> os </li>
    <li> imagehash </li>
    <li> shutil </li>
  </ul>
  </p>
  <p>
    <h2>install the dependencies using pip</h2>
      <ul>
        <li>pip3 install Pillow</li>
         <li>pip3 install os-sys</li>
         <li>pip3 install ImageHash</li>
         <li>pip3 install pytest-shutil </li>
      </ul>
  </p>
  
<h3>**Remember**<h3>
 Add prefix of r to the source and destination folder
 It will be something like this
<h5>source=r"C:\Users\Rajesh\Desktop\miniProjectPython\Images"<br>
destination = r'C:\Users\Rajesh\Desktop\miniProjectPython\duplicate'</h5>
 
<h4> remember to take a backup, before running the program <h4>

<h1>How it works<h1>
<p>
  The image is converted into a unique hash which will be a string. Each image has a unique fingerprint,
  which can be used for identifing the duplicate images. Perceptual hash is the best and ideal hashing algoritms for image processing.  
</p>
  

# Duplicate Images
using the image hashing to identify the similar images.
<h1> Dependencies</h1>
<p>
  <ul>
    <li> pillow </li>
    <li> os </li>
    <li> imagehash </li>
    <li> shutil </li>
  </ul>
  </p>
  <p>
    <h1>Install the dependencies using pip</h1>
      <ul>
        <li>pip3 install Pillow</li>
         <li>pip3 install os-sys</li>
         <li>pip3 install ImageHash</li>
         <li>pip3 install pytest-shutil </li>
      </ul>
  </p>
  
<h1>**Remember**</h1>
<p> Add prefix of r to the source and destination folder. 
 It will be something like this<br>
source=r"C:\Users\Rajesh\Desktop\miniProjectPython\Images"<br>
destination = r'C:\Users\Rajesh\Desktop\miniProjectPython\duplicate'</p>
 
<h3> Remember to take a backup, before running the program <h3>

<h1>How it works</h1>
<p>
  The image is converted into a unique hash which will be a string. Each image has a unique fingerprint,
  which can be used for identifing the duplicate images. Few of the image hashing that are included in the library are 
  <ul>
    <li>average hashing (aHash)</li>
    <li>perception hashing (pHash)</li>
    <li>difference hashing (dHash)</li>
    <li>wavelet hashing (wHash)</li>
    </ul>
</p>
<h1>Reference<h1>
  <p>ourcodeworld
<a href="https://ourcodeworld.com/articles/read/1006/how-to-determine-whether-2-images-are-equal-or-not-with-the-perceptual-hash-in-python">click here</a></p>
  
  
  

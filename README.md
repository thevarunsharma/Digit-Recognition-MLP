# Handwritten Digit Recognizer
<h2>Features of the Model</h2>
 <p>A python program which uses a model trained on MNIST dataset for digit recognition. Following are the features of the model :</p>
 <ul>
<li>The model is a Neural Network with 4-Layers consisting of 300, 200, 110 and 10 units for layers 1, 2, 3 and 4 respectively.</li>
<li>L2-Regularisation has been used to prevent the overfitting of the model.</li>
<li>The model inputs an feature vector of size 784, where each feature signifies each pixel of the 28x28 pixel image.</li>
 </ul>
 
 <h2>Components of the Project</h2>
 <p>The repository consists of the following files and folders. (To use the handwritten digit recognizer run the python file 'main.py')
 <ul>
 <li><b>main.py : </b>Main python file to run the program for digit recognition.</li>
 <li><b>canvas.py : </b>Python program to run tkinter canvas widget and get handwritten digit input.</li>
 <li><b>canvas.pyc : </b>Python file canvas.py bundled as module file('.pyc') to be imported in main.py.</li>
 <li><b>utils : </b>It contains the following files-
 <ul>
  <li><i>weights.npy</i> : Contains the array of weights saved in NumPy (.npy) file format.</li>
  <li><i>temp.jpg</i> : A temporary image file saved as jpeg from from the canvas input.</li>
  </ul>
 </li>
 </ul>
<h2>Requirements:</h2>
<p>(The following packages are needed to be pre-installed in order to run the project)</p>
 <ul>
 <li>NumPy</li>
 <li>SciPy</li>
 <li>PIL</li>
 <li>Tkinter</li>
